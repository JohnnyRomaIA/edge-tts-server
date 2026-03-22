from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import edge_tts, asyncio, uuid, os

app = FastAPI()

class TTSRequest(BaseModel):
    text: str
    voice: str = "es-MX-JorgeNeural"

@app.post("/tts")
async def tts(req: TTSRequest):
    filename = f"/tmp/{uuid.uuid4()}.mp3"
    communicate = edge_tts.Communicate(req.text, req.voice)
    await communicate.save(filename)
    return FileResponse(filename, media_type="audio/mpeg")

@app.get("/")
def health():
    return {"status": "ok"}
