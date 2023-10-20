from fastapi import FastAPI 
import uvicorn
from app import home
from api import weather_api
from fastapi.middleware.cors import CORSMiddleware



api = FastAPI()


origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:8080",
]


api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def configure():
    api.include_router(weather_api.router)
    api.include_router(home.router)



configure()
if __name__ == "__main__":
    uvicorn.run("main:api", reload=True)


