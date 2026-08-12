# Azure Deployment Roadmap

> **Note:** Azure infrastructure is not provisioned in this boilerplate.
> This document outlines the planned deployment path for future feature branches.

## Target Architecture

- **Azure Container Apps** — serverless container hosting for the FastAPI backend.
- **Azure OpenAI Service** — LLM inference (GPT-4o / GPT-4 Turbo).
- **Azure Cognitive Search** — vector index for RAG pipelines.
- **Azure Container Registry** — private Docker image registry.

## Planned Steps

1. **Containerise** — `Dockerfile` and `docker-compose.yml` are already provided.
2. **Build & push image** — GitHub Actions workflow (`feature/azure-deployment`).
3. **Provision Container App** — via Azure CLI or Bicep templates.
4. **Configure secrets** — store `.env` values in Azure Key Vault.
5. **Set up CI/CD** — auto-deploy on merge to `main`.

## Environment Variables (Azure)

All secrets listed in `.env.example` must be set as environment variables in the
Azure Container App (or loaded from Key Vault references).
