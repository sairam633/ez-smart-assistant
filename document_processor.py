from pdfminer.high_level import extract_text
from transformers import pipeline

def process_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text(uploaded_file)
    else:
        return uploaded_file.read().decode("utf-8")

def generate_summary(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text[:2000], max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]
