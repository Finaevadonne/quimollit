import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Assuming MongoDB is running on localhost
db = client['mydatabase']  # Replace 'mydatabase' with your database name

# Create or access a collection
collection = db['mycollection']  # Replace 'mycollection' with your collection name

# Dummy data to insert
dummy_data = [
    {"name": "John Doe", "age": 30, "city": "New York"},
    {"name": "Jane Smith", "age": 25, "city": "San Francisco"},
    {"name": "Mike Johnson", "age": 35, "city": "Chicago"}
]

# Insert dummy data into the collection
result = collection.insert_many(dummy_data)

# Print the IDs of the inserted documents
print("Inserted IDs:", result.inserted_ids)

# Close the MongoDB connection
client.close()
