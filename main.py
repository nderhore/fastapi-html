from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.templating import Jinja2Templates

from schemas.Message import Message

app = FastAPI()
# configuration de jinja2 afin d'utiliser le dossier 'templates'
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
  return templates.TemplateResponse("index.html", {"request": request, "name": "José "})

@app.post("/api/messages/")
async def create_message(message : Message):
  return JSONResponse(content={"message":message.contenu})
