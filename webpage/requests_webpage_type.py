import requests

from .webpage import Webpage

class RequestsWebpage(Webpage):
    def __init__(self, webpage_url, webpage_alias):
        super().__init__(webpage_url, webpage_alias)

    def get_webpage_content(self):
        request = requests.get(self.url)
        return request.text

