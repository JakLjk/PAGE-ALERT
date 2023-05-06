from webpage_information import UserConfig
from webpage import Webpage
from .read_webpage_elements import read_elements

def are_webpages_the_same(
        user_config:UserConfig,
        webpage_1:Webpage,
        webpage_2:Webpage):

    are_the_same = None
    aliases_difference = None
    webpage_1_elements = read_elements(user_config, webpage_1)
    webpage_2_elements = read_elements(user_config, webpage_2)
    web1set = set(webpage_1_elements.items())
    web2set = set(webpage_2_elements.items())

    differences = web1set ^ web2set
    if differences: 
        are_the_same = False
        aliases_difference = list(set([al[0] for al in differences]))
    else:
        are_the_same = True
    return are_the_same, aliases_difference


    


