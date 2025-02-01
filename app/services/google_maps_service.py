import requests
import os
from typing import List, Dict
from time import sleep
import json
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from app.core.constants import (
    GOOGLE_PLACES_URL,
    GOOGLE_DETAILS_URL,
    GOOGLE_PLACE_TYPES,
    GOOGLE_PLACES_FIELDS,
    GOOGLE_API_STATUS_OK,
    GOOGLE_API_STATUS_ZERO_RESULTS,
    GOOGLE_API_KEY_ENV,
    GOOGLE_CREDENTIALS_FILE_ENV,
    GOOGLE_AUTH_SCOPES
)

class GoogleMapsServiceError(Exception):
    """Custom exception for Google Maps API errors"""
    pass

class GoogleMapsService:
    def __init__(self):
        """Initialize the service with appropriate authentication"""
        self.session = self._get_authenticated_session()

    def _get_authenticated_session(self) -> requests.Session:
        """
        Get an authenticated session using either API key or service account.
        Prioritizes service account authentication over API key.
        """
        # Try service account authentication first
        credentials_path = os.getenv(GOOGLE_CREDENTIALS_FILE_ENV)
        if credentials_path and os.path.exists(credentials_path):
            try:
                credentials = service_account.Credentials.from_service_account_file(
                    credentials_path,
                    scopes=GOOGLE_AUTH_SCOPES
                )
                return AuthorizedSession(credentials)
            except Exception as e:
                print(f"Warning: Failed to load service account credentials: {e}")

        # Fall back to API key authentication
        api_key = os.getenv(GOOGLE_API_KEY_ENV)
        if not api_key:
            raise GoogleMapsServiceError(
                f"Neither service account credentials nor API key found. "
                f"Please set either {GOOGLE_CREDENTIALS_FILE_ENV} or {GOOGLE_API_KEY_ENV}"
            )

        session = requests.Session()
        session.params = {'key': api_key}
        return session

    def search_businesses(
        self, business_type: str, latitude: float, longitude: float, 
        radius: int = 5000, limit: int = 50
    ) -> List[Dict]:
        """
        Search businesses using Google Places API.
        """
        params = {
            "location": f"{latitude},{longitude}",
            "radius": radius,
            "keyword": business_type,  # Use 'keyword' instead of 'type' for better results
            "key": os.getenv(GOOGLE_API_KEY_ENV)
        }

        try:
            response = requests.get(GOOGLE_PLACES_URL, params=params)
            response.raise_for_status()
            data = response.json()

            if data.get("status") not in {GOOGLE_API_STATUS_OK, GOOGLE_API_STATUS_ZERO_RESULTS}:
                raise GoogleMapsServiceError(
                    f"Google API Error: {data.get('status')} - {data.get('error_message', 'Unknown error')}"
                )

            results = data.get("results", [])

            # Handle pagination if needed and respect rate limits
            next_page_token = data.get("next_page_token")
            while next_page_token and len(results) < limit:
                sleep(2)  # Wait before requesting next page
                params["pagetoken"] = next_page_token
                response = requests.get(GOOGLE_PLACES_URL, params=params)
                response.raise_for_status()
                data = response.json()
                results.extend(data.get("results", []))
                next_page_token = data.get("next_page_token")

            return results[:limit]

        except requests.exceptions.RequestException as e:
            raise GoogleMapsServiceError(f"Request failed: {str(e)}")


    def get_business_details(self, place_id: str) -> Dict:
        """
        Get additional details about a business.
        """
        params = {
            "place_id": place_id,
            "fields": ",".join(GOOGLE_PLACES_FIELDS),
            "key": os.getenv(GOOGLE_API_KEY_ENV)
        }

        try:
            response = self.session.get(GOOGLE_DETAILS_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data.get("status") != GOOGLE_API_STATUS_OK:
                raise GoogleMapsServiceError(f"Google API Error: {data.get('status')} - {data.get('error_message', 'Unknown error')}")

            return data.get("result", {})

        except requests.exceptions.RequestException as e:
            raise GoogleMapsServiceError(f"Request failed: {str(e)}")

    @classmethod
    def create(cls) -> 'GoogleMapsService':
        """Factory method to create a new instance of the service"""
        return cls()
