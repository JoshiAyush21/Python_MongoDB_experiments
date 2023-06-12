from pymongo.mongo_client import MongoClient
# Replace the placeholder with your connection string
uri = "mongodb://localhost:27017"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)