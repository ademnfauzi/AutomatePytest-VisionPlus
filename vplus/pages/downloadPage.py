import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.downloadObject import objectDownload
from vplus.pages.loginPage import LoginPage

class DownloadPage:
    def __init__(self, driver):
        self.driver = driver
        self.download = objectDownload()
        
    def goMyDownload(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.download.goMyDownloads).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.download.txtItems)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def backPage(self):
        self.driver.back()
        time.sleep(1)
    
    def cardCheckDownloadsVod(self):
        time.sleep(5)
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.download.txtNoDownloads)))
            checkAssert = False
        except:
            checkAssert = True
            
        return checkAssert