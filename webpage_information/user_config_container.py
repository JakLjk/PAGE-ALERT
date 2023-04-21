
from abc import ABC, abstractmethod


class UserConfig():
    def __init__(self, webpage_alias, webpage_url) -> None:
        self.webpage_alias = webpage_alias
        self.webpage_url = webpage_url
        self._webpage_html_elements = {}        

    def __repr__(self) -> str:
        return f"WebInformation(webpage_aliast={self.webpage_alias}, webpage_url={self.webpage_url})"
    
    def __str__(self) -> str:
        return f"""WebInformation:
            Alias: {self.webpage_alias}
            URL: {self.webpage_url}
            Elements to check: {self._web_elems_amount}"""

    def __getitem__(self, key):
        return self._webpage_html_elements[key]
    
    @property
    def _web_elems_amount(self):
        return len(self._webpage_html_elements)

    def add_html_element(self, 
                         element_alias:str, 
                         element_type:str, 
                         element_tag_type:str, 
                         element_tag_value:str):
        """adds html element with it's details to webpage's html elements list"""
        self._webpage_html_elements[element_alias] = {
            "element_type":element_type,
            "element_tag_type":element_tag_type,
            "element_tag_value":element_tag_value
        }

    @property
    def html_elements(self) -> dict:
        return self._webpage_html_elements