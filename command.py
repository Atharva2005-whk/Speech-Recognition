import openai

# Set your API key (ideally use environment variables in production)
openai.api_key = "your-api-key"

from openai import OpenAI

client = OpenAI()

def ai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
