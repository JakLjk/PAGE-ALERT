from abc import ABC, abstractmethod
from urllib.parse import urlparse

from .headless_drivers import HeadllessFirefoxDriver

class Webpage(ABC):
    def __init__(self, url, display_domain_name):
        self.url:str = url
        self._domain_name = display_domain_name
        self._webpage_content = None   

    def __repr__(self):
        return f'Webpage(url="{self.url}", display_domain_name="{self._domain_name}")'

    @classmethod
    def initialize(cls, url):
        domain_name = urlparse(url).netloc
        domain_name = domain_name.split('.')[-2]
        return cls(url, domain_name)

    @property
    def webpage_content(self):
        return self._webpage_content
    
    @property
    def webpage_domain(self):
        return self._domain_name
    
    def website_is_responding(self):
        # TODO return if website is reponding to pings
        pass

    @abstractmethod
    def get_webpage_content(self):
        # Get _webpage_content from website
        self._webpage_content = None
        pass


class AbsSeleniumWebpage(Webpage):
    def __init__(self, url, domain_name):
        super().__init__(url, domain_name)
        self._selenium_driver = HeadllessFirefoxDriver

    def change_driver(self, driver:str="firefox"):
        """Accepted drivers: firefox, chromium, safari, edge, opera"""
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


        
