from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, UTC

Base = declarative_base()

class Business(Base):
    """Database model for storing business details."""
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    osm_id = Column(String, unique=True, nullable=True)  # OpenStreetMap ID
    name = Column(String, nullable=False)
    business_type = Column(String, nullable=False)
    address = Column(String, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    website = Column(String, nullable=True)
    scraped_at = Column(DateTime, default=lambda: datetime.now(UTC))
    manual_update = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    updated_at = Column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))
