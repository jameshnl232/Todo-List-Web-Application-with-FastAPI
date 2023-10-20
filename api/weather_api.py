from fastapi import FastAPI, APIRouter, Depends, Form
from typing import Optional, Annotated
from models import Location

router = APIRouter()

@router.get("/api/umbrella")
def do_I_need_an_umbrella(location: Location = Depends()):
    return location




