import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-5-nano"


def parse_expense(user_text: str):

    system_prompt = """
    You are a financial assistant. Extract expense details from the user's text.
    Return ONLY a JSON object with these keys:
    - "amount": (number)
    - "category": (string, summarize into one word like Food, Transport, Bills, Entertainment)
    - "description": (string, brief summary)
    
    If you cannot find an amount, return "amount": 0.
    """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": system_prompt},
                      {"role": "user", "content": user_text}],
            response_format={"type": "json_object"}
        )
        ai_response = response.choices[0].message.content
        data = json.loads(ai_response)
        return data

    except Exception as e:
        print(f"Error parsing expense: {e}")
        return None
