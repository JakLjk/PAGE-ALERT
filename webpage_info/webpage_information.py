from abc import ABC, abstractmethod

from HTML_element import HTMLElementFullInfo, UserConfigHTMLElement


class AbsWebpageInfo:
    def __init__(self, webpage_alias, webpage_url) -> None:
        self.webpage_alias = None
        self.webpage_url = None
        self.html_elements = []

    @abstractmethod
    def add_html_element(self):
        """adds html element with it's details to html elements list"""

class UserConfigWebInfo(AbsWebpageInfo):
    def __init__(self, webpage_alias, webpage_url) -> None:
        super().__init__(webpage_alias, webpage_url)

    def add_html_element(self, 
                         element_alias:str, 
                         element_type:str, 
                         element_tag_type:str, 
                         element_tag_value:str):
        
        new_element = UserConfigHTMLElement(
                        element_alias,
                        element_type,
                        element_tag_type,
                        element_tag_value)
        
        self.html_elements.append(new_element)


class WebpageFullInfo(AbsWebpageInfo):
    def __init__(self, webpage_alias, webpage_url) -> None:
        super().__init__(webpage_alias, webpage_url)

    def add_html_element(self, 
                         element_alias:str, 
                         element_type:str, 
                         element_tag_type:str, 
                         element_tag_value:str,
                         element_value:str):
        
        new_element = HTMLElementFullInfo(
                        element_alias,
                        element_type,
                        element_tag_type,
                        element_tag_value,
                        element_value)
        
        self.html_elements.append(new_element)