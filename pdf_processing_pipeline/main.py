

from pdf_ingestion import ingest_pdfs
from pdf_processing import process_pdfs
from mongodb_storage import store_in_mongodb
from performance_measurement import measure_performance, process_multiple_pdfs_concurrently

if __name__ == "__main__":
    folder_path = '/path/to/your/pdf/folder'  # Replace with your actual folder path
    
    # Step 1: Ingest PDFs (read and extract text)
    pdf_texts = ingest_pdfs(folder_path)
    
    # Step 2: Process PDFs (summarize and extract keywords)
    results = process_multiple_pdfs_concurrently(pdf_texts)
    
    # Step 3: Store results in MongoDB
    store_in_mongodb(results)
    
    # Measure performance for the entire pipeline
    measure_performance(process_multiple_pdfs_concurrently, pdf_texts)
