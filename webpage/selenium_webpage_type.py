from .headless_selenium_drivers import HeadllessFirefoxDriver
from .webpage import Webpage

class SeleniumWebpage(Webpage):
    def __init__(self, webpage_url, webpage_alias):
        super().__init__(webpage_url, webpage_alias)

    def refresh_webpage_content(self):
        with self._selenium_driver() as driver:
            driver.get(url=self.url)
            return driver.page_source

    def change_driver(self, driver:str="firefox"):
        """Accepted drivers: firefox, chromium, safari, edge, opera"""
        # TODO implement other drivers
        accepted_drivers = {
            "firefox":HeadllessFirefoxDriver,
            "chromium":None,
            "safari":None,
            "edge":None,
            "opera":None}
        
        driver = str.lower(driver)
        if driver in accepted_drivers.keys():
            self._selenium_driver = accepted_drivers[driver]
        else:
            raise ValueError("Wrong driver name passed")