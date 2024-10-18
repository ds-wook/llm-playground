# langchain-playground
랭체인을 활용한 개발 놀이터 만들기

## 환경 설정

### 1. install [rye](https://github.com/mitsuhiko/rye)

[install documentation](https://rye-up.com/guide/installation/#installing-rye)

Linux
```bash
curl -sSf https://rye-up.com/get | bash
echo 'source "$HOME/.rye/env"' >> ~/.bashrc
source ~/.bashrc
```

Windows  
see [install documentation](https://rye-up.com/guide/installation/)


### 2. Create virtual environment

First, Please match the index url to the environment at hand to use torch.

```toml
# pyproject.toml
dependencies = [
    "transformers==4.44.0",
    "torch==1.13.1+cu116",
    "accelerate==0.33.0",
    "jinja2>=3.1.3",
    "flake8>=7.1.1",
    "black>=24.10.0",
    "fastapi>=0.115.0",
    "isort>=5.13.2",
    "uvicorn>=0.31.1",
    "nvitop>=1.3.2",
    "google-generativeai>=0.8.3",
    "ipython>=8.28.0",
    "python-dotenv>=1.0.1",
    "python-multipart>=0.0.12",
]

[[tool.rye.sources]]
name = "torch"
url = "https://download.pytorch.org/whl/cu116" # change this to match your environment
type = "index"
```

Second, create virtual environment.
```bash
rye sync
```

## 데이터 생성
```python
rye run app/preprocessor.py
```
실행하면 다음과 같이 데이터가 생성됩니다.

```
└── app
    ├── __pycache__
    └── data
        └── weather_data.csv
```

### 폴더 구성
```
app
  ├── data: 데이터 폴더
  │   └── weather_data.csv
  ├── preprocessor.py: API활용하여 불러옴
  ├── server.py: FastAPI 실행
  └── templates: Html 템플릿
      ├── df_representation.html
      └── introduction.html
```
## Run code

API 서버는 다음과 같이 실행합니다.
```sh
rye run uvicorn app.server:app --host=127.0.0.1 --port=8000 --reload
```
