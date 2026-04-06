def summarize_text(text):
    sentences = text.split(".")
    return ".".join(sentences[:2])  # simple summary (first 2 sentences)