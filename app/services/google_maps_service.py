import requests
import os
from typing import List, Dict, Optional

GOOGLE_PLACES_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
GOOGLE_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Store API Key in .env file

class GoogleMapsService:
    @staticmethod
    def search_businesses(
        business_type: str, latitude: float, longitude: float, radius: int = 5000, limit: int = 50
    ) -> List[Dict]:
        """
        Search businesses using Google Places API.
        """
        params = {
            "location": f"{latitude},{longitude}",
            "radius": radius,
            "type": business_type.lower(),
            "key": GOOGLE_API_KEY
        }

        response = requests.get(GOOGLE_PLACES_URL, params=params)
        if response.status_code != 200:
            print(f"Error: Google Places API returned status {response.status_code}")
            return []

        results = response.json().get("results", [])
        return results[:limit]  # Limit results

    @staticmethod
    def get_business_details(place_id: str) -> Dict:
        """
        Get additional details about a business.
        """
        params = {
            "place_id": place_id,
            "fields": "name,formatted_address,geometry,formatted_phone_number,website",
            "key": GOOGLE_API_KEY
        }

        response = requests.get(GOOGLE_DETAILS_URL, params=params)
        if response.status_code != 200:
            print(f"Error: Google Places Details API returned status {response.status_code}")
            return {}

        return response.json().get("result", {})
