import openai

openai.api_key = "YOUR_API_KEY"

def rewrite_email(email_text, tone="professional"):
    prompt = f"""
    Rewrite the following email in a {tone} tone:
    "{email_text}"
    Make it polite, clear, and concise.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

print(rewrite_email("Hey I am waiting for update. No one replied yet."))