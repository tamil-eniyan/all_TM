
from fastapi import APIRouter
from models.SaveModel import PlanCollection,SaveModel
from config.database import plan_collection,user_collection
from bson import ObjectId
import pydantic 

plan_api_router=APIRouter()
#checking if user present and appending trip plan in history
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str
@plan_api_router.post("/save")
def createPlan(data: SaveModel):
    trip_data = data.save.dict()
    trip_id = plan_collection.insert_one(trip_data).inserted_id

    # Find the user in the user collection and add the trip ID to the saved key array
    user = user_collection.find_one({"user_id": data.uid})
    saved_trips = user.get("history", [])
    saved_trips.append(trip_id)
    user_collection.update_one({"user_id": data.uid}, {"$set": {"history": saved_trips}})

    # Return the trip ID
    return {"trip_id": str(trip_id)}