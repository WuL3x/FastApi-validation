import uvicorn
from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8081, reload=True, log_level="info", workers=4)
