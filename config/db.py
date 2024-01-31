import pymongo
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://<username>:<password>@firstproject.wami2av.mongodb.net/?retryWrites=true&w=majority"

try:
    # Attempt to establish a connection to the MongoDB database
    conn: MongoClient = pymongo.MongoClient(MONGO_URI)

    # Access a specific database (replace 'your_database' with your actual database name)
    db = conn.notes

    # Now you can perform operations on the database

except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")