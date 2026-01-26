from fastapi import  FastAPI,HTTPException
from pydantic import  BaseModel

app=FastAPI()


class query(BaseModel):
    def __init__(self):
        pass




@app.get("/")
def get():
    return {"name":"gitesh"}




@app.post("/query")
async def post_qurey():
    pass

