from fastapi import APIRouter

router = APIRouter()

@router.get("")
def say_hello():
    return "Hello World!"