from fastapi import FastAPI
from pydantic import BaseModel
import psutil
import uvicorn
from functools import lru_cache
import time

# Define response model
class UsageResponse(BaseModel):
    cpu_usage_percent: float
    ram_usage_percent: float
    timestamp: float

# Initialize FastAPI app
app = FastAPI()

# Cache function to reduce resource usage and ensure fresh data
def get_usage_data():
    # Get CPU usage with a short interval
    cpu_percent = psutil.cpu_percent(interval=0.1)
    # Get RAM usage percent
    ram_percent = psutil.virtual_memory().percent
    # Current timestamp for the response
    timestamp = time.time()
    return {
        "cpu_usage_percent": cpu_percent,
        "ram_usage_percent": ram_percent,
        "timestamp": timestamp
    }

# Endpoint to get system usage
@app.get("/", response_model=UsageResponse)
def get_usage():
    return get_usage_data()

if __name__ == "__main__":
    # Run the app without reload (for production)
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
