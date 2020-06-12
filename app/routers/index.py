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


@router.get("/explore")
def hello_exploring():
  response = {
    "message": "Hi! Sailun here. I want to explore the world!",
    "statusCode": status.HTTP_200_OK
  }
  return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@router.get("/food")
def hello_food():
  response = {
    "message": "Hi! Sailun here again. I love steak and tacos! :D",
    "statusCode": status.HTTP_200_OK
  }
  return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@router.get("/hanging")
def hello_hanging(person: str = 'Nguyen'):
  response = {
    "message": "Hi! Sailun here again! I love hanging out with {}".format(person),
    "statusCode": status.HTTP_200_OK
  }
  return JSONResponse(status_code=status.HTTP_200_OK, content=response)
