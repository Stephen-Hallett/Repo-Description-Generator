# Repo-Description-Generator

A langchain prompt chaining implementation which generates simple project descriptions based on contents of a README or documentation file.

### Example usage

##### Install the package

```sh
pip install git+https://github.com/your-username/description-generator.git
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

generator.generate(readme_contents)
```
