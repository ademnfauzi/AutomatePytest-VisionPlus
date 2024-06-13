from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from vplus.object.programGuideObject import objectProgramGuide
from vplus.object.settingsObject import objectSettings

class NotificationPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.settings = objectSettings()

    def goToNotification(self):
        self.driver.find_element(By.XPATH, self.settings.iconSettings).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.settings.goNotifications).click()
        
    def assertNotification(self):
        # time.sleep(2)
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.settings.popUpNotifications)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert