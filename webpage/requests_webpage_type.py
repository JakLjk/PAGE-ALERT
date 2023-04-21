import requests

from .webpage import Webpage

class RequestsWebpage(Webpage):
    def __init__(self, url, webpage_alias):
        super().__init__(url, webpage_alias)

    def refresh_webpage_content(self):
        request = requests.get(self.url)
        return request.text

