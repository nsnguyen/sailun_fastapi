from fastapi import APIRouter, Depends, Header, status
from fastapi.responses import JSONResponse
import json

router = APIRouter()


@router.get("/")
def hello_word():

  response = {
    "message": "Hello World! My name is Sailun and I love Python.",
    "statusCode": status.HTTP_200_OK
  }
  return JSONResponse(status_code=status.HTTP_200_OK, content=response)
