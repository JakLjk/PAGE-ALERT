from .abs_web_elements_info import WebInfo

class WebUserConfig(WebInfo):
    def __init__(self, webpage_alias, webpage_url) -> None:
        super().__init__(webpage_alias, webpage_url)

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
        

class WebFullInfo(WebInfo):
    def __init__(self, webpage_alias, webpage_url) -> None:
        super().__init__(webpage_alias, webpage_url)

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
    

# test = WebElementsUserConfig('x','d')
# test.add_html_element('a','b','c','d')
# print(test['a'])
