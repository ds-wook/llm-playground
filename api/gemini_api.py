import os

import google.generativeai as genai
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()


class Settings:
    Google_API = os.getenv("Google_API")


# Settings 클래스 인스턴스 생성
settings = Settings()


genai.configure(api_key=settings.Google_API)


def predict_response(message: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(message)
    return response.text
