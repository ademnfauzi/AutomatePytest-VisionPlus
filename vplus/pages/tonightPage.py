import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.tonightObject import objectTonight

class TonightPage:
    def __init__(self, driver):
        self.driver = driver
        self.tonight = objectTonight()
        
    def goTonight(self):
        self.driver.find_element(By.XPATH, self.tonight.goTonight).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navAll)))
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navAllActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goTabFilms(self):
        self.driver.find_element(By.XPATH, self.tonight.navFilms).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navFilmsActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goTabSports(self):
        self.driver.find_element(By.XPATH, self.tonight.navSports).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navSportsActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goTabNews(self):
        self.driver.find_element(By.XPATH, self.tonight.navNews).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navNewsActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goTabChildren(self):
        self.driver.find_element(By.XPATH, self.tonight.navChildren).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navChildrenActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goTabSeriess(self):
        self.driver.find_element(By.XPATH, self.tonight.navSeries).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navSeries)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goTabEntertainment(self):
        self.driver.find_element(By.XPATH, self.tonight.navEntertainment).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navEntertainmentActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goTabCulture(self):
        self.driver.find_element(By.XPATH, self.tonight.navCulture).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navCultureActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goTabMusic(self):
        self.driver.find_element(By.XPATH, self.tonight.navMusic).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navMusicActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goTabAll(self):
        self.driver.find_element(By.XPATH, self.tonight.navAll).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.navAllActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goFilterByProgress(self):
        self.driver.find_element(By.XPATH, self.tonight.selectFilter).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.filterProgressActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goFilterByChannels(self):
        # self.driver.find_element(By.XPATH, self.tonight.selectFilter).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.tonight.filterChannels).click()
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.selectFilter))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.filterChannelsActive)))
            checkAssert = True   
            # WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.filterChannelsActive))).click()
        except:
            checkAssert = False
            
        return checkAssert
    
    def goFilterByAlphabets(self):
        # self.driver.find_element(By.XPATH, self.tonight.selectFilter).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.tonight.filterAlphabet).click()
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.selectFilter))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tonight.filterAlphabetActive)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert