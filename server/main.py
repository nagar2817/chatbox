from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://chatbox-one-alpha.vercel.app",
        "http://localhost:3000",
        "https://chatbox-rb3b.onrender.com"  # Added the render.com domain
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "welcome"}

@app.get("/api/hello")
async def read_root():
    return {"message": "Hello World"}