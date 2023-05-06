import json
import os

LOCAL_FILE = "webpage_elements_data.json"
here = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(here, LOCAL_FILE)


class LocalDataManagement:
    def __init__(self, webpage_alias, webpage_url) -> None:
        self.alias = webpage_alias
        self.url = webpage_url

    def load_data(self):
        with open(data_file) as json_file:
            webpages_data = json.load(json_file)

        webpages_data = webpages_data['WEBPAGES']  
        try:
            webpage_data = webpages_data[str(self.alias)]
        except KeyError:
            raise KeyError(f"There is no information stored about: ALIAS:{self.alias} URL:{self.url}")

        webpage_url = webpage_data["URL"]
        webpage_html = webpage_data['HTML']
        
        assert self.url == webpage_url, "URL address found in local database \
            does not correspond to the one provided"

        return webpage_html


    def save_data(self, 
                  web_html,
                  replace_if_exists=False):
        
        with open(data_file) as json_file:
            full_data = json.load(json_file)
        webpages_data = full_data['WEBPAGES']

        # try reading file, to check if there is current information stored
        data_exists = None
        try:
            webpages_data[self.alias]
            data_exists = True
        except KeyError:
            webpages_data[self.alias] = {}
            data_exists = False

        if not replace_if_exists and data_exists:
            raise AssertionError("replace_if_exists=False, cannot replace exisiting data")

        webpages_data[self.alias]["URL"] = self.url
        webpages_data[self.alias]["HTML"] = web_html

        full_data['WEBPAGES'] = webpages_data
        with open(data_file, 'w') as json_file:
            json.dump(full_data, json_file, indent=4)