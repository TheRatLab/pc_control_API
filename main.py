from fastapi import FastAPI, status
from model.requests import Command
app = FastAPI()

@app.get("/pc/command")
def read_root():
    return {}


@app.post("/pc/command", status_code=status.HTTP_200_OK)
def send_command(command: Command):
    return {"command": command}
