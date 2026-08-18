# Import the main FastAPI class to initialize our web application framework
from fastapi import FastAPI
# Import CORSMiddleware to allow cross-origin resource sharing from the frontend
from fastapi.middleware.cors import CORSMiddleware
# Import application-wide settings configured via Pydantic
from app.core.config import settings
# Import the aggregated version 1 API router
from app.api.v1.router import api_router
# Import the database engine and Base model
from app.db.session import engine, Base
# Import model classes to register them with metadata
from app.models.travel import Itinerary

# Create database tables if they do not exist
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application instance with configuration options
app = FastAPI(

    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configure Cross-Origin Resource Sharing (CORS) middleware 
# This permits frontend applications running on other domains (e.g., localhost:5173) to communicate with this API
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include the endpoints router under the /api/v1 prefix
app.include_router(api_router, prefix=settings.API_V1_STR)

# Define a root level endpoint primarily used for basic health/liveness checks
@app.get("/")
def root():
    return {"message": "Welcome to AI Travel Agent API"}

