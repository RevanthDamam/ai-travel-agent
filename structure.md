# Project Structure

- `backend/`
  - `app/`
    - `api/v1/`
      - `endpoints/`
        - `travel.py` - Contains HTTP path operations for itinerary resources. Defines schemas, routes (GET to fetch, POST to create), and queries the database session.
      - `router.py` - Merges sub-routers under a unified router interface. Registers the travel endpoints under the `/travel` subpath.
    - `core/`
      - `config.py` - Manages app-wide configurations via Pydantic settings. Reads environment variables for CORS headers, API prefixes, and the PostgreSQL connection URL.
    - `db/`
      - `session.py` - Initializes the SQLAlchemy PostgreSQL engine and local sessionmaker. Exposes a `get_db` generator dependency to securely inject database sessions.
    - `models/`
      - `travel.py` - Holds the SQLAlchemy ORM `Itinerary` model representing the database table schemas (id, destination, days).
    - `main.py` - Main FastAPI application handler. Configures the CORS origins middleware, creates schemas/tables, registers v1 routers, and serves the base path.
  - `requirements.txt` - Dependency file listing standard backend libraries (`fastapi`, `uvicorn`, `sqlalchemy`, `psycopg2-binary`, etc.).
  - `run.py` - Script using `uvicorn` to programmatically load and host the API on port `8000` with live file reloader.
- `frontend/`
  - `src/`
    - `App.jsx` - React core component containing UI inputs, local states (loading, errors, lists), submit handlers, and API connection callers.
    - `App.css` - Custom styling declarations matching modern aesthetic specifications (glassmorphic boxes, dark palette, hover animations).
- `structure.md` - Directory & file map of the application (this documentation file).

