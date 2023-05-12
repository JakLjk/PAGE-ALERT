from logger import logger
from response_methods import Responses

from webpage import SeleniumWebpage, RequestsWebpage
from webpage import LocalWebpage, Webpage
from webpage_information import UserConfig
from webpage_comparer import are_webpages_the_same

from threading import Lock
from time import sleep, strftime, localtime

def get_webpage_obj(engine_name='') -> Webpage:
    """Allows for selecting most suitable webpage element,
    If webpage has a lot of javascriptm Selenium might be better choice"""
    web_engines = {
        "requests":RequestsWebpage,
        "selenium":SeleniumWebpage}
    try:
        return web_engines[engine_name]
    except KeyError as ke:
        web_engines_names = ' or '.join(str(web_engines.keys()))
        raise KeyError(f"Passed wrong argument for web_engine_type, try:  {web_engines_names}")

def refresh_object(
        user_webpage_information:UserConfig,
        thread_lock:Lock,
        web_engine_type="requests", 
        response_elements:Responses=None,
        check_whole_site=False,  # TODO
        use_saved_elem_data=False,
        ):
    """Main function for fetching and comparing webpage data"""
    
    # Loading configs with webpage details
    webpage_alias = user_webpage_information.webpage_alias
    logger.info(f"{webpage_alias}| Unpacking user config")
    webpage_url = user_webpage_information.webpage_url
    refresh_time_seconds = user_webpage_information.retry_interval_min * 60
    num_of_retries = user_webpage_information.num_of_retries

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
        with thread_lock:
            local_webpage_obj.set_webpage_content(
                    html=webpage_obj.get_webpage_content(),
                    replace_if_exists=True)

    while True:
        current_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        try: 
            logger.info(f"{webpage_alias}| Checking...")
            are_webs_the_same = are_webpages_the_same(
                        user_config=user_webpage_information,
                        webpage_1=webpage_obj,
                        webpage_2=local_webpage_obj)
            
            if are_webs_the_same[0]:
                logger.info(f"{webpage_alias}| Did not find any differences between reference and current webpage")
            else: 
                logger.info(f"{webpage_alias}| Found differences between reference and current webpage")
                logger.info(f"Sending notifiation via {len(response_elements)} methods")
                different_aliases = ", ".join(are_webs_the_same[1])
                for response in response_elements:
                    response.send_response(
                        web_alias = webpage_alias,
                        element_details = different_aliases,
                        time_of_occurence = current_time)
                num_of_retries = 0
            
            logger.info("===============================================")
            if num_of_retries is not None and num_of_retries <=0:
                break
            if num_of_retries is not None:
                num_of_retries -= 1
            sleep(refresh_time_seconds)
            
        except Exception as expt:
            for response in response_elements:
                print(response)
                response.send_failure_info(
                    web_alias = webpage_alias,
                    time_of_occurence = current_time,
                    error_details = expt)
            raise expt

    
