from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Schema for creating a new business
class BusinessCreate(BaseModel):
    osm_id: Optional[str] = None
    name: str = Field(..., example="Hotel Sunshine")
    business_type: str = Field(..., example="Hotel")
    address: Optional[str] = Field(None, example="123 Main Street")
    latitude: float = Field(..., example=40.7128)
    longitude: float = Field(..., example=-74.0060)
    phone_number: Optional[str] = Field(None, example="+123456789")
    email: Optional[str] = Field(None, example="info@hotel.com")
    website: Optional[str] = Field(None, example="https://hotel.com")

# Schema for updating an existing business
class BusinessUpdate(BaseModel):
    name: Optional[str] = None
    business_type: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None

# Schema for returning business data in API responses
class BusinessResponse(BaseModel):
    id: int
    osm_id: Optional[str]
    name: str
    business_type: str
    address: Optional[str]
    latitude: float
    longitude: float
    phone_number: Optional[str]
    email: Optional[str]
    website: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy ORM
