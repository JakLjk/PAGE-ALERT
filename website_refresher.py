from time import sleep

from logger import logger

from webpage import SeleniumWebpage, RequestsWebpage
from webpage import LocalWebpage, Webpage
from webpage_information import UserConfig
from webpage_comparer import are_webpages_the_same

def get_webpage_obj(engine_name='') -> Webpage:
    web_engines = {
        "requests":RequestsWebpage,
        "selenium":SeleniumWebpage}
    try:
        return web_engines[engine_name]
    except KeyError as ke:
        web_engines_names = ' or '.join(str(web_engines.keys()))
        raise KeyError(f"Passed wrong argument for web_engine_type, try:  {web_engines_names}")

# Change fucntion into class with accessible condition for while loop?  
def refresh_object(
        user_webpage_information:UserConfig,
        web_engine_type = "requests", 
        check_whole_site=False,  # TODO
        use_saved_elem_data=False, # TODO
        refresh_time_min = 1 
        ):
    
    
    webpage_url = user_webpage_information.webpage_url
    webpage_alias = user_webpage_information.webpage_alias
    logger.info(f"Initializing refresh function for webpage: {webpage_alias}")

    refresh_time_seconds = refresh_time_min * 60

    logger.info(f"{webpage_alias}| webdriver type: {web_engine_type}")
    web_engine_type = get_webpage_obj(web_engine_type)

    logger.info(f"{webpage_alias}| Initializing online webpage container")
    webpage_obj = web_engine_type.initialize(
                webpage_url=webpage_url, 
                webpage_alias=webpage_alias)
    
    logger.info(f"{webpage_alias}| Initializing local webpage container")
    local_webpage_obj = LocalWebpage.initialize(
                webpage_url=webpage_url, 
                webpage_alias=webpage_alias)
    
    logger.info(f"{webpage_alias}| Using previously saved webpage structure = {use_saved_elem_data}")
    if not use_saved_elem_data:
        local_webpage_obj.set_webpage_content(
                html=webpage_obj.get_webpage_content(),
                replace_if_exists=True)


    while True:
        logger.info(f"{webpage_alias}| Checking...")
        are_webs_the_same = are_webpages_the_same(
                    user_config=user_webpage_information,
                    webpage_1=webpage_obj,
                    webpage_2=local_webpage_obj)
        if are_webs_the_same:
            logger.info(f"{webpage_alias}| Did not find any differences between reference and current webpage")
        else: 
            logger.info(f"{webpage_alias}| Found differences between reference and current webpage")


        sleep(refresh_time_seconds)

    





    
