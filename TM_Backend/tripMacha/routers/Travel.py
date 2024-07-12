#from models.Getmodel import Getmodel
from fastapi import APIRouter
from models.SaveModel import Getmodel
import openai
import googlemaps
import json
from pprint import pprint
import datetime
import requests
import google.generativeai as genai
import json


travel_api_router=APIRouter()

openai.api_key = "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"
api_key_maps = "AIzaSyDMWSgHTmFD9UdPTYIvLkXww_eyRdI5ggA"
api_key = "AIzaSyDMWSgHTmFD9UdPTYIvLkXww_eyRdI5ggA"
GEMINI_API = "AIzaSyDcdRlJrMJRmLKgDHV92MUfdj-oRLRQY-U"
gmaps = googlemaps.Client(key=api_key_maps)

def textify(text):
    n=1
    text = text.split("```")[n]
    text = text.replace("\\n","")
    text = text.replace("json","")
    text = text.replace("\\","")
    text = text.lower()
    n=n+1
    return text


generation_config = {
    "temperature": 0,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 400,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]


def get_gemini_response(place, start_time, end_time, distance):
    genai.configure(api_key=GEMINI_API)
    model = genai.GenerativeModel('gemini-pro')

    template = f"""i am in {place} and I am free from {start_time} to {end_time}. 
    Please create an itinerary within a {distance} travel radius not more than it, 
    with accurate place name ,activities and travel details and by considering 
    breakfast,lunch,dinner with appropriate restaurant names if needed according to 
    the time, considering the buffer time of 20min.Prioritize locations based on the 
    shortest distance first. I want the itinerary to only travel on the road by car, 
    no airways, no train included. Provide the output in JSON format with fields: Time, 
    Location, Activity, Travel Time, Spend Time and Distance (in the specified order only).
    Give me only the itinerary, no other explanation or suggestion or sorry message or
    any alternatives. """

    text = model.generate_content(template).text
    print('-=-='*50)
    print(text)
    try:
        text = text.split("```")[1]
        text = text.replace("\\n","")
        print(text[:20])
        text = text.replace("json","")
        text = text.replace("JSON","")
        text = text.replace("Json","")
        text = text.replace("\\","")
        text = text.lower()
        print("gemini"*7)
        print(text)
        #n=n+1
        return text
    except:
        return None





# def get_chatgpt_response(place, start_time, end_time, distance):
#     messages = [{"role": "system", "content": "You are an intelligent assistant."}]
#     template = f"i am in {place} and I am free from {start_time} to {end_time}. Please create an itinerary within a {distance} travel radius not more than it, with accurate place name ,activities and travel details and by considering breakfast,lunch,dinner with appropriate restaurant names if needed according to the time, considering the buffer time of 20min.Prioritize locations based on the shortest distance first. I want the itinerary to only travel on the road by car, no airways, no train included. Provide the output in JSON format with fields: Time, Location, Activity, Travel Time, Spend Time and Distance (in the specified order only).Give me only the itinerary, no other explanation or suggestion or sorry message or any alternatives. "
#     if template:
#         messages.append(
#             {"role": "user", "content": template},
#         )
#         chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, n=3)

#     reply = chat.choices[0].message.content
#     print(reply)
#     output = reply.split("```")[0]
#     output = output.replace("\\n", "", 100)
#     output = output.replace("json", "")
#     output = output.replace("\\", "")
#     output = output.lower()

#     return output


def get_coordinates_from_place_id(api_key, place_id):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?place_id={place_id}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK":
        result = data["results"][0]
        latitude = result["geometry"]["location"]["lat"]
        longitude = result["geometry"]["location"]["lng"]
        return latitude, longitude
    else:
        return None


def is_place_open(place_id, api_key):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=opening_hours&key={api_key}"
    response = requests.get(url)
    data = response.json()

    current_datetime = datetime.datetime.now()
    current_day = current_datetime.weekday()
    current_time = current_datetime.strftime("%H:%M")

    time_available = False
    currently_open = False
    currently_closed = False
    time_open = "NA"
    time_close = "NA"

    # checking if opening hours data is available
    if data["result"] == {}:
        return {
            "time_available": time_available,
            "currently_open": currently_open,
            "currently_closed": currently_closed,
            "open_time": time_open,
            "close_time": time_close,
        }
    else:                                                                 
        # opeimg hours data is available so loop through each day in to find current days open and close timings
        for period in data["result"]["opening_hours"]["periods"]:
            day = period["open"]["day"]
            open_time = period["open"]["time"]
            time_available = True

            # if close time not available handle the exception
            try:
                closse_time = period["close"]["time"]
            except:
                time_available = False

            # if closing time is available, the only we check for current days timings of a place
            if time_available is True:
                if day == current_day:
                    if open_time <= current_time <= closse_time:
                        currently_open = True
                    else:
                        currently_closed = True
                    time_close = closse_time
                    time_open = open_time
        return {
            "time_available": time_available,
            "currently_open": currently_open,
            "currently_closed": currently_closed,
            "open_time": time_open,
            "close_time": time_close,
        }


def without_itinerary(json_res):
    pass


def with_itinerary(json_res):
    places_output = []
    for place in json_res["itinerary"]:
        place_name = place["location"]

        # send request to GoogleMap API to find place using place name
        place_result = gmaps.find_place(
            input=place_name,
            input_type="textquery",
        )
        # after finding place, we extract placeID
        if place_result["status"] == "OK" and len(place_result["candidates"]) > 0:
            place_id = place_result["candidates"][0]["place_id"]

        # now we extract coordinates, based on placeID extracted above
        coordinates = get_coordinates_from_place_id(api_key, place_id)

        # if coordinates exists, store them in place object
        if coordinates:
            latitude, longitude = coordinates
            place["latitiude"] = latitude
            place["longitude"] = longitude
        else:
            place["latitiude"] = None
            place["longitude"] = None

        # print(place["location"])
        place_timing = is_place_open(place_id, api_key)
        place["timing"] = place_timing
        places_output.append(place)
    return places_output


def get_itinerary_plan(place, start_time, end_time, distance):
    output = get_gemini_response(
        place=place, start_time=start_time, end_time=end_time, distance=distance
    )

    if output.find("itinerary") == -1:
        get_itinerary_plan(
            place=place, start_time=start_time, end_time=end_time, distance=distance
        )
        # response = without_itinerary(json_out)
    else:
        try:
            print('8'*80)
            pprint(output)
            json_out = json.loads(output)
            response = with_itinerary(json_out)

            json_data_str = json.dumps(response)
            x = json_data_str.replace("[", '{"plan":[', 1)
            x = x.replace("]", "]}", 1)

            json_output = json.loads(x)
            pprint(json_output)
            return json_output
        except Exception as e:
            error = {"message at get_itinerary_plan": e}
            print(error)
            return error




@travel_api_router.post("/mltravel")
async def getdetails(obj: Getmodel):
    # Call the mltravel function to get the JSON data

    data = get_itinerary_plan(obj.place,obj.start_time,obj.end_time,obj.distance)
    print(data)
    
    
    # for i,v in plan_dict.items():
    #     print(i, v)
    #     print("\n")
 # Calculate the count of the plan
    try:
        plan_count = len(data['plan'])

    except Exception as e:
        print({"Error at travel.py1" : e})
        data = None
        data = get_itinerary_plan(obj.place,obj.start_time,obj.end_time,obj.distance)
        print(data)
        try:
            plan_count = len(data['plan'])
        except Exception as e:
            print({"Error at travel.py2" : e})
            data = None
            data = get_itinerary_plan(obj.place,obj.start_time,obj.end_time,obj.distance)
            print(data)
            try:            
                plan_count = len(data['plan'])        
            except Exception as e:
                print({"Error at travel.py1" : e})
                data = None
                data = get_itinerary_plan(obj.place,obj.start_time,obj.end_time,obj.distance)
                print(data) 
                try:            
                    plan_count = len(data['plan'])        
                except Exception as e:
                    print({"Error at travel.py1" : e})
                    data = None
                    data = get_itinerary_plan(obj.place,obj.start_time,obj.end_time,obj.distance)
                    print(data) 
                    plan_count = len(data['plan'])    
                
    # Append the plan count to the JSON data
    data['plan_count'] = plan_count


    # # Convert the data back to JSON string
    json_data = json.dumps(data)

    pprint(json_data)

    # Return the JSON response
    return json_data
    


