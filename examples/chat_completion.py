"""Azure OpenAI SDK example.

pip install openai
Set AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY,
AZURE_OPENAI_DEPLOYMENT, and AZURE_OPENAI_API_VERSION.
"""
import os
from openai import AzureOpenAI


def ask(question: str) -> str:
    client = AzureOpenAI(
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    )
    response = client.chat.completions.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        messages=[{"role": "user", "content": question}],
        temperature=0,
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print(ask("Explain data lineage in two sentences."))
