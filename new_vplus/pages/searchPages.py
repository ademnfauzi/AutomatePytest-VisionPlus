from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from new_vplus.object.searchObject import ObjectSearch
import time

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search = ObjectSearch()
        self.wait = WebDriverWait(self.driver, 10)

    def refreshThePageAfterLogin(self):
        self.driver.get("https://app.visionplus.id/visionqa/home")
        
    def clikIconSearch(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.search.iconSearch))).click()

    def inputSearch(self,keyword):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.search.inputSearch))).send_keys(keyword)
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.search.cardResultSearch)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
                    
    def deleteInputSearch(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.search.inputSearch)))
        element.send_keys(Keys.COMMAND + 'a')
        time.sleep(1)
        element.send_keys(Keys.DELETE)
        
    def clickCardResultsearch(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.search.cardResultSearch))).click()