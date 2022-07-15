import json


class ConfigLoader:
    URL = {}

    def __init__(self):
        with open("cfg/pc.config.json", "r") as config:
            ConfigLoader.URLS = json.load(config)

    @classmethod
    def get_value(cls, value):
        return ConfigLoader.URLS.get(value)
