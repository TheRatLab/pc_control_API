import logging
import logging.handlers
from src.configloader import ConfigLoader



class loggingModule:

    def __init__(self):
        config = ConfigLoader()

    logging.basicConfig(filename='/var/log/app.log', filemode='a',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
