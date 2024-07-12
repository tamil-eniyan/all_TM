from pymongo import MongoClient

uri = "mongodb://localhost:27017/"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client["travels"]
feedback_db = client["Feedbacks"]
user_collection=db["user"]
plan_collection=db["trip"]
feedback_collection = feedback_db["UserFeedbacks"]