from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.repositories.business_repository import BusinessRepository
from app.schemas.business import BusinessCreate, BusinessResponse, BusinessUpdate
from app.services.google_maps_service import GoogleMapsService
from typing import List
import json


router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/search", response_model=List[BusinessResponse])
def search_businesses(
    business_type: str,
    latitude: float,
    longitude: float,
    radius: int = 5000,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """
    Search businesses using Google Places API and store results in our database.
    """
    google_results = GoogleMapsService().search_businesses(business_type, latitude, longitude, radius, limit)

    if not google_results:
        return []

    businesses = []
    for item in google_results:
        place_id = item.get("place_id")
        details = GoogleMapsService().get_business_details(place_id)

        business_data = {
            "osm_id": place_id,  # Store place_id as our unique identifier
            "name": details.get("name", "Unknown"),
            "business_type": business_type,
            "address": details.get("formatted_address", ""),
            "latitude": item["geometry"]["location"]["lat"],
            "longitude": item["geometry"]["location"]["lng"],
            "phone_number": details.get("formatted_phone_number"),
            "email": None,  # Google API does not provide email directly
            "website": details.get("website"),
        }

        # Convert dictionary to Pydantic schema
        business_schema = BusinessCreate(**business_data)

        existing_business = BusinessRepository.get_by_osm_id(db, business_schema.osm_id)
        if not existing_business:
            new_business = BusinessRepository.create(db, business_schema)
            businesses.append(new_business)
        else:
            businesses.append(existing_business)

    return businesses

@router.post("/", response_model=BusinessResponse)
def create_business(business: BusinessCreate, db: Session = Depends(get_db)):
    """Create a new business entry."""
    return BusinessRepository.create(db, business)

@router.get("/{business_id}", response_model=BusinessResponse)
def get_business(business_id: int, db: Session = Depends(get_db)):
    """Fetch a business by ID."""
    db_business = BusinessRepository.get_by_id(db, business_id)
    if not db_business:
        raise HTTPException(status_code=404, detail="Business not found")
    return db_business

@router.get("/", response_model=List[BusinessResponse])
def get_all_businesses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Fetch all businesses with pagination."""
    return BusinessRepository.get_all(db, skip, limit)

@router.put("/{business_id}", response_model=BusinessResponse)
def update_business(business_id: int, business_update: BusinessUpdate, db: Session = Depends(get_db)):
    """Update a business entry."""
    updated_business = BusinessRepository.update(db, business_id, business_update)
    if not updated_business:
        raise HTTPException(status_code=404, detail="Business not found")
    return updated_business

@router.delete("/{business_id}", response_model=BusinessResponse)
def delete_business(business_id: int, db: Session = Depends(get_db)):
    """Delete a business entry."""
    deleted_business = BusinessRepository.delete(db, business_id)
    if not deleted_business:
        raise HTTPException(status_code=404, detail="Business not found")
    return deleted_business

