# Anime Recommender LLMOps

A recommendation system powered by LangChain and RAG (Retrieval-Augmented Generation) capabilities for personalized anime suggestions.

## Features

- **LangChain Integration**: Leverages LangChain framework for LLM orchestration
- **RAG Implementation**: Retrieval-Augmented Generation for enhanced recommendations
- **Scalable Deployment**: Containerized architecture ready for Kubernetes

## Deployment

The system is designed to run on Minikube deployed on a Google Cloud Platform VM instance.

### Prerequisites

- GCP VM instance
- Minikube installed and configured
- Docker Engine

### Run Locally

```bash
# Clone the repository
git clone <repository-url>

# Setup environment
pip install -e .
```

## Architecture

- **Backend**: LangChain-based recommendation engine
- **Vector Store**: RAG-enabled document retrieval
- **Orchestration**: Kubernetes on Minikube
- **Infrastructure**: GCP VM instance