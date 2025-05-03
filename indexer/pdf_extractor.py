import fitz
import requests
from pathlib import Path

def download_pdf(pdf_url, save_path):
    r = requests.get(pdf_url)
    with open(save_path, 'wb') as f:
        f.write(r.content)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    # Example usage
    url = "http://arxiv.org/pdf/2505.00703v1"
    path = "./data/sample.pdf"
    download_pdf(url, path)
    text = extract_text_from_pdf(path)
    print(text[:1000])
