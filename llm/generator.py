import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Please add it to your .env file.")

openai.api_key = api_key

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

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or "gpt-4-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message["content"]
