from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Welcome to the FastAPI root endpoint!"})
# main.py
:contentReference[oaicite:1]{index=1}
:contentReference[oaicite:2]{index=2}
:contentReference[oaicite:3]{index=3}

app = FastAPI()

# Request body schema for creating a user
:contentReference[oaicite:4]{index=4}
    username: str
    email: EmailStr
    :contentReference[oaicite:5]{index=5}

# Response schema including an ID
:contentReference[oaicite:6]{index=6}
    id: int

# In-memory store (for demo purposes)
:contentReference[oaicite:7]{index=7}
next_user_id = 1

:contentReference[oaicite:8]{index=8}
:contentReference[oaicite:9]{index=9}
    """
    :contentReference[oaicite:10]{index=10}
    """
    global next_user_id
    :contentReference[oaicite:11]{index=11}
    :contentReference[oaicite:12]{index=12}
    next_user_id += 1
    return new_user

:contentReference[oaicite:13]{index=13}
:contentReference[oaicite:14]{index=14}
    """
    :contentReference[oaicite:15]{index=15}
    """
    :contentReference[oaicite:16]{index=16}
        :contentReference[oaicite:17]{index=17}
            return u
    :contentReference[oaicite:18]{index=18}

:contentReference[oaicite:19]{index=19}
:contentReference[oaicite:20]{index=20}
    """
    :contentReference[oaicite:21]{index=21}
    """
    return fake_db
