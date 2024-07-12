from fastapi import FastAPI,APIRouter, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from config.database import feedback_collection
from models.SaveModel import FeedbackCollection
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
import pydantic
import smtplib
import ssl
from email.message import EmailMessage

SENDER_EMAIL = "tripmachagt@gmail.com"
PASS = 'hloa atjv ijnu byvw'
RECEIVER_EMAIL = "gangliatechnologies@gmail.com"

feedback_api_router=APIRouter()

# Create a custom encoder for ObjectId serialization
def encode_object_id(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
# Add the custom encoder to pydantic's ENCODERS_BY_TYPE dictionary
pydantic.json.ENCODERS_BY_TYPE[ObjectId] = encode_object_id

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(feedback_api_router)

# Uncomment to enable feedbacks saving to mongoDB but will work if getforms is removed from the ConstactUs.jsx
@feedback_api_router.post("/feedback")
def createFeedback(feedback: FeedbackCollection, background_tasks: BackgroundTasks):
    data = feedback
    new_feedback = {
        "name" : data.name,
        "email" : data.email,
        "subject" : data.subject,
        "messageContent" : data.messageContent
    }

    message = f"Name : {new_feedback['name']} ({new_feedback['email']}) \n Subject: {new_feedback['subject']} \n Message: {new_feedback['messageContent']}"
    
    def send_mail(host = "smtp.gmail.com", port = 587, subject = new_feedback['subject'], msg = message, sender = SENDER_EMAIL, recipients = RECEIVER_EMAIL):
        try:
            em = EmailMessage()
            em['From'] = SENDER_EMAIL
            em['To'] = RECEIVER_EMAIL
            em['Subject'] = subject
            em.set_content(msg)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
                smtp.login(SENDER_EMAIL, PASS)
                smtp.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, em.as_string())
        except:
            print("Couln't email")

    
    background_tasks.add_task(send_mail)

    ins_feedback = feedback_collection.insert_one(new_feedback).inserted_id
    return {"message": "inserted feedback", "feedback_id": str(ins_feedback)}  # Convert the ObjectId to str before returning

 
