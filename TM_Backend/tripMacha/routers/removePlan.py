from fastapi import APIRouter
from config.database import user_collection,plan_collection
from models.SaveModel import UnsaveModel
from bson.objectid import ObjectId

remove_plan_router = APIRouter()

@remove_plan_router.post("/unsave")
def unsaveTrip(data: UnsaveModel):
    u = removeFromUser(data.uid, data.tripid)
    t = removeFromTrip(data.tripid)
    if u == 1 and t == 1:
        return {"message": "recordDeleted"}
    else:
        return {"message": "notFound"}

       


def removeFromTrip(trip_id):
    # Convert the provided trip_id to ObjectId
    trip_object_id = ObjectId(trip_id)

    # Delete the document with the matching ObjectId from the trip collection
    result = plan_collection.delete_one({"_id": trip_object_id})

    # Check if the deletion was successful
    if result.deleted_count == 1:
        return 1
    else:
        return 0


def removeFromUser(uid, trip_id):
    trip_object_id = ObjectId(trip_id)
    result = user_collection.update_one(
        {"user_id": uid},
        {"$pull": {"history": trip_object_id}}
    )
    if result.modified_count == 1:
        return 1
    else:
        return 0