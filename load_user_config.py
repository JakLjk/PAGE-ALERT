import json
from .user_webpage_information import WebpageInfo


def load_webpage_information() -> list:
    webpages_info = 'webpages.json'
    webpage_template_name = "template_name"
    data = None

    with open(webpages_info) as json_file:
        data = json.load(json_file)

    webpages_data = data['WEBPAGES']
    for webpage_alias, webpage_information in webpages_data.items():
        if webpage_alias == webpage_template_name:
            continue
        webpage_information = WebpageInfo()

load_webpage_information()