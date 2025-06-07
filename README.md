# docker-fastapi-with-keycloak
Basic Setup for a FastAPI deployment protected by Keycloak

## Deployment Order
Follow these steps in sequence; each component has its own detailed README you must follow before starting:

1. Frontproxy
   - cd frontproxy
   - Copy and edit environment file: `cp example-env .env` then set your domain, certs and service URLs
   - `docker-compose up -d`

2. Keycloak
   - cd keycloak
   - Copy and edit environment file: `cp example-env .env` then set DB and admin credentials
   - `docker-compose up -d`

3. FastAPI
   - cd fastapi
   - Copy and edit environment file: `cp example-env .env` then set Keycloak URL, realm, client ID/secret
   - `uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000`


> [!WARNING] 
>Make sure to review and complete the individual README.md in each directory for prerequisites and detailed configuration before running these commands.