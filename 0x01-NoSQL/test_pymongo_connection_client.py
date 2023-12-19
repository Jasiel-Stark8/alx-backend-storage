from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://jason:220300@jason.hcm3lse.mongodb.net/?retryWrites=true&w=majority"

# Create client to server connection
client = MongoClient(uri)

# test ping to server
try:
    client.admin.command('ping')
    print('Pinged server succesfuly')
except Exception as e:
    print(f'Error: {e}')
