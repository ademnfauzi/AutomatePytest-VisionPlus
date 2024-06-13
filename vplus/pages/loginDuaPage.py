import time
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vplus.object.loginDuaObject import objectLoginDua


class LoginDuaPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.visionplus.id'
        self.wait = WebDriverWait(self.driver, 10)
        
        self.login = objectLoginDua()
        
    def open(self):
        self.driver.get(self.url)
        
    def clickButtonLogin(self):
        self.driver.find_element(By.XPATH, self.login.buttonLoginRegis).click()