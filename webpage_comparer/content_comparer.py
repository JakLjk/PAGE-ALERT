from webpage_information import UserConfig
from webpage import Webpage
from .read_webpage_elements import read_elements

def are_webpages_the_same(
        user_config:UserConfig,
        webpage_1:Webpage,
        webpage_2:Webpage):

    webpage_1_elements = read_elements(user_config, webpage_1)
    webpage_2_elements = read_elements(user_config, webpage_2)


    return webpage_1_elements == webpage_2_elements


    


