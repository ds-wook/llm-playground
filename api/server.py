import markdown
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.gemini_api import predict_response

app = FastAPI()
templates = Jinja2Templates(directory="api/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/gemini", response_class=HTMLResponse)
async def post_gemini(request: Request, Check: str = Form(...)):
    # POST로 받은 데이터 처리
    prediction = predict_response(Check)
    prediction = markdown.markdown(prediction)
    return templates.TemplateResponse("llm.html", {"request": request, "prediction": prediction})
