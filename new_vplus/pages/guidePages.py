from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from new_vplus.object.guideObject import ObjectGuide
import time

class GuidePage:
    def __init__(self, driver):
        self.driver = driver
        self.guide = ObjectGuide()
        self.wait = WebDriverWait(self.driver, 10)
        
    def goGuide(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.guide.navGuide))).click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.guide.checkGuide))).click()
            checkAssert = True
        except:
            checkAssert = False
        
        return checkAssert
    
    def scrollToNick(self):
        xpath = self.guide.imgNick
        self.scrollUntilFindElement(xpath)
        
    def scrollToSportstars(self):
        xpath = self.guide.imgSportstars
        self.scrollUntilFindElement(xpath)
    
    def scrollUntilFindElement(self, xpath):
        try:
            # Initialize ActionChains
            actions = ActionChains(self.driver)
            # Scroll until the element is found
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            # Use JavaScript to scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return True
        except:
            return False
        
    def clickSportstars(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.guide.chooseSportstars))).click()
        
    def clickNick(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.guide.chooseNick))).click()