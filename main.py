from fastapi import FastAPI, Response, Cookie
from datetime import datetime
 
app = FastAPI()
 
@app.get("/")
def root(response: Response):
    now = datetime.now()    # получаем текущую дату и время
    response.set_cookie(key="last_visit", value=now)
    return  {"message": "куки установлены"}

@app.get("/visit")
def root(last_visit: str | None = Cookie(default=None)):
    if last_visit == None:
        return {"message": "Это ваш первый визит на сайт"}
    else:
        return  {"message": f"Ваш последний визит: {last_visit}"}