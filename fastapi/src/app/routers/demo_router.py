from fastapi import APIRouter, Depends
from authorize.keycloak import validate_keycloak_token


router = APIRouter()


@router.get("/")
async def read_demo(
    token_info=Depends(validate_keycloak_token)
):
    """A simple demo endpoint that returns a greeting message."""
    return {"message": "Hello from the demo router!"}
