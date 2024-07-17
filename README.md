# AI If-Elif

AI If-Elif is a Python library that provides AI-enhanced conditional logic using OpenAI's GPT models. It allows you to use natural language conditions in your if-else statements and elif chains.

## Installation

You can install AI If-Elif using pip:

```
pip install ai_if_elif
```

## Usage

First, make sure to set your OpenAI API key as an environment variable:

```python
import os
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'
```

Then you can use the library as follows:

```python
from ai_if_elif import ai_if, ai_elif

# Simple boolean condition
result = ai_if(True, lambda: "Condition is True", lambda: "Condition is False")
print(result)  # Output: Condition is True

# AI-evaluated condition
result = ai_if("Is the sky blue?", lambda: "The sky is blue", lambda: "The sky is not blue")
print(result)  # Output depends on AI evaluation

# AI-evaluated elif chain
conditions_actions = [
    ("Is it raining?", lambda: "Bring an umbrella"),
    ("Is it sunny?", lambda: "Wear sunglasses"),
    ("Is it cloudy?", lambda: "Expect changes in weather")
]
result = ai_elif(conditions_actions)
print(result)  # Output depends on AI evaluation of conditions
```

## Note

This library uses OpenAI's API, which may incur costs. Please be aware of your usage and the associated costs.

## License

This project is licensed under the MIT License.