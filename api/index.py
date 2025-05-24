from fastapi import FastAPI, Request
import json

app = FastAPI()

# Load data at startup (optional optimization)
with open('api/data.json', 'r') as f:
    data = json.load(f)
marks_map = {item['name']: item['marks'] for item in data}

@app.get("/")
async def get_marks(request: Request):
    # Get 'name' query params
    query_params = request.query_params.getlist('name')
    marks = [marks_map.get(name, None) for name in query_params]
    datareturn = { 'marks': marks }
    return datareturn