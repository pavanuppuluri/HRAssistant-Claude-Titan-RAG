# Text Embedding

Text embedding is a way to convert words, sentences, or entire documents into numerical vectors (lists of numbers) that capture their meaning and semantic relationships.

## Why Do We Need Embeddings?

Computers don't understand text like humans do. They need text to be in a numeric form for tasks like:

- **Search**
- **Similarity comparison**
- **Clustering**
- **Machine learning**
- **Retrieval-Augmented Generation (RAG)**

## What Does a Text Embedding Represent?

An embedding is a dense vector (like `[0.32, -0.15, 0.78, ...]`) that encodes the semantic meaning of the text. This means:

- **Similar texts → similar vectors**
- **Unrelated texts → far apart vectors**

### Example

| Text   | Vector            | Notes                    |
|--------|-------------------|--------------------------|
| "Cat"  | [0.11, 0.87, ...] | Close to "Dog"           |
| "Dog"  | [0.10, 0.88, ...] | Similar to "Cat"         |
| "Pizza"| [0.91, -0.42, ...]| Far from "Cat" and "Dog" |

## How Are Embeddings Used in Your Code?

### Need of Amazon Titan in our code:

- We are using Amazon Titan to generate embeddings.
- These embeddings are stored in FAISS, so you can search and retrieve similar text chunks when a user asks a question.
  
```python
data_embeddings = BedrockEmbeddings(
    credentials_profile_name='default',
    model_id='amazon.titan-embed-text-v2:0')
```

### Need of Claude in our code: 

- Claude (via the BedrockLLM class using anthropic.claude-v2) is playing the role of a reasoning engine or answer generator. 
- Here’s what it’s doing step by step:

```python
def hr_llm():
    llm = BedrockLLM(
        credentials_profile_name='default',
        model_id='anthropic.claude-v2',
        model_kwargs={
            "max_tokens_to_sample": 3000,
            "temperature": 0.1,
            "top_p": 0.9})
return llm
```

This function prepares the Claude LLM (Large Language Model) from Anthropic, accessed via Amazon Bedrock.
And then it’s used here:

```python
def hr_rag_response(index, question):
    rag_llm = hr_llm()
    hr_rag_query = index.query(question=question, llm=rag_llm)
return hr_rag_query
```

### What Claude Does

#### 1. Receives Context (Text Chunks) + Question

The system retrieves relevant parts of the **HR policy PDF** using **vector search** (powered by **FAISS + embeddings**).

These chunks (context) + the user's question are sent to **Claude**.

#### 2. Generates a Natural Language Answer

Claude uses its language understanding to read the context and answer the question as if it had "read" the document.

#### 3. Returns the Answer

The final response is a **natural-language reply** to the question, based on the retrieved context.

## Example

Let’s say your question is:

> **"What is the company’s leave policy?"**

### The RAG Process:

1. **Finds relevant PDF chunks** like:  
   *"Employees are entitled to 20 days of paid leave annually..."*

2. **Sends those to Claude** along with your question.

3. **Claude replies** with something like:  
   *"According to the HR policy, employees are entitled to 20 days of paid leave per year."*








