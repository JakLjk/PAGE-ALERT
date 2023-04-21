from abc import ABC, abstractmethod
from urllib.parse import urlparse

from .headless_selenium_drivers import HeadllessFirefoxDriver

class Webpage(ABC):
    def __init__(self, url, webpage_alias):
        self.url:str = url
        self.webpage_alias = webpage_alias

    def __repr__(self):
        return f'Webpage(url="{self.url}", display_domain_name="{self._domain_name}")'

    @classmethod
    def initialize(cls, url, webpage_alias):
        return cls(url, webpage_alias)

    @abstractmethod
    def get_webpage_content(self) -> str:
        "Get webpage's HTML content as string"
        pass



        
