import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    with open("q-vercel-python.json", "r") as file:
        data = json.load(file)
    m1 = m2 = 0
    for i in data:
        if i["name"]==names[0]:
            m1 = i["marks"]
        elif i["name"]==names[1]:
            m2 = i["marks"]
    return JSONResponse(content={"marks": [m1, m2]})

if __name__=="__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
