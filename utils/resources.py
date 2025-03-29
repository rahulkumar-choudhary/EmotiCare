import requests
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_nearby_resources(disorder, location):
    query = f"{disorder} therapist"
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json"

    params = {
        "query": query,
        "location": location,
        "radius": 5000,
        "type": "health",
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(url, params=params)
    results = response.json().get("results", [])[:5]

    formatted = []
    for r in results:
        formatted.append({
            "name": r.get("name"),
            "address": r.get("formatted_address"),
            "rating": r.get("rating", "N/A"),
            "type": disorder,
        })

    return formatted

def book_appointment(resource, user_info):
    print(f"Booking appointment at {resource['name']} for {user_info}")
    return True