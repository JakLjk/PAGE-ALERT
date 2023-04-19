from abc import ABC, abstractmethod


class ElementsInfo(ABC):
    def __init__(self, webpage_alias, webpage_url) -> None:
        self.webpage_alias = webpage_alias
        self.webpage_url = webpage_url
        self._webpage_html_elements = {}        

    def __repr__(self) -> str:
        return f"ElementsInfo(webpage_aliast={self.webpage_alias}, webpage_url={self.webpage_url})"
    
    def __getitem__(self, key):
        return self._webpage_html_elements[key]

    @abstractmethod
    def add_html_element(self):
        """adds html element with it's details to webpage's html elements list"""