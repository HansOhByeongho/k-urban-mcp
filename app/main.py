from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI(title="k-urban-mcp",version="0.3.0")
class Query(BaseModel): query:str
@app.get("/health")
def health(): return {"status":"ok","project":"k-urban-mcp","version":"0.3.0"}
@app.post("/analyze")
def analyze(req:Query): return {"domain":"urban","query":req.query,"checks":["land use","building register","land price/transactions","planning/regulation"],"status":"prototype"}
