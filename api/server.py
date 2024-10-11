from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from api.gemini_api import predict_response

app = FastAPI()
templates = Jinja2Templates(directory="api/templates")


class NameValues(BaseModel):
    Check: str = None


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/gemini", response_class=HTMLResponse)
async def handle_form(request: Request, Check: str = Form(...)):
    # POST로 받은 데이터 처리
    prediction = predict_response(Check)
    return templates.TemplateResponse("llm.html", {"request": request, "prediction": prediction})
