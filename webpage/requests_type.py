import requests

from .webpage import Webpage

class RequestsWebpage(Webpage):
    def __init__(self, url, domain_name):
        super().__init__(url, domain_name)

    def get_webpage_content(self):
        request = requests.get(self.url)
        self._webpage_content = request.text

