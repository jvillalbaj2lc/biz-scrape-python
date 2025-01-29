import requests
from typing import List, Dict, Optional
import json

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

class OpenStreetMapService:
    @staticmethod
    def search_businesses(
        business_type: str, latitude: Optional[float] = None, longitude: Optional[float] = None,
        city: Optional[str] = None, country: Optional[str] = None, radius: int = 5000,
        limit: int = 50
    ) -> List[Dict]:
        """
        Search businesses using OpenStreetMap's Nominatim API.
        """

        headers = {"User-Agent": "biz-scrape-python/1.0"}
        
        # Constructing the query string properly
        query_parts = [business_type]

        if city:
            query_parts.append(city)
        if country:
            query_parts.append(country)
        
        query_string = ", ".join(query_parts)

        params = {
            "q": query_string,  # The proper query format
            "format": "json",
            "limit": limit,
            "extratags": 1,
            "addressdetails": 1
        }

        # If we have latitude and longitude, prefer geolocation search
        if latitude and longitude:
            params["lat"] = latitude
            params["lon"] = longitude
            params["radius"] = radius  # OpenStreetMap uses meters

        response = requests.get(NOMINATIM_URL, params=params, headers=headers)

        results = response.json()
        # Debugging raw OpenStreetMap API response
        print(f"Raw OpenStreetMap API Response: {json.dumps(results, indent=4)}")

        if response.status_code != 200:
            print(f"Error: OpenStreetMap API returned status {response.status_code}")
            return []

        results = results

        # Debugging response
        if not results:
            print(f"⚠️ No results found for query: {query_string} with radius {radius}m")

        return results
