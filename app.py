from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from kokoro import KPipeline
import soundfile as sf

app = FastAPI()
# Kokoro-82M हिंदी के लिए 'hi' लैंग्वेज कोड का इस्तेमाल करता है
pipeline = KPipeline(lang_code='h') 

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    text = data.get("text")
    # यहाँ मॉडल आपकी वॉइस क्लोन करेगा
    audio_data, rate = pipeline(text, voice='af_sarah', speed=1)
    sf.write('output.wav', audio_data, rate)
    return FileResponse('output.wav')
