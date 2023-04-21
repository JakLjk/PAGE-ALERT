from .abs_web_elements_info import WebInformation


class WebUserConfig(WebInformation):
    def __init__(self, webpage_alias, webpage_url) -> None:
        super().__init__(webpage_alias, webpage_url)

    def __repr__(self) -> str:
        return f"WebUserConfig(webpage_aliast={self.webpage_alias}, webpage_url={self.webpage_url})"

    def add_html_element(self, 
                         element_alias:str, 
                         element_type:str, 
                         element_tag_type:str, 
                         element_tag_value:str):
        
        self._webpage_html_elements[element_alias] = {
            "type":element_type,
            "tag_type":element_tag_type,
            "tag_value":element_tag_value}
    def show_d_test(self):
        print(self._webpage_html_elements)
        

class WebFullInfo(WebInformation):
    def __init__(self, webpage_alias, webpage_url) -> None:
        super().__init__(webpage_alias, webpage_url)

    def __repr__(self) -> str:
        return f"WebFullInfo(webpage_aliast={self.webpage_alias}, webpage_url={self.webpage_url})"

    def add_html_element(self, 
                         element_alias:str, 
                         element_type:str, 
                         element_tag_type:str, 
                         element_tag_value:str,
                         element_value:str):
        
        self._webpage_html_elements[element_alias] = {
            "type":element_type,
            "tag_type":element_tag_type,
            "tag_value":element_tag_value,
            "tag_value":element_tag_value,
            "element_value":element_value}
    
