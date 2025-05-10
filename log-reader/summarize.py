import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_logs(log_data):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You're a security analyst."},
            {"role": "user", "content": f"Summarize this:\n{log_data}"}
        ]
    )
    return response.choices[0].message.content
