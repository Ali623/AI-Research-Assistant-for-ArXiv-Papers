# 🤖 AI Research Assistant for ArXiv Papers

A Retrieval-Augmented Generation (RAG) application that helps users query and explore AI/ML research papers from [arXiv.org](https://arxiv.org). It uses vector search and large language models to generate context-aware, citation-rich answers.

---

##  Features

-  Ask questions like:
  - *"What’s the contribution of the paper titled 'Attention is All You Need'?"*
  - *"Summarize key ideas in recent diffusion model papers."*
-  Multi-document summarization.
-  Citation-aware responses with paper titles.
-  Fetches latest AI/ML papers via ArXiv API.
-  Streamlit-based interactive frontend.
-  Uses sentence-transformers, FAISS, and OpenAI's GPT models.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Research-Assistant-for-ArXiv-Papers.git
cd AI-Research-Assistant-for-ArXiv-Papers
```

---


### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set OpenAI API Key

```bash
OPENAI_API_KEY=your-openai-api-key
```

### 5. Build Vector Index

```bash
python indexer/vector_indexer.py
```

### 6. Run the App

```bash
streamlit run app.py
```


## Tech Stack
- LLM: OpenAI (GPT-3.5 / GPT-4)

- Embeddings: sentence-transformers/all-MiniLM-L6-v2

- Vector DB: FAISS

- Paper Source: ArXiv API

- Frontend: Streamlit

## Acknowledgements
- arxiv.org for providing open-access research content.

- Hugging Face Transformers

- OpenAI

- Streamlit

## License
This project is MIT-licensed. Feel free to fork and extend!