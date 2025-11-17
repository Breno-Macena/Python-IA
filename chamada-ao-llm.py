# 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
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
)

response = client.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[
        {"role": "system", "content": "Você é um assistente de IA que sempre responde de forma muito sarcástica."},
        {"role": "user", "content": "O que é a IA generativa?"}
    ],
    temperature=1.0
)

print(response.choices[0].message.content)
