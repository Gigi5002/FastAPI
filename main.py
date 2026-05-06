from fastapi import FastAPI, Query, Path
 
app = FastAPI()
 
@app.get("/users")
def users(people: list[str]  = Query()):
    return {"people": people}

 
@app.get("/users/{name}")
def users(name:str  = Path(min_length=3, max_length=20), 
            age: int = Query(ge=18, lt=111)):
    return {"name": name, "age": age}