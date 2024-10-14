

import spacy

# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')

# Function to summarize text based on document length
def summarize_text(text):
    sentences = text.split('.')
    if len(sentences) > 30:  # Long document
        return '.'.join(sentences[:10])  # Longer summary
    elif len(sentences) > 10:  # Medium document
        return '.'.join(sentences[:5])  # Medium summary
    else:  # Short document
        return '.'.join(sentences[:2])  # Brief summary

# Function to extract top keywords using spaCy NLP
def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return keywords[:10]  # Return top 10 keywords

# Function to generate summary and keywords for all PDFs
def process_pdfs(pdf_texts):
    results = []
    
    for filename, text in pdf_texts:
        summary = summarize_text(text)  # Summarize the PDF content
        keywords = extract_keywords(text)  # Extract keywords from the content
        results.append((filename, summary, keywords))
    
    return results
