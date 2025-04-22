# Repo-Description-Generator

A langchain prompt chaining implementation which generates simple project descriptions based on contents of a README or documentation file.

### Example usage

##### Install the package

```sh
pip install git+https://github.com/Stephen-Hallett/Repo-Description-Generator.git
```

Using the DescriptionGenerator class, you can generate a description with just a few lines of code.

```python
import os

import requests

from description_generator import DescriptionGenerator

readme_contents = requests.get(
    "https://raw.githubusercontent.com/Stephen-Hallett/Repo-Description-Generator/main/README.md",
    timeout=30,
).text

generator = DescriptionGenerator(os.environ["OPENAI_API_KEY"])

print(generator.generate(readme_contents))

# This project utilizes Python with the Langchain framework to create a tool that employs a language model
# for automating the generation of project descriptions by analyzing the content of a README or documentation file.
```
