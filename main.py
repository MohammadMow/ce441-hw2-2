from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("exoloit.html", "r", encoding="utf-8") as file:
        content = file.read()
    return HTMLResponse(content=content)
