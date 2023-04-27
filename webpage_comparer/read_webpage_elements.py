# used to read the content of selected website element
from webpage_information import UserConfig
from webpage import Webpage
from bs4 import BeautifulSoup

def read_elements(
          user_config:UserConfig,
          webpage_obj:Webpage) -> dict:
    
    elements_to_find = user_config.get_elements
    web_html = webpage_obj.get_webpage_content()
    soup = BeautifulSoup(web_html, 'html.parser')

    found_elements = {}
    for elem_alias, elem_data in elements_to_find.items():
            element_type = elem_data["element_type"]
            element_details = elem_data["tag_info"]
            found_element = soup.find(element_type, element_details)
            found_elements[elem_alias] = found_element
    return found_elements



