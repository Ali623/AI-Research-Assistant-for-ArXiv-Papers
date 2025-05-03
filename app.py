import streamlit as st
from retriever.query_engine import RAGRetriever
from llm.generator import generate_answer

st.set_page_config(page_title="AI Research Assistant", layout="wide")
st.title("AI Research Assistant for arXiv Papers")

query = st.text_input("Ask a research question (e.g., What is the main contribution of Transformer models?)")

if query:
    with st.spinner("Retrieving relevant papers..."):
        retriever = RAGRetriever()
        results = retriever.search(query)

        for r in results:
            st.markdown(f"**{r['title']}**  \nAuthors: {', '.join(r.get('authors', []))}  \n")

        with st.spinner("Generating answer using LLM..."):
            answer = generate_answer(query, results)

        st.markdown("---")
        st.subheader("Answer")
        st.write(answer)
