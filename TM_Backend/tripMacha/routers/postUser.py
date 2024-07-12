from fastapi import APIRouter
from models.SaveModel import UserCollection
from config.database import user_collection
from bson import ObjectId
import pydantic
#rom schema.user_schema import plans_serializer
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str
user_api_router=APIRouter()
@user_api_router.post("/user_collection") 
def createUserCollection(user: UserCollection):
    data = user.dict()
    print('-------------',data)
    find_user=user_collection.find_one({"user_id":user.user_id})
    if find_user is not None:
        print("user already present")
        return "user already present"
    ins_user_id=user_collection.insert_one(data).inserted_id
    return {"message":"inserted succussefully","user_id":ins_user_id}





""" @save_rout.post("/save")
def process_data(data: SaveModel):
    trip_data = data.save.dict()
    trip_id = savecol.insert_one(trip_data).inserted_id

    # Find the user in the user collection and add the trip ID to the saved key array
    user = ucol.find_one({"uid": data.uid})
    saved_trips = user.get("saved", [])
    saved_trips.append(trip_id)
    ucol.update_one({"uid": data.uid}, {"$set": {"saved": saved_trips}})

    # Return the trip ID
    return {"trip_id": str(trip_id)}
 """
