# Author: Miguel Bedoya
# Made in 8 of june 2022

from subprocess import Popen, PIPE, STDOUT, CalledProcessError
from fastapi import FastAPI, status, HTTPException
from model.pc import Health_response
from src.configloader import ConfigLoader

app = FastAPI()

#TODO move endpoint to file
@app.get("/pc/power", status_code=status.HTTP_200_OK, response_model=Health_response)
def get_pc_powered_state():
    

    config = ConfigLoader()

    #TODO move to config file
    host = config.get_value("host")
    hosts_status = []

    try:

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

