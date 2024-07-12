from fastapi import APIRouter
from config.database import plan_collection,user_collection
from models.SaveModel import PlanCollection


fetch_api_router=APIRouter()

@fetch_api_router.get("/user/{uid}")
def getUserPlan(uid: str):
    # Find the user document based on the provided UID
    user = user_collection.find_one({"user_id": uid})
    if not user:
        return {"message": "User not found"}

    # Retrieve the saved trip IDs from the user document
    saved_trip_ids = user.get("history", [])

    # Use the saved trip IDs to fetch the corresponding trip records
    saved_trips = plan_collection.find({"_id": {"$in": saved_trip_ids}})

    # Convert MongoDB documents to Pydantic models
    saved_trip_models = [PlanCollection(**trip) for trip in saved_trips]

    # Return the saved trip records
    return {"saved_trips": saved_trip_models}
    
    


