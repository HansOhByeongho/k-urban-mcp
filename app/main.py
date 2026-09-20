from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title="K-Urban MCP",version="0.1.0")
class Query(BaseModel):
    query:str

@app.get("/health")
def health(): return {"status":"ok","project":"k-urban-mcp","version":"0.1.0"}

@app.post("/analyze")
def analyze(req:Query):
    return {"project":"k-urban-mcp","domain":"urban","query":req.query,"status":"prototype","next":"connect verified official data sources"}
