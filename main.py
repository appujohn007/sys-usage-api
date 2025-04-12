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

# Cache function to reduce resource usage
@lru_cache(maxsize=1)
def get_cached_usage():
    return {
        "cpu_usage_percent": psutil.cpu_percent(interval=None),
        "ram_usage_percent": psutil.virtual_memory().percent,
        "timestamp": time.time()  # Return timestamp to know when data was last fetched
    }

# Endpoint to get system usage
@app.get("/", response_model=UsageResponse)
def get_usage():
    return get_cached_usage()

if __name__ == "__main__":
    # Run the app without reload (for production)
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
