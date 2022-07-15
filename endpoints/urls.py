import json

class url_builder:

    version: str = ""
    host: str = ""
    def __init__(self):
        with open("../cfg/pc.config.json", "r") as config:
            pc_config = json.load(config)
            self.version = pc_config.get("version")
            self.host = pc_config.get("host")

    #this should not be here, this needs to be moved to another librarie
    def base_url(self):
        url: str = ""
        base_url: str = f"http://{self.host}"
        url = f"{base_url}/{self.version}"
        return url

    def build_url(self, endpoint):
        return f"{self.base_url()}/{endpoint}"



if __name__ == '__main__':
    url = url_builder()
    print(url.build_url("pc"))