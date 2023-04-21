from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


class HeadllessFirefoxDriver(Firefox):
    def __init__(self):
        options = Options()
        options.headless = True
        super().__init__(options=options)

