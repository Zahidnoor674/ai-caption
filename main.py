from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()

OPENAI_API_KEY = "zvFErpL4Bl7wPq5MbLKECmYmsXzTcw3I"

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio = await file.read()
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    files = {
        "file": (file.filename, audio, file.content_type),
        "model": (None, "whisper-1")
    }
    response = requests.post("https://api.openai.com/v1/audio/transcriptions", headers=headers, files=files)
    return response.json()
