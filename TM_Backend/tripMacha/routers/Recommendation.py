import requests
from fastapi import APIRouter

recommendation__router=APIRouter()
# Configure CORS
'''origins = [
    "*",
    # Add more allowed origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
'''

@recommendation__router.get("/process_data")
def get_place_photos(location_name, type_of_place):
    api_key = "AIzaSyDMWSgHTmFD9UdPTYIvLkXww_eyRdI5ggA"
    api_url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={location_name} {type_of_place}&key={api_key}"

    response = requests.get(api_url)
    data = response.json()
    
    place_results = []
    
    if "results" in data:
        for place in data["results"]:
            place_name = place["name"]
            #place_id = place["place_id"]
            place_photos = place.get("photos", [])

            if place_photos and len(place_photos) > 0:
                photo_reference = place_photos[0].get("photo_reference", "")
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
                print(place_name)
                print(photo_url)
                place_results.append((place_name, photo_url))
    print(place_results)
    return place_results

@recommendation__router.get("/get_place_photos")
def handle_get_place_photos(type_of_place: str):
    print("working : ",type_of_place)
    location_name = "udupi"
    return get_place_photos(location_name, type_of_place)

'''def main():
    api_key = "AIzaSyDMWSgHTmFD9UdPTYIvLkXww_eyRdI5ggA"
    location_name = "Udupi"
    type_of_place = "history"
    get_place_photos(location_name, type_of_place, api_key)'''



