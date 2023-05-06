from .user_config_container import UserConfig

import json
from typing import List
from pathlib import Path


base_path = Path(__file__).parent
file_path = (base_path / "../configs/webpages.json").resolve()


def load_webpage_information(webpages_info_file_dir:str = file_path) -> List[UserConfig]:
    webpage_template_name = "webpage_alias"
    user_config_data = None
    webpage_objects = []

    with open(webpages_info_file_dir) as json_file:
        user_config_data = json.load(json_file)

    webpages_data = user_config_data['WEBPAGES']
    for webpage_alias, webpage_information in webpages_data.items():
        if webpage_alias == webpage_template_name:
            continue

        web_alias = webpage_alias
        web_url = webpage_information["URL"]
        web_refresh_interval = webpage_information["CHECK_INTERVAL_MIN"]
        web_num_of_refresh = webpage_information["NUM_OF_RETRIES"]

        webpage_info_obj = UserConfig(
            webpage_alias=web_alias,
            webpage_url=web_url,
            retry_interval=web_refresh_interval,
            num_of_retries=web_num_of_refresh)
        
        elements = webpage_information["CHECK_ELEMENTS"]
        for element_alias, element_details in elements.items():
            alias = element_alias
            element_type = element_details["ELEMENT_TYPE"]
            element_tag_type = element_details["ELEMENT_TAG_TYPE"]
            element_tag_value = element_details["ELEMENT_TAG_VALUE"]

            webpage_info_obj.add_html_element(
                element_alias=alias,
                element_type=element_type,
                element_tag_type=element_tag_type,
                element_tag_value=element_tag_value)
            
        webpage_objects.append(webpage_info_obj)

    return webpage_objects