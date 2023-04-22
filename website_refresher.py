from time import sleep

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

    print("_X_____")
    refresh_time_seconds = refresh_time_min * 60

    webpage_url = user_webpage_information.webpage_url
    webpage_alias = user_webpage_information.webpage_alias

    web_engine_type = get_webpage_obj(web_engine_type)
    webpage_obj = web_engine_type.initialize(
                webpage_url=webpage_url, 
                webpage_alias=webpage_alias)

    local_webpage_obj = LocalWebpage.initialize(
                webpage_url=webpage_url, 
                webpage_alias=webpage_alias)
    print("1----")
    print(webpage_obj)
    print("2----")
    print(local_webpage_obj)

    test = are_webpages_the_same(
                user_config=user_webpage_information,
                webpage_1=webpage_obj,
                webpage_2=local_webpage_obj)
    
    print(test)
    # if use_saved_elem_data:
    #     local_html = local_data.load_data()
    # else:
    #     local_data.save_data(webpage_html)
    #     local_html = webpage_html
    
    
    




    #     sleep(refresh_time_seconds)
    # TODO refresh every x seconds

    # TODO init read_website_elements and get webstite_elements object
    
    #Refreshes data about webpage

    # webpage_obj.get_webpage_content()
    # TODO use content_comparer to compare webpage_elements in data and from website

    # TODO if they differ, return information about object that differs






    
