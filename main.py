from fastapi import FastAPI, Request
from pydantic import BaseModel
from model.model_predict import lang_predict
from model.model_predict import __version__ as model_version
import uvicorn
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


class TextIn(BaseModel):
    text : str

class PredictionOut(BaseModel):
    lang: str

# Serve the HTML page
@app.get("/")
def read_root():
    return FileResponse("static/index.html")

# def lang_predict(text: str) -> str:
#     lang = lang_predict(text)
#     print('*********', lang)
#     return "English"

# @app.get("/")
# def home():
#     return {"helth_check": "Ok"}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    lang = lang_predict(payload.text)
    print('*********', lang)
    return JSONResponse({"Language": lang})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use the PORT environment variable or default to 8000
    uvicorn.run(app, host="0.0.0.0", port=port)