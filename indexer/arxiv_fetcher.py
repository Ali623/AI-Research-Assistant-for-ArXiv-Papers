import arxiv
import os
import json

def fetch_papers(query="artificial intelligence", max_results=10):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    client = arxiv.Client()
    papers = []
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "pdf_url": result.pdf_url,
            "id": result.get_short_id(),
            "authors": [a.name for a in result.authors],
        })
    return papers

if __name__ == "__main__":
    papers = fetch_papers("machine learning", max_results=10)
    os.makedirs("./data", exist_ok=True)
    with open("./data/papers.json", "w") as f:
        json.dump(papers, f, indent=2)
    print("Fetched and saved metadata for", len(papers), "papers.")
