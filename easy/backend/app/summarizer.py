
from transformers import pipeline

_model = None

def get_model():
    global _model
    if _model is None:
        _model = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )
    return _model


def split_text(text: str, max_words: int = 400):
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks


def summarize_text(text: str) -> str:
    summarizer = get_model()
    text = text.strip()

    if len(text.split()) < 60:
        return "Text is too short to summarize. Please provide a longer paragraph."

    chunks = split_text(text)

    partial_summaries = []

    for chunk in chunks:
        result = summarizer(
            chunk,
            max_length=100,
            min_length=40,
            do_sample=False,
            truncation=True
        )
        partial_summaries.append(result[0]["summary_text"])

    combined_text = " ".join(partial_summaries)

    final_summary = summarizer(
        combined_text,
        max_length=1000,
        min_length=50,
        do_sample=False,
        truncation=True
    )

    return final_summary[0]["summary_text"]
