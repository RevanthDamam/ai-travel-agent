from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Itinerary(Base):
    """
    SQLAlchemy Model representing the itineraries stored in PostgreSQL.
    """
    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)
    destination = Column(String, index=True, nullable=False)
    days = Column(Integer, nullable=False)
