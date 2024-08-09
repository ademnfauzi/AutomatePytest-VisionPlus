import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from new_vplus.object.chooseProfile import ObjectChooseProfile
from new_vplus.object.loginObject import ObjectLogin

class ChooseProfileProfile:
    def __init__(self, driver):
        self.driver = driver

    def chooseProfileAfterLogin(self):
        mainWindow = self.driver.window_handles[0]
        self.driver.switch_to.window(mainWindow)
        wait = WebDriverWait(self.driver, 10)
        
        profile = ObjectChooseProfile()
        # time.sleep(3)
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, profile.checkedProfileFalse)))           
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, profile.checkedProfileFalse))).click()
        except:
            pass
        
        # time.sleep(1)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, profile.imgChooseProfile))).click()
        # time.sleep(1)
        
    def chooseProfileAfterLogin(self):
        mainWindow = self.driver.window_handles[0]
        self.driver.switch_to.window(mainWindow)
        wait = WebDriverWait(self.driver, 10)
        
        profile = ObjectChooseProfile()
        # time.sleep(3)
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, profile.checkedProfileFalse)))           
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, profile.checkedProfileFalse))).click()
        except:
            pass
        
        # time.sleep(1)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, profile.imgChooseProfile2))).click()
        # time.sleep(1)
            
    def assertChooseProfile(self):
        # time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        # profile = objectChooseProfile()
        login = ObjectLogin()
        try:
            # wait.until(EC.presence_of_element_located((By.XPATH, profile.imgChooseProfile)))
            wait.until(EC.presence_of_element_located((By.XPATH, login.buttonLogin)))
            checkAssert = False
        except:
            checkAssert = True
        
        return checkAssert