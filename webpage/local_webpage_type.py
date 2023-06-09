from .webpage import Webpage
from local_web_data import LocalDataManagement

class LocalWebpage(Webpage):
    def __init__(self, webpage_url, webpage_alias): 
        super().__init__(webpage_url, webpage_alias)
        self.local_data = LocalDataManagement(webpage_alias=webpage_alias,
                                               webpage_url=webpage_url)

    def __repr__(self):
        return f'Webpage(url="{self.url}", webpage_alias="{self.webpage_alias}")'

    def get_webpage_content(self):
        return self.local_data.load_data()

    def set_webpage_content(self, html:str, replace_if_exists=False):
        self.local_data.save_data(
                            web_html=html,
                            replace_if_exists=replace_if_exists)
        
    
