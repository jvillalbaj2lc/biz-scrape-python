# Google Places API Constants
GOOGLE_PLACES_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
GOOGLE_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

# Google API Authentication
GOOGLE_API_KEY_ENV = "GOOGLE_API_KEY"
GOOGLE_CREDENTIALS_FILE_ENV = "GOOGLE_APPLICATION_CREDENTIALS"
GOOGLE_AUTH_SCOPES = ["https://www.googleapis.com/auth/places"]

# Google Places API Fields
GOOGLE_PLACES_FIELDS = [
    "name",
    "formatted_address",
    "geometry",
    "formatted_phone_number",
    "website",
    "type",
    "email",
    "opening_hours",
    "rating",
    "reviews",
    "place_id",
    "photos",
    "price_level",
    "user_ratings_total"
]

# Valid place types as per Google Places API documentation
GOOGLE_PLACE_TYPES = [
    "accounting", "airport", "amusement_park", "aquarium", "art_gallery", "atm", "bakery",
    "bank", "bar", "beauty_salon", "bicycle_store", "book_store", "bowling_alley", "cafe",
    "campground", "car_dealer", "car_rental", "car_repair", "car_wash", "casino", "cemetery",
    "church", "city_hall", "clothing_store", "convenience_store", "courthouse", "dentist",
    "department_store", "doctor", "drugstore", "electrician", "electronics_store", "embassy",
    "fire_station", "florist", "funeral_home", "furniture_store", "gas_station", "gym",
    "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "hospital", "insurance_agency",
    "jewelry_store", "laundry", "lawyer", "library", "light_rail_station", "liquor_store",
    "local_government_office", "locksmith", "lodging", "meal_delivery", "meal_takeaway",
    "mosque", "movie_rental", "movie_theater", "moving_company", "museum", "night_club",
    "painter", "park", "parking", "pet_store", "pharmacy", "physiotherapist", "plumber",
    "police", "post_office", "primary_school", "real_estate_agency", "restaurant", "roofing_contractor",
    "rv_park", "school", "secondary_school", "shoe_store", "shopping_mall", "spa", "stadium",
    "storage", "store", "subway_station", "supermarket", "synagogue", "taxi_stand",
    "tourist_attraction", "train_station", "transit_station", "travel_agency", "university",
    "veterinary_care", "zoo"
]

# API response status codes
GOOGLE_API_STATUS_OK = "OK"
GOOGLE_API_STATUS_ZERO_RESULTS = "ZERO_RESULTS"
GOOGLE_API_STATUS_ERROR = "ERROR"
GOOGLE_API_STATUS_INVALID_REQUEST = "INVALID_REQUEST"
GOOGLE_API_STATUS_OVER_QUERY_LIMIT = "OVER_QUERY_LIMIT"
GOOGLE_API_STATUS_REQUEST_DENIED = "REQUEST_DENIED"
GOOGLE_API_STATUS_UNKNOWN_ERROR = "UNKNOWN_ERROR" 