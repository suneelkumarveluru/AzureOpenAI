# Azure OpenAI Python Examples

A minimal example of Azure OpenAI chat-completion API integration.

## Setup

Requires Python 3.10+ and access to an Azure OpenAI deployment.

```bash
python -m pip install openai
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
export AZURE_OPENAI_API_KEY="your-key"
export AZURE_OPENAI_DEPLOYMENT="your-deployment-name"
export AZURE_OPENAI_API_VERSION="your-supported-api-version"
python examples/chat_completion.py
```

Use `$env:NAME = "value"` to set environment variables on Windows PowerShell.

Keep keys out of source control and use secret management or identity authentication in production. API usage may incur costs. This example calls a live service and is not an offline simulation.
