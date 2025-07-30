import time

from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
async def root():
    return {
        "msg": "hello world"
    }

@app.middleware("http")
async def add_process_time_header(request: Request, 
call_next):
    start_time = time.time()
    reponse = await call_next(request)
    process_time = time.time() - start_time
    reponse.headers["X-Process-Time"] = str(process_time)
    return reponse