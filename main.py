
import subprocess
from subprocess import Popen, PIPE, STDOUT, CalledProcessError
from fastapi import FastAPI, status, HTTPException
from model.pc import Health_response

app = FastAPI()

@app.get("/pc/power", status_code=status.HTTP_200_OK, response_model=Health_response)
def get_pc_powered_state():
    #TODO move to config file
    hosts = ['192.168.1.130']
    hosts_status = []
    try:
        for host in hosts:
            #TODO make parameter for ping configurable
            stdout = (Popen(['ping', '-c 2', host], stdout=PIPE, stderr=STDOUT)).communicate()
            hosts_status.append(stdout)

    except CalledProcessError as err:
        #TODO log errors
        print(err)
        raise HTTPException(status_code=500, detail='server error while executing command')
    except:
        raise HTTPException(status_code=500, detail='general server error')
    #TODO log host status
    return {'status': True}


@app.post("/pc/command", status_code=status.HTTP_200_OK)
def send_command():
    return {"command": "return thing"}
