import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY") # add your specific key from the openAI

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
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message["content"]
