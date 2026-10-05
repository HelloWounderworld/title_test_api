from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import json

import ai.scripts.loading_model.loading_model as llm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/generatetitle")
async def requestllm(request: Request):
    text = await request.body()
    text = text.decode('utf-8')
    text = json.loads(text)
    text = text["textNews"]
    list_title = llm.output_titles(text)
    return { "text": list_title}
