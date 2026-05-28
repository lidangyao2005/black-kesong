from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 允许所有跨域请求（前端必须）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SceneRequest(BaseModel):
    emotion: str
    age: int

@app.post("/api/generate_scene")
def generate_scene(req: SceneRequest):
    emotion = req.emotion
    if emotion == "happy":
        scene = "今天你很开心！小鸟在唱歌，阳光暖暖的，世界真美好～"
    elif emotion == "sad":
        scene = "难过没关系，我们慢慢变好，抱抱你，一切都会好起来。"
    elif emotion == "angry":
        scene = "生气的时候可以深呼吸，慢慢数到五，心情就会平静下来啦。"
    elif emotion == "surprised":
        scene = "哇，好惊喜！生活里总有有趣的事情等着你发现。"
    else:
        scene = "现在很平静哦，安安静静的也特别棒～"
    return {"scene": scene}

@app.get("/")
def root():
    return {"message": "Backend is running!"}