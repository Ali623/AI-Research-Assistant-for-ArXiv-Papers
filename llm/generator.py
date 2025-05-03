import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env")

# New client-based API usage
client = OpenAI(api_key=api_key)

def generate_answer(query, docs):
    context = "\n\n".join(
        [f"Title: {doc['title']}\nSnippet: {doc.get('chunk', '')}" for doc in docs]
    )

    prompt = f"""You are an AI assistant for AI/ML researchers. Use the following paper snippets to answer the question.
Answer concisely and cite papers using their titles.

Context:
{context}

Question: {query}
Answer:"""

    response = client.chat.completions.create(
        model="gpt-4-turbo",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content
