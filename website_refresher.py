from time import sleep

from webpage import SeleniumWebpage, RequestsWebpage, Webpage, WebpageReader
from __webpage_info_container import WebUserConfig, WebFullInfo

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
        user_webpage_information:WebUserConfig,
        web_engine_type = "requests", 
        check_whole_site=False,  # TODO
        use_saved_elem_data=False, # TODO
        refresh_time_min = 1 
        ):

    refresh_time_seconds = refresh_time_min * 60

    webpage_url = user_webpage_information.webpage_url
    webpage_alias = user_webpage_information.webpage_alias

    # Initialize proper engine
    webpage_obj = get_webpage_obj(web_engine_type)
    webpage_obj.initialize(
                webpage_url=webpage_url, 
                webpage_alias=webpage_alias)
    
    # TODO if use_saved_elem_data=True try to read webpage_data_management and get webstite_elements object
    # TODO init read_website_elements and get webstite_elements object
    # TODO use content_comparer to compare both website_elements, if there is difference of lacks, raise exception
    
    while True:
        webpage_obj.refresh_webpage_content()
        current_webpage_obj = None




        sleep(refresh_time_seconds)
    # TODO refresh every x seconds

    # TODO init read_website_elements and get webstite_elements object
    
    #Refreshes data about webpage

    webpage_obj.get_webpage_content()
    # TODO use content_comparer to compare webpage_elements in data and from website

    # TODO if they differ, return information about object that differs






    
