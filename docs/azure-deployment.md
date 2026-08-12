# Azure Deployment Roadmap

> **Note:** Azure infrastructure provisioning is intentionally out of scope for the boilerplate.
> This document describes the target deployment path for future feature branches.

## Planned Azure Resources

| Resource | Purpose |
|----------|---------|
| Azure Container Registry (ACR) | Store Docker images |
| Azure Container Apps | Host the FastAPI service |
| Azure OpenAI Service | LLM inference (GPT-4o) |
| Azure AI Search | Vector store for RAG (feature branch) |
| Azure Key Vault | Secrets management |
| Azure Monitor / App Insights | Observability |

## Deployment Steps (Future)

1. Build and push Docker image to ACR.
2. Deploy to Azure Container Apps with environment variables from Key Vault.
3. Configure managed identity for Azure OpenAI and AI Search access.
4. Set up CI/CD pipeline to auto-deploy on `main` merges.

## Environment Variables Required

Refer to `.env.example` for the full list of configuration keys.
