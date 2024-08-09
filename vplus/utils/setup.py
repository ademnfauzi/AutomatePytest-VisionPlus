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
        elif env == "malaysia":
            return 'https://www.visionplus.my'
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

    def get_driverGoogle(self):
        url = 'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2F%3Fptid%3D19027681%26ptt%3D8%26fpts%3D0&ec=futura_hpp_co_si_001_p&ifkv=AS5LTAQOuWIWiEEw8Nn4FDfaoL9vtyHrtx-rr8WQOmy38w6u6Pyzwbgzeg89xkRc1MbWByI-RKqGuw&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1526908146%3A1719979218405549&ddm=0'
        if self.browser == 'chrome':
            self.driver = self.chrome(url)
        elif self.browser == 'safari':
            self.driver = self.safari(url)
        else:
            raise ValueError("Invalid browser type")
        return self.driver
    
    def get_driverGmail(self):
        url = 'https://mail.google.com/mail/u/0/#inbox'
        if self.browser == 'chrome':
            self.driver = self.chrome(url)
        elif self.browser == 'safari':
            self.driver = self.safari(url)
        else:
            raise ValueError("Invalid browser type")
        return self.driver