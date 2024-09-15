import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Allow cross-origin requests from any domain with GET method
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Only allow GET method
)

# Route to return product information in JSON format
@app.get("/products")
async def get_products():
    return [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]

# Fetch the port from environment or use default
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 3030))  # Default port 3030 if not in .env
    uvicorn.run(app, host="0.0.0.0", port=port)
