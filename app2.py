from fastapi import FastAPI
import asyncio

application = FastAPI()
@application.get("/greeting")
async def greeting():
    await asyncio.sleep(20)
    return {"message":"Hello World!"}

@application.get("/greetings")
async def greeting():
    await asyncio.sleep(20)
    return {"message":"Hello World!2"}

@application.post("/submit")
def submit(data:dict):
    return {"message":"Data submitted successfully!","data":data["name"]}