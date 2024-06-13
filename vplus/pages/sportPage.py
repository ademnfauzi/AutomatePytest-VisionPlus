import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.originalsObject import objectOriginals
from vplus.object.sportObject import objectSport

class SportPage:
    def __init__(self, driver):
        self.driver = driver
        self.sport = objectSport()
        
    def goSport(self):
        self.driver.find_element(By.XPATH, self.sport.goSports).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.goSportsSelected)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def backPage(self):
        self.driver.back()
        time.sleep(1)
        
    def goLiveTvSportChannels(self):
        # self.driver.execute_script("window.scrollBy(0,1000)")
        element = self.driver.find_element(By.XPATH, self.sport.txtLiveTv)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardLiveTvSoccerChannels))).click()
        time.sleep(1)
        originals = objectOriginals()
        
        try:
            print("eksekusi btncnct")
            # time.sleep(19999)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, originals.btnConnectDevice)))
            self.driver.find_element(By.XPATH, originals.btnConnectDevice).click()
            time.sleep(3)
        except:
            print("ga eksek btnconect")
            pass
        
        try:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.sport.playerLiveTv)))
            ActionChains(self.driver).move_to_element(element).perform()
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.btnPauseLiveTv)))
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.soccerChannelsSelected)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def goWatchVodSports(self):
        # self.driver.execute_script("window.scrollBy(0,2350)")
        element = self.driver.find_element(By.XPATH, self.sport.txtCatchYourMatch)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch))).click()
        # time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.sport.btnWatch))).click()
        except:
            pass
        
        try:
            print("eksekusi btncnct")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnConnectDevice)))
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice).click()
            time.sleep(3)
        except:
            print("ga eksek btnconect")
            pass
        
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.btnPauseVod)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def goWatchVodSportsWithPremium(self):
        # self.driver.execute_script("window.scrollBy(0,2350)")
        element = self.driver.find_element(By.XPATH, self.sport.txtCatchYourMatch)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        originals = objectOriginals()
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch))).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, originals.btnSubscribe))).click()
        except:
            pass
        
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, originals.popUpSubscribe)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert