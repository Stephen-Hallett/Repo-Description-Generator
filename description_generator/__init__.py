import importlib.resources

from langchain.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.output_parsers.string import StrOutputParser
from langchain_openai import ChatOpenAI

from .Prompts.Prompts import description_prompt, info_prompt, purpose_prompt
from .Tools.ProgrammingTools import ProgrammingTools


class DescriptionGenerator:
    def __init__(self, openai_key: str) -> None:
        self.info_chain = (
            info_prompt
            | ChatOpenAI(api_key=openai_key, temperature=0.1).bind_tools(
                [ProgrammingTools], strict=True, tool_choice="ProgrammingTools"
            )
            | PydanticToolsParser(tools=[ProgrammingTools])
        )
        self.purpose_chain = (
            purpose_prompt
            | ChatOpenAI(api_key=openai_key, temperature=0.5)
            | StrOutputParser()
        )
        self.description_chain = (
            description_prompt
            | ChatOpenAI(api_key=openai_key, temperature=0.8)
            | StrOutputParser()
        )

        with (
            importlib.resources.files("description_generator.Knowledge")
            .joinpath("README1.md")
            .open("r") as f
        ):
            self.example_contents = f.read()

    def generate(self, contents: str) -> str:
        """Generate a description for the given readme/documentation content.

        :param contents: A projects documentation in string form.
        :return: A description of the project in a few sentences.
        """
        tools_results = self.info_chain.invoke(
            {"example_contents": self.example_contents, "input": contents}
        )

        purpose_result = self.purpose_chain.invoke(
            {"example_contents": self.example_contents, "input": contents}
        )

        return self.description_chain.invoke(
            {
                "languages": ", ".join(list(tools_results[0].languages)),
                "frameworks": ", ".join(list(tools_results[0].frameworks)),
                "purpose": purpose_result,
            }
        )
