from langchain_core.prompts import ChatPromptTemplate

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
