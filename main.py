import os
from fastapi import FastAPI, HTTPException, Request, File, UploadFile
from pydantic import BaseModel
from core import Bard
from fastapi.middleware.cors import CORSMiddleware

from gtts import *
from fastapi.staticfiles import StaticFiles
import speech_recognition as sr

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

r = sr.Recognizer()

class Message(BaseModel):
    sessionId: str
    message: str

class Text(BaseModel):
    name: str
    message: str

@app.post("/ask")
async def ask(data: Message):
    bard = Bard(token=data.sessionId, proxies={'http':'http://127.0.0.1:7890', 'https':'http://127.0.0.1:7890'})
    answer = bard.get_answer(data.message)['content']
    return answer

@app.post("/tts")
def tts(data: Text):
    tts = gTTS(data.message)
    file_name = str(data.name) + ".mp3"
    file_path = os.path.join("static", file_name)
    tts.save(file_path)
    return {"audio_url": f"/static/{file_name}"}

@app.post("/upload")
def upload(file: UploadFile):
     if not file:
         return {"message": "no file sent"}
     else:
        with open(file.filename, "wb") as f:
            f.write(file.file.read())
        return {"message": "file create"}

@app.get("/recognize")
def recognize():
    try:
        with sr.AudioFile('speech.wav') as source:
            audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='en-US')
        print(text)
        return {"message": "text recognized", "text": text}
    except:
        return {"message": "no text recognized"}