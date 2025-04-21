import os

from langchain.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class ProgrammingTools(BaseModel):
    languages: list[str] = Field(
        ..., description="A list of the programming languages used in the project"
    )
    frameworks: list[str] = Field(
        ..., description="A list of the programming frameworks used in the project"
    )

# -----------------

info_model = ChatOpenAI(
    api_key=os.environ["OPENAI_API_KEY"], temperature=0.1
).bind_tools([ProgrammingTools], strict=True, tool_choice="ProgrammingTools")

info_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You have a world class talent for summarising content."),
        (
            "human",
            "Please summarise the contents of this readme file.\n {example_contents}",
        ),
        (
            "ai",
            "{{'languages': ['Python', 'Terraform'], 'frameworks': ['FastAPI', 'Azure Functions']}}",
        ),
        ("human", "Please summarise the contents of this readme file.\n {input}"),
    ]
)

purpose_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You have a world class talent for summarising content."),
        (
            "human",
            "What is the overarching purpose of the project with the following README? {example_contents}",
        ),
        (
            "ai",
            "The purpose of this project is to provide template resources to deploy a FastAPI server on an Azure function app",
        ),
        (
            "human",
            "What is the overarching purpose of the project with the following README? {input}",
        ),
    ]
)

description_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You have a world class talent for creating descriptions of \
projects. These descriptions are entirely factual, and are only 2 or 3 sentences long.",
        ),
        (
            "human",
            "Please generate a description of a project which uses the programming\
languages: Python, Terraform. With frameworks FastAPI, Azure Functions. \n\
The project aims to provide resources and workflows for deploying a FastAPI server on \
an Azure function app. It includes guidance on setting up Azure resources, integrating \
with GitHub actions, and updating infrastructure and FastAPI code for customization.",
        ),
        (
            "ai",
            "This project leverages Python and Terraform to establish resources and \
workflows for deploying a FastAPI server on an Azure Function app. It offers \
comprehensive instructions on configuring Azure resources, integrating with GitHub \
actions, and making updates to infrastructure and FastAPI code for personalized \
deployments.",
        ),
        (
            "human",
            "Please generate a description of a project which uses the programming\
languages: {languages}. With frameworks {frameworks}. \n\
{purpose}",
        ),
    ]
)

info_chain = info_prompt | info_model | PydanticToolsParser(tools=[ProgrammingTools])
purpose_chain = (
    purpose_prompt
    | ChatOpenAI(api_key=os.environ["OPENAI_API_KEY"], temperature=0.5)
    | StrOutputParser()
)
final_chain = (
    description_prompt
    | ChatOpenAI(api_key=os.environ["OPENAI_API_KEY"], temperature=0.7)
    | StrOutputParser()
)

with open("example_readme.md") as f:
    example_contents = f.read()

with open("test_readme.md") as f:
    contents = f.read()


tools_results = info_chain.invoke(
    {"example_contents": example_contents, "input": contents}
)

purpose_result = purpose_chain.invoke(
    {"example_contents": example_contents, "input": contents}
)

description = final_chain.invoke(
    {
        "languages": ", ".join(list(tools_results[0].languages)),
        "frameworks": ", ".join(list(tools_results[0].frameworks)),
        "purpose": purpose_result,
    }
)

