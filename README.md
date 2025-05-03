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


## 📋 Example Queries for AI Research Assistant

Use the following example prompts to test your RAG-powered research assistant on AI/ML papers from arXiv:

1. **What are the key contributions of the paper titled _"On the Importance of Gaussianizing Representations"_?**

2. **Summarize the recent advances in diffusion models from the latest arXiv papers.**

3. **Compare the methods used in _"T2I-R1"_ and _"DALL·E"_ for text-to-image generation.**

4. **What datasets were used in the paper _"Deep Reinforcement Learning for Urban Air Quality Management"_?**

5. **Which papers focus on multi-modal learning techniques?**

6. **Give a brief overview of transformers in computer vision based on recent arXiv submissions.**

7. **List key limitations discussed in papers about reinforcement learning for real-world environments.**

8. **What is the role of collaborative token-level reasoning in recent text-to-image research?**

9. **Summarize contributions of top papers in generative AI from the past month.**

10. **Explain the optimization techniques used in papers related to air quality modeling.**


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
