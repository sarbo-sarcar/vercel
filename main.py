import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    if len(names) < 1:
        return JSONResponse(content={"error": "At least two names must be provided"}, status_code=400)

    try:
        with open("q-vercel-python.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return JSONResponse(content={"error": "Data file not found"}, status_code=500)
    except json.JSONDecodeError:
        return JSONResponse(content={"error": "Data file is not a valid JSON"}, status_code=500)

    m = []
    for name in names:
        for i in data:
            if i["name"] == name:
                m.append(i["marks"])
                break

    return JSONResponse(content={"marks": m})

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
