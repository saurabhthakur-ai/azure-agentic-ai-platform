# Branching Strategy

## Overview

`main` is the stable, framework-neutral boilerplate branch.  
All feature development happens in dedicated branches and is merged via pull requests.

## Branch Map

```
main                          ← stable boilerplate (this branch)
├── feature/project-foundation
├── feature/langchain-rag
├── feature/langchain-retrieval
├── feature/langchain-chatbot
├── feature/langgraph-orchestrator
├── feature/langgraph-agents
├── feature/azure-deployment
└── feature/frontend
```

## Rules

1. `main` must always pass CI.
2. No LangChain, LangGraph, vector-database, or Azure resource provisioning code in `main`.
3. Feature branches are short-lived and merged via PR.
4. Commit messages follow Conventional Commits (`feat:`, `fix:`, `chore:`, etc.).
