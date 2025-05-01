from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager


load_dotenv()

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)

    yield




@app.get("/")
def read_root():
    return {"Hello": "World"}
