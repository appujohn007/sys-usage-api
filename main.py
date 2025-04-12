from fastapi import FastAPI
import psutil
import uvicorn

app = FastAPI()

@app.get("/")
def get_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    return {
        "cpu_usage_percent": cpu_percent,
        "ram_usage_percent": ram_percent
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
