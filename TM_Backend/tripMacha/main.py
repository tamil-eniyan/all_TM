from fastapi import FastAPI
#from fetch_recom import user_rout
from  routers.postUser import user_api_router 
from  routers.postPlan import plan_api_router 
from  routers.getPlan import fetch_api_router 
from routers.removePlan import remove_plan_router
from routers.postFeedback import feedback_api_router
from routers.Travel import travel_api_router
import firebase_admin
from firebase_admin import auth,credentials
from routers.firebase import firebase_api_router
from routers.Recommendation import recommendation__router
from fastapi.middleware.cors import CORSMiddleware
#from fetch_saved import fetch_rout
button_pressed=False

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(r"tripappfb-firebase-adminsdk-fn7u9-895d8ad959.json")
firebase_admin.initialize_app(cred)
app = FastAPI()

app.add_middleware(
  CORSMiddleware,allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
)
#
# app.include_router(user_rout)
app.include_router(user_api_router)
app.include_router(fetch_api_router)
#if button_pressed==True:

app.include_router(plan_api_router)
app.include_router(travel_api_router)
app.include_router(remove_plan_router)
app.include_router(feedback_api_router)
app.include_router(firebase_api_router)
app.include_router(recommendation__router)
