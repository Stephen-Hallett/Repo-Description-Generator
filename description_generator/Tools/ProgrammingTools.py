from pydantic import BaseModel, Field


class ProgrammingTools(BaseModel):
    languages: list[str] = Field(
        ..., description="A list of the programming languages used in the project"
    )
    frameworks: list[str] = Field(
        ..., description="A list of the programming frameworks used in the project"
    )
