

from pymongo import MongoClient

# MongoDB setup - connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['pdf_database']
collection = db['pdf_collection']

# Function to store summaries and keywords in MongoDB
def store_in_mongodb(results):
    for filename, summary, keywords in results:
        try:
            data = {
                'filename': filename,
                'summary': summary,
                'keywords': keywords
            }
            collection.insert_one(data)  # Insert document into MongoDB
            print(f"Data stored for {filename}")
        except Exception as e:
            print(f"Error storing {filename} in MongoDB: {e}")
