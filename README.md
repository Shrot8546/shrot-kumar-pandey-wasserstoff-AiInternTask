
# PDF Processing Pipeline

### A domain-specific PDF summarization and keyword extraction pipeline

This project is designed to process multiple PDF documents, extract key content, generate summaries, and store results (summary and keywords) in a MongoDB database. The pipeline is built with concurrency in mind to efficiently handle large batches of PDFs.

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [MongoDB Setup](#mongodb-setup)
6. [Performance](#performance)
7. [Notes](#notes)
8. [Contributing](#contributing)

---

## Features

- **PDF Ingestion and Parsing**: Reads and extracts text from multiple PDF documents in a given folder.
- **Summarization**: Dynamically generates summaries of the PDF content based on document length.
- **Keyword Extraction**: Extracts domain-specific, non-generic keywords using NLP.
- **MongoDB Integration**: Stores extracted summaries and keywords in a MongoDB database for easy retrieval.
- **Concurrency**: Processes multiple PDFs in parallel using Python's `multiprocessing` to enhance performance.
- **Performance Measurement**: Measures and logs the time taken and memory used during processing.

---

## Project Structure

```
pdf_processing_pipeline/
│
├── pdf_ingestion.py           # Reads PDFs and extracts text
├── pdf_processing.py          # Generates summaries and extracts keywords
├── mongodb_storage.py         # Stores results in MongoDB
├── performance_measurement.py # Handles concurrency and performance measurement
└── main.py                    # Main script that runs the entire pipeline
└── README.md                  # Project documentation
```

---

## Installation

### Prerequisites
1. **Python 3.x**
2. **MongoDB** (Make sure MongoDB is running locally or remotely)

### Step 1: Clone the repository
```bash
git clone <repository-url>
cd pdf_processing_pipeline
```

### Step 2: Install Python dependencies
Ensure you have the required Python libraries by running:
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file, you can manually install the dependencies:
```bash
pip install PyPDF2 pymongo spacy psutil
```

Then, download the required **spaCy** language model:
```bash
python -m spacy download en_core_web_sm
```

---

## Usage

### Step 1: Place Your PDFs
Place the PDF files you want to process in a folder. Note the folder path for the next step.

### Step 2: Edit the `main.py` File
In the `main.py` file, update the folder path to point to the directory where your PDFs are stored:
```python
folder_path = '/path/to/your/pdf/folder'  # Replace this with your folder path
```

### Step 3: Run the Pipeline
From the terminal, run the `main.py` script:
```bash
python main.py
```

### Step 4: Check MongoDB for Results
Once the script finishes processing, open MongoDB and check the `pdf_database` and `pdf_collection` to view the stored summaries and keywords for each processed PDF.

---

## MongoDB Setup

The pipeline uses **MongoDB** to store the results (summary and keywords). To set up MongoDB:

1. **Install MongoDB** (if you don’t have it yet):
   - [Download MongoDB](https://www.mongodb.com/try/download/community) and follow the installation instructions for your operating system.

2. **Start MongoDB**:
   ```bash
   mongod
   ```

3. **Check MongoDB Data**:
   After running the script, open the MongoDB shell:
   ```bash
   mongo
   ```
   Check your database:
   ```bash
   use pdf_database
   db.pdf_collection.find().pretty()
   ```


---

## Performance

The pipeline is designed to process multiple PDFs concurrently using Python’s `multiprocessing` module. It also tracks the performance in terms of **time taken** and **memory used**.

The `performance_measurement.py` file includes functions that:
- **Measure the time** it takes to process all PDFs.
- **Log memory usage** during the pipeline execution.

---

## Notes

- **Document Lengths**: The summary length is dynamically adjusted based on the length of the PDF:
  - **Long PDFs** (more than 30 sentences) get a longer summary.
  - **Medium PDFs** (10–30 sentences) get a medium-length summary.
  - **Short PDFs** (fewer than 10 sentences) get a brief summary.
  
- **Keyword Extraction**: The extracted keywords are top 10 non-generic words, relevant to the document's content.

---

## Contributing

Feel free to submit issues or pull requests if you would like to improve or extend the pipeline. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---
