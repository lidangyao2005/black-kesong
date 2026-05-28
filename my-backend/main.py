from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmotionRequest(BaseModel):
    emotion: str
    age: int

@app.post("/api/generate_scene")
def generate_scene(data: EmotionRequest):
    emotion = data.emotion
    if emotion == "happy":
        scene = "你今天真开心！阳光明媚，世界都在对你微笑～"
    elif emotion == "sad":
        scene = "难过没关系，我会陪着你，一切都会好起来。"
    elif emotion == "angry":
        scene = "生气的时候深呼吸，慢慢放松，你会变得平静。"
    elif emotion == "surprised":
        scene = "哇！好惊喜呀，生活真有趣！"
    else:
        scene = "现在安安静静的，很舒服。"
    return {"scene": scene}