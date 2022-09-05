from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/headers")
def read_headers(request: Request):
    return dict(request.headers)
