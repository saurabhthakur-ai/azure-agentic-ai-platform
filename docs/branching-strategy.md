# Branching Strategy

## Overview

`main` is the stable, framework-neutral base branch. All feature development happens in dedicated branches that are merged back via pull request.

## Branch Map

```
main
├── feature/project-foundation   ← initial boilerplate (this branch)
├── feature/langchain-rag        ← RAG pipeline with Azure Cognitive Search
├── feature/langchain-retrieval  ← document ingestion & retrieval
├── feature/langchain-chatbot    ← conversational memory & prompts
├── feature/langgraph-orchestrator ← multi-agent graph orchestration
├── feature/langgraph-agents     ← individual specialist agents
├── feature/azure-deployment     ← Azure Container Apps / App Service
└── feature/frontend             ← full React / Streamlit frontend
```

## Rules

1. **Never** commit LangChain, LangGraph, vector-DB, or Azure SDK code directly to `main`.
2. Each feature branch targets a single concern and is reviewed before merge.
3. Hotfixes go to `main` directly only if they affect the boilerplate foundation.
4. Feature branches should be rebased on the latest `main` before opening a PR.
