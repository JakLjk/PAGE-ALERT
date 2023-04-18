from .webpage import AbsSeleniumWebpage

class SeleniumWebpage(AbsSeleniumWebpage):
    def __init__(self, url, domain_name):
        super().__init__(url, domain_name)

    def get_webpage_content(self):
        with self._selenium_driver() as driver:
            driver.get(url=self.url)
            self._webpage_content = driver.page_source
