from sqlalchemy.orm import Session
from app.models.business import Business
from app.schemas.business import BusinessCreate, BusinessUpdate
from datetime import datetime

class BusinessRepository:
    
    @staticmethod
    def create(db: Session, business: BusinessCreate):
        """Creates a new business entry in the database."""
        db_business = Business(
            osm_id=business.osm_id,
            name=business.name,
            business_type=business.business_type,
            address=business.address,
            latitude=business.latitude,
            longitude=business.longitude,
            phone_number=business.phone_number,
            email=business.email,
            website=business.website,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(db_business)
        db.commit()
        db.refresh(db_business)
        return db_business

    @staticmethod
    def get_by_id(db: Session, business_id: int):
        """Fetch a business by its internal ID."""
        return db.query(Business).filter(Business.id == business_id).first()

    @staticmethod
    def get_by_osm_id(db: Session, osm_id: str):
        """Fetch a business by its OpenStreetMap ID."""
        return db.query(Business).filter(Business.osm_id == osm_id).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10):
        """Fetch all businesses with pagination."""
        return db.query(Business).offset(skip).limit(limit).all()

    @staticmethod
    def update(db: Session, business_id: int, business_update: BusinessUpdate):
        """Update an existing business entry."""
        db_business = db.query(Business).filter(Business.id == business_id).first()
        if not db_business:
            return None
        
        for key, value in business_update.dict(exclude_unset=True).items():
            setattr(db_business, key, value)
        
        db_business.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_business)
        return db_business

    @staticmethod
    def delete(db: Session, business_id: int):
        """Delete a business entry from the database."""
        db_business = db.query(Business).filter(Business.id == business_id).first()
        if not db_business:
            return None
        db.delete(db_business)
        db.commit()
        return db_business

