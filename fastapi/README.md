# FastAPI Service

This directory contains the FastAPI application for your demo API.

## Prerequisites

1. Python 3.11+ installed.
2. Copy the example environment file and rename:

   ```bash
   cp example-env .env
   ```
3. Open `.env` and set your Keycloak values:
   - KEYCLOAK_URL
   - REALM
   - CLIENT_ID
   - CLIENT_SECRET

## Install & Run

```bash
# (Optional) create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r src/app/requirements.txt

# Start FastAPI (with auto‐reload)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Or with the Compose file:

> [!WARNING] 
>For the Compose file to work you will need a frontproxy as the one in the `/frontproxy` directory


```bash
docker compose up -d 
```

Browse the interactive docs at http://localhost:8000/docs

---

# Use with Frontproxy

Make sure the Proxy is up and healthy. After that login to the web ui of the npm and set a domain for the IPv4 address that is declared in the fastapis `docker-compose.yml` (in the demp setup this would be `172.20.20.20` on Port `8000`). 

After that you can access the docs at https://your-domain/docs