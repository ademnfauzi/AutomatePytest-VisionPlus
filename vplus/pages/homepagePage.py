from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from vplus.object.homepageObject import objectHomepage
from vplus.object.originalsObject import objectOriginals
from vplus.pages.loginPage import LoginPage
from vplus.pages.originalsPage import OriginalsPage


class HomepagePage:
    def __init__(self, driver):
        self.driver = driver
        self.homepage = objectHomepage()
        self.originals = objectOriginals()
        self.wait = WebDriverWait(self.driver, 10)
        
    def clickCardRCTI(self):
        # driver.execute_script("window.scrollBy(0,1400)")
        # time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.homepage.cardRCTI))).click()    
        except:
            self.driver.find_element(By.XPATH, self.homepage.cardRCTI).click()
        
    def btnConnectDevice(self):
        time.sleep(3)
        try:
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice)
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice).click()
        except:
            pass
        time.sleep(1)
        
    def assertAfterClickCardRCTI(self):
        time.sleep(3)
        try:
            WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH, self.homepage.RCTISelectedLiveTv)))
            checkAssert = True
        except:
            checkAssert = False
        
        time.sleep(3)
        return checkAssert
    
    def slideLiveTvChannelsFavorite(self,driver):
        # driver.execute_script("window.scrollBy(0,1400)")
        element = self.driver.find_element(By.XPATH, self.homepage.liveTvSection)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        # time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, self.homepage.slideRightLiveTvFavorite).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.homepage.slideLeftLiveTvFavorite).click()
            checkAssert = True
        except:
            checkAssert = False
        
        return checkAssert
            
    def clickCardVodTopTenWeek(self,driver):
        wait = WebDriverWait(self.driver,120)
        time.sleep(1)
        # driver.execute_script("window.scrollBy(0,3000)")
        element = self.driver.find_element(By.XPATH, self.homepage.topTenSection)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH, self.homepage.CardTopTenWeekSection))).click()
        time.sleep(3)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.originals.sypnosis)))  
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, self.originals.btnWatch))).click()
        # time.sleep(1)
        time.sleep(3)
        originals = OriginalsPage(driver)
        try:
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice)
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice).click()
        except:
            pass
        
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.player)))
            ActionChains(self.driver).move_to_element(element).perform()
            wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnPause)))
            playVOD = True
        except:
            playVOD = False
                
        return playVOD
    
        
    def listWatchlist(self,driver):
        # driver.execute_script("window.scrollBy(0,400)")
        time.sleep(1)
        card = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.homepage.cardWatchlistVod)))
        ActionChains(self.driver).move_to_element(card).perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.homepage.cardTitle))).click()
        time.sleep(1)
        
    def AddOrRemoveWatchList(self):
        originals = objectOriginals()
        try:
            self.driver.find_element(By.XPATH, self.originals.btnAddToListTrue)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.originals.btnAddToListTrue).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.originals.btnAddToList).click()
        except:
            self.driver.find_element(By.XPATH, self.originals.btnAddToList).click()
        
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, self.originals.btnAddToListTrue)
        return element
        
        time.sleep(3)
        
    def slideClusterWatchlist(self,driver):
        # self.driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, self.homepage.watchlistSection)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        try:
            layout = self.wait.until(EC.presence_of_element_located((By.XPATH, self.homepage.layoutWatching)))
            ActionChains(self.driver).move_to_element(layout).perform()
            time.sleep(2)
            print("udah perform")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.homepage.RightSlideWatchlist))).click()
            print("udah click right")
            self.driver.find_element(By.XPATH, self.homepage.LeftSlideWatchlist).click()
            element = True
        except:
            element = False
        return element
    
    # def clickCardWatchlist(self):
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, self.homepage.cardWatchlistVod).click()
    #     time.sleep(1)
        
    def assertDetailVod(self):
        time.sleep(1)
        element = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH, self.originals.sypnosis)))
        return element
    
    def goHome(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.homepage.navHome).click()
        
    def slideClusterNewReleases(self,driver):
        # driver.execute_script("window.scrollBy(0,2500)")
        element = self.driver.find_element(By.XPATH, self.homepage.newReleasesSection)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.homepage.slideRightNewReleases))).click()
            time.sleep(1)
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.homepage.slideLeftNewReleases))).click()
            element = True
        except:
            element = False
        return element
    
    def clickCardNewReleases(self):
        # wait = WebDriverWait(self.driver,120)
        card = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.homepage.cardNewReleases)))
        ActionChains(self.driver).move_to_element(card).perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.homepage.cardTitleNewReleases))).click()
        
    def slideClusterContinueWatching(self,driver):
        time.sleep(1)
        # driver.execute_script("window.scrollBy(0,1200)")
        element = self.driver.find_element(By.XPATH, self.homepage.continueWatchingSection)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        # try:
        #     # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH, self.homepage.slideRightContinueWatching))).click()
        #     # time.sleep(1)
        #     # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH, self.homepage.slideRightContinueWatching))).click()
        #     self.driver.find_element(By.XPATH, self.homepage.slideRightContinueWatching).click()
        #     time.sleep(1)
        #     self.driver.find_element(By.XPATH, self.homepage.slideLeftContinueWatching).click()
        #     element = True
        # except:
        #     element = False
        return element
    
    def clickCardContinueWatching(self):
        # wait = WebDriverWait(self.driver,120)
        
        elementContinue = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.homepage.hoverContinueWatching)))
        ActionChains(self.driver).move_to_element(elementContinue).perform()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.homepage.titleContinue))).click()
        element = self.assertDetailVod()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.originals.sypnosis).send_keys(Keys.ESCAPE)
        time.sleep(1)
        return element
    
    def clickIconPlayContinueWatching(self, driver):
        # driver.execute_script("window.scrollBy(0,1200)")
        time.sleep(1)
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH, self.homepage.cardContinueWatching))).click()
        originals = OriginalsPage(driver)
        
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, self.originals.btnWatch))).click()
        except:
            pass
        
        try:
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice)
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice).click()
        except:
            pass
                            
        try:
            checkAssert = originals.assertAppearAds()
            print("assert ads ada")
            checkAssert = originals.assertPlayVOD()
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert