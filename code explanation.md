## Logic Explanation

#### 📄 PDF Document Loader

```python
from langchain_community.document_loaders import PyPDFLoader
```
Loads PDF documents using LangChain's community-supported PDF loader. Useful for ingesting HR policies, manuals, or any structured 
document content.

#### ✂️ Text Splitter

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
```
Splits large documents into smaller, overlapping chunks for efficient embedding and querying. Uses recursive logic to split at paragraph, 
newline, word, or character level.

#### 🔡 Embeddings via Amazon Bedrock
```python
from langchain_aws import BedrockEmbeddings
```

Interface to generate text embeddings using Amazon Bedrock. This example uses the Titan model to convert text into numerical vectors 
for semantic search and retrieval.

#### 📚 Vector Store – FAISS
```python
from langchain_community.vectorstores import FAISS
```

FAISS is a high-performance vector store used to store and efficiently search text embeddings based on similarity. Ideal for 
Retrieval-Augmented Generation (RAG) workflows.

#### 🧱 Index Creator Utility
```python
from langchain.indexes import VectorstoreIndexCreator
```

High-level helper from LangChain to create an index using document loader, embeddings, and vector store like FAISS.

#### 🤖 Large Language Model Interface via Bedrock
```python
from langchain_aws import BedrockLLM
```
Interface to interact with Claude or other Amazon Bedrock-supported large language models using LangChain.

#### Function: hr_index()

- Creates the vector index for HR policy document
- Loads the PDF file PavanTech_HR_Policy.pdf
- Splits the document into chunks of 100 characters, with a 10-character overlap, using recursive splitting at paragraph, newline, space, or character level
- Uses Amazon Titan via Bedrock to convert each text chunk into a vector (embedding) for semantic similarity search
- Creates an indexer object using the provided text splitter, embeddings, and FAISS as the vector store
- Returns the created vector index for querying

```python
def hr_index():
    data_load = PyPDFLoader('PavanTech_HR_Policy.pdf')
    data_split = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size=100,
        chunk_overlap=10)
    data_embeddings = BedrockEmbeddings(
        credentials_profile_name='default',
        model_id='amazon.titan-embed-text-v2:0')
    data_index = VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS)
    db_index = data_index.from_loaders([data_load])
return db_index
```

#### Function: hr_llm()

- Creates an instance of Claude LLM via Bedrock.
- Instantiates a Claude model (v2) from Anthropic with:
  - max_tokens_to_sample: maximum output length,
  - temperature: lower value = more deterministic output,
  - top_p: controls diversity of output (similar to top-k sampling).
- Returns the Claude LLM object.

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

#### Function: hr_rag_response(index, question)

- Performs the RAG query using the vector index and Claude.
- Gets an instance of the Claude LLM.
- Runs the question against the indexed document using RAG. It:
  - Finds the most relevant document chunks,
  - Sends them to the Claude LLM with the question,
- Returns the RAG-generated answer from Claude

```python
def hr_rag_response(index, question):
    rag_llm = hr_llm()
return hr_rag_query
```

##### In Summary
- hr_index() builds a searchable index of your HR policy.
- hr_llm() initializes the Claude model for answering questions.
- hr_rag_response() takes a question, searches relevant context, and generates an answer using Claude LLM.
