from openai import OpenAI
import os

# Ensure OpenAI API key is set
if 'OPENAI_API_KEY' not in os.environ:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def ai_if(condition, true_action, false_action=None):
    """
    Executes true_action if condition is True, otherwise executes false_action.
    
    :param condition: A boolean condition
    :param true_action: Function to execute if condition is True
    :param false_action: Function to execute if condition is False (optional)
    :return: Result of the executed action
    """
    if eval_condition_with_ai(condition):
        return true_action()
    elif false_action:
        return false_action()

def ai_elif(conditions_actions):
    """
    Executes the action corresponding to the first true condition.
    
    :param conditions_actions: List of (condition, action) tuples
    :return: Result of the executed action or None if no condition is met
    """
    for condition, action in conditions_actions:
        if eval_condition_with_ai(condition):
            return action()
    return None


def eval_condition_with_ai(condition):
    """
    Evaluates a condition using OpenAI's Chat API.    
    """
    if isinstance(condition, bool):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that evaluates conditions."},
                {"role": "user", "content": f"Evaluate this condition and respond with only 'True' or 'False': {condition}"}
            ]
        )
        print(condition)
        print(response.choices[0].message.content)
        result = response.choices[0].message.content.strip().lower() == 'true'
    else:
        raise ValueError("Condition must be a boolean")

    return result
    