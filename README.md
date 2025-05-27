# HRAssistant-Claude-Titan-RAG

## 🧠 Project Overview

This is a fully functional HR Assistant chatbot that leverages Anthropic's Claude (Titan) model via AWS Bedrock, integrated with RAG (Retrieval-Augmented Generation) to provide contextual, real-time responses based on your organization's HR policies and documents.

## ⚙️ Tech Stack

- **LLM:** Claude Titan via AWS Bedrock  
- **RAG:** Embedding and retrieval using FAISS  
- **Backend:** Python  
- **Frontend:** Streamlit  
- **Vector Store:** FAISS with local embedding using Amazon Titan Embeddings  
- **Document Parsing:** LangChain  
- **Deployment:** Local or cloud-compatible  

## 💼 Key Use Cases

- Answer employee queries based on internal HR policies and FAQs  
- Speed up onboarding by offering instant guidance  
- Reduce HR team load by automating repetitive questions  
- Private and customizable assistant for any organization  

## 🎯 Takeaways

- Demonstrates how to build secure, enterprise-ready AI assistants using RAG + Foundation Models  
- Provides a blueprint for domain-specific GenAI applications (e.g., HR, legal, finance)  

## Logic Explanation

### 📄 PDF Document Loader

```python
from langchain_community.document_loaders import PyPDFLoader
```
