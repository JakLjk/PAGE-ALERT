from time import sleep

from webpage import SeleniumWebpage, RequestsWebpage, Webpage

def get_webpage_obj(engine_name='') -> Webpage:
    web_engines = {
        "requests":RequestsWebpage,
        "selenium":SeleniumWebpage}
    try:
        return web_engines[engine_name]
    except KeyError as ke:
        web_engines_names = ' or '.join(str(web_engines.keys()))
        raise KeyError(f"Passed wrong argument for web_engine_type, try:  {web_engines_names}")
    
def refresh_object(
        url:str, 
        compare_elems:dict, # key is alias, value is element of webpage
        web_engine_type = "requests", 
        check_whole_site=False, 
        use_saved_elem_data=False,
        custom_domain_name:str=""):

    # Initialize proper engine
    webpage_obj = get_webpage_obj(web_engine_type)
    webpage_obj.initialize
    # TODO init read_website_elements and get webstite_elements object

    # TODO if use_saved_elem_data=True try to read webpage_data_management and get webstite_elements object
    # TODO use content_comparer to compare both website_elements, if there is difference of lacks, raise exception

    # TODO refresh every x seconds

    # TODO init read_website_elements and get webstite_elements object
    
    #Refreshes data about webpage

    webpage_obj.get_webpage_content()
    # TODO use content_comparer to compare webpage_elements in data and from website

    # TODO if they differ, return information about object that differs






    
