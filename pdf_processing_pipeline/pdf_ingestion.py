

import os
from PyPDF2 import PdfReader

# Function to read PDF file and extract text .I have not set the file location as it may vary
def read_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()  # Add text from each page to 'text'
        return text
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# Function to process multiple PDFs in a folder
def ingest_pdfs(folder_path):
    pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]
    pdf_texts = []
    
    for pdf_path in pdf_files:
        text = read_pdf(pdf_path)  # Extract text from each PDF
        if text:
            pdf_texts.append((os.path.basename(pdf_path), text))  # Store (filename, text)
    
    return pdf_texts
