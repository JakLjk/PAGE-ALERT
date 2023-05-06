from abc import ABC, abstractmethod
class Webpage(ABC):
    def __init__(self, webpage_url, webpage_alias):
        self.url:str = webpage_url
        self.webpage_alias = webpage_alias

    def __repr__(self):
        return f'Webpage(url="{self.url}", display_domain_name="{self.webpage_alias}")'

    @classmethod
    def initialize(cls, webpage_url, webpage_alias):
        return cls(webpage_url, webpage_alias)

    @abstractmethod
    def get_webpage_content(self) -> str:
        "Get webpage's HTML content as string"
        pass



        
