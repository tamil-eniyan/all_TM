from datetime import time
from typing import List
from pydantic import BaseModel, Field, validator
from bson import ObjectId

class PlaceCollection(BaseModel):#for place collection
    duration: int
    time: str
    location: str
    activity: str
    travel_time: str
    distance: int
    longitude:float
    latitude:float
    isopen:bool
    spend_time:str
    close_time:str
    currently_open:str
    open_time:str
    time_available:bool


class PlanCollection(BaseModel):
    current_location: str
    current_time: str
    day:str
    place_count:int
    trip_plan: List[PlaceCollection]


class SaveModel(BaseModel):
    uid: str
    save: PlanCollection
    class Config:
        arbitrary_types_allowed = True 
    """@validator('uid')
    def validate_uid(cls, uid):
        if not isinstance(uid, str):
            raise ValueError('uid must be a string')
        return uid"""

class UserData(BaseModel):
    uid: str
    saved: List[ObjectId]
    class Config:
        arbitrary_types_allowed = True

class UserCollection(BaseModel):
    user_id:str
    history: list=[]
    class Config:
        arbitrary_types_allowed = True 

class UnsaveModel(BaseModel):
    uid: str
    tripid: str
    class Config:
        arbitrary_types_allowed = True

class FeedbackCollection(BaseModel):
    name: str
    email:str
    subject:str
    messageContent:str


class Getmodel(BaseModel):
    place:str
    start_time:str
    end_time:str
    distance:str
