from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Create the SQLAlchemy database engine using the configured connection string
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)

# Create a configured database Session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for database models to inherit from
Base = declarative_base()

def get_db():
    """
    Dependency function to yield a database session.
    Ensures that the connection is closed after the request is finished.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
