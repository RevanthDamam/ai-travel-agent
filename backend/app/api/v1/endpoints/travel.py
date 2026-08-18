from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.models.travel import Itinerary

router = APIRouter()

# Schema for incoming request validation
class ItineraryCreate(BaseModel):
    destination: str
    days: int

@router.get("/")
def get_travel_status(db: Session = Depends(get_db)):
    """
    Retrieves all stored travel itineraries from the PostgreSQL database.
    """
    itineraries = db.query(Itinerary).all()
    return {
        "status": "ready",
        "message": "AI Travel Agent Backend is active",
        "data": itineraries
    }

@router.post("/itinerary")
def create_itinerary(payload: ItineraryCreate, db: Session = Depends(get_db)):
    """
    Creates a new travel itinerary and commits it to the PostgreSQL database.
    """
    # Create database model instance
    db_itinerary = Itinerary(
        destination=payload.destination,
        days=payload.days
    )
    # Add and commit to database
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    
    return {
        "message": "Itinerary created successfully",
        "data": db_itinerary
    }
