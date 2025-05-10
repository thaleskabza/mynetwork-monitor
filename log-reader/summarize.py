from openai import OpenAI
import os

def summarize_logs(log_data):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"Summarize and identify any suspicious patterns in:\n\n{log_data}"
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content
