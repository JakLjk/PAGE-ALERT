# used to read the content of selected website element
from webpage import Webpage
from bs4 import BeautifulSoup
class ReadWebElems:
    def __init__(self, Webpage_obj:Webpage, elems_to_find:list) -> None:
        self.webpage_obj = Webpage_obj
        self.elements_to_find = elems_to_find

        self.web_elements = {}

    def read_web_elements(self):
        if not self.webpage_obj.webpage_content:
            self.webpage_obj.get_webpage_content()
        web_content = self.webpage_obj.webpage_content
        soup = BeautifulSoup(web_content, 'html.parser')
        for elem in self.elements_to_find:
            element_type = elem.element_type
            tag_type = elem.tag_type
            tag_value = elem.tag_type
            
            soup.find(element_type, {tag_type:tag_value})
            self.web_elements

