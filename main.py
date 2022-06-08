from fastapi import FastAPI, status, HTTPException
from model.pc import Health_response
import requests
app = FastAPI()

@app.get("/pc/power", status_code=status.HTTP_200_OK)
async def get_pc_powered_state():
    try:
        req = requests.get("http://192.168.1.130:1886/pc/health")
    except:
        raise HTTPException(status_code=500, detail="server is not on at the moment")
    if req.text == 1:
        response = {"status": True}
    return {response}


@app.post("/pc/command", status_code=status.HTTP_200_OK)
async def send_command():
    return {"command": "return thing"}
