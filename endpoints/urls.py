import json
from urllib.parse import urljoin


class urls:

    version: str = ""
    host: str = ""
    def __init__(self):
        with open("../cfg/pc.config.json", "r") as config:
            pc_config = json.load(config)
            self.version = pc_config.get("version")
            self.host = pc_config.get("host")

    def root_path(self):
        base_url: str = "http://" + self.host

        url: str = ""
        url = urljoin(base_url, self.version)
        # add version and path
        print(url)
        return url
    def build_url(self, endpoint):
        pass

if __name__ == '__main__':
    url = urls()
    url.root_path()