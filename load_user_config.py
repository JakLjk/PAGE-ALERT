import json

from webpage_info import WebElementsUserConfig


def load_webpage_information(webpages_info_file = 'webpages.json') -> list:
    webpage_template_name = "template_name"
    user_config_data = None
    webpage_objects = []

    with open(webpages_info_file) as json_file:
        user_config_data = json.load(json_file)

    webpages_data = user_config_data['WEBPAGES']
    for webpage_alias, webpage_information in webpages_data.items():
        if webpage_alias == webpage_template_name:
            continue

        web_alias = webpage_alias
        web_url = webpage_information["URL"]

        webpage_info_obj = WebElementsUserConfig(
            webpage_alias=web_alias,
            webpage_url=web_url)
        
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