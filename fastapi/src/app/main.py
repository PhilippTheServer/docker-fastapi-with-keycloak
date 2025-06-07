from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging

# from routers.name import endpoint (example import, for a router)
from routers.demo_router import router as demo_router


app = FastAPI(title="Demo API")


# Configure logging once at the entry point
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


origins = ["*"]  # Consider restricting this in a production environment

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Example router (you can replace this with your actual router)
# app.include_router(any_router.router)
app.include_router(demo_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
