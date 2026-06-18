from fastapi.responses import HTMLResponse
from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    return {"result": omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Hello!NetPro</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/greeting")
async def greeting(name: str, language: str = "ja"):
    greetings = {
        "ja": f"こんにちは、{name}さん！今日もいい天気ですね。",
        "en": f"Hello, {name}! Have a great day!",
        "zh": f"你好，{name}！祝你今天过得愉快！",
        "ko": f"안녕하세요, {name}님! 좋은 하루 되세요!",
    }
    message = greetings.get(language, greetings["ja"])
    lucky_number = random.randint(1, 100)
    return {
        "name": name,
        "language": language,
        "greeting": message,
        "lucky_number": lucky_number
    }
