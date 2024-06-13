import pytest
from selenium import webdriver
import os

# Function to configure pytest markers
def pytest_configure(config):
    config.addinivalue_line("markers", "platform_chrome: mark test to run on Chrome")
    config.addinivalue_line("markers", "platform_safari: mark test to run on Safari")

# Fixture to determine the platform
@pytest.fixture(scope="session")
def platform(request):
    platform = os.environ.get("PLATFORM", "chrome").lower()
    return platform

class SetupDriver:
    def __init__(self, browser=None):
        self.browser = browser
        self.driver = None
    
    def url(self):
        env = os.environ.get("ENV", "prod").lower()
        if env == "prod":
            return 'https://www.visionplus.id'
        elif env == "stag":
            return 'https://prelive.visionplus.id/webclient/#/'
        else:
            raise ValueError("Invalid environment type")

    def get_driver(self):
        url = self.url()
        if self.browser == 'chrome':
            self.driver = self.chrome(url)
        elif self.browser == 'safari':
            self.driver = self.safari(url)
        else:
            raise ValueError("Invalid browser type")
        return self.driver

    def chrome(self,url):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ["enable-logging"])
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        return driver

    def safari(self,url):
        driver = webdriver.Safari()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        return driver