from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Welcome to the FastAPI root endpoint!"})
