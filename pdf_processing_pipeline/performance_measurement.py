

from multiprocessing import Pool
import time
import psutil

# Function to process multiple PDFs in parallel using multiprocessing
def process_multiple_pdfs_concurrently(pdf_texts):
    with Pool() as pool:
        results = pool.map(process_single_pdf, pdf_texts)  # Process PDFs concurrently
    return results

# Helper function to process a single PDF (for multiprocessing)
def process_single_pdf(pdf):
    filename, text = pdf
    summary = summarize_text(text)
    keywords = extract_keywords(text)
    return (filename, summary, keywords)

# Function to measure performance (time and memory usage)
def measure_performance(func, *args):
    start_time = time.time()
    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss

    # Call the function and measure performance
    result = func(*args)

    memory_after = process.memory_info().rss
    elapsed_time = time.time() - start_time
    memory_usage = (memory_after - memory_before) / 1024 ** 2

    print(f"Time taken: {elapsed_time:.2f} seconds, Memory used: {memory_usage:.2f} MB")
    return result
