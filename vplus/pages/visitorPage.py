import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.buyPackageObject import objectBuyPackage
from vplus.object.downloadObject import objectDownload
from vplus.object.homepageObject import objectHomepage
from vplus.object.liveTvObject import objectTV
from vplus.object.loginObject import objectLogin
from vplus.object.originalsObject import objectOriginals
from vplus.object.programGuideObject import objectProgramGuide
from vplus.object.settingsObject import objectSettings
from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import SetupDriver

class VisitorPage:
    def __init__(self, driver):
        self.driver = driver
        self.settings = objectSettings()
        self.login = objectLogin()
        self.homepage = objectHomepage()
        self.originals = objectOriginals()
        self.download = objectDownload()
        self.buyPackage = objectBuyPackage()
        self.program = objectProgramGuide()
        self.tv = objectTV()
        self.wait = WebDriverWait(self.driver, 10)
    
    def assertLoginPage(self):
        time.sleep(1)
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.login.form_inputPhone)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.login.form_inputPassword)))
            checkAssert = True
        except:
            checkAssert = False
            
        time.sleep(1)
        return checkAssert
    
    def backToMainTab(self):
        mainWindow = self.driver.window_handles[0]  
        self.driver.switch_to.window(mainWindow)
        
    def goToLogin(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.login.buttonLoginRegis))).click()
        
    def goIconSettings(self):
        self.driver.find_element(By.XPATH, self.settings.iconSettings2).click()
        
    def goMyDownloads(self):
        self.driver.find_element(By.XPATH, self.download.goMyDownloads).click()
    
    def goBuyPackage(self):
        self.driver.find_element(By.XPATH, self.buyPackage.navBuyPackage).click()
        
    def goIconProfile(self):
        self.driver.find_element(By.XPATH, self.homepage.iconProfileAvatar).click()
        
    def goLiveTV(self):
        self.driver.find_element(By.XPATH, self.tv.navLiveTv).click()

    def goOpenDetailProgramGuide(self):
        self.driver.find_element(By.XPATH, self.program.navbarProgramGUidance).click()
        time.sleep(1)
        card = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.program.cardTransTvCurrent))).click()
    
        
    def goOpenDetail(self):
        self.driver.find_element(By.XPATH, self.originals.navOriginals).click()
        # element = self.driver.find_element(By.XPATH, self.originals.loveStoriesText)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(1)
        # card = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.originals.cardLoveStories)))
        # ActionChains(self.driver).move_to_element(card).perform()
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.originals.titleCardLoveStories))).click()
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,800)")
        card = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.originals.cardOriginals)))
        ActionChains(self.driver).move_to_element(card).perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.originals.titleCardOriginals))).click()
        
    def clickButtonWatch(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnWatch2))).click()
        
    def clickIconLike(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnLike))).click()
        
    def clickIconUnLike(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnUnLike))).click()
        
    def clickIconAddToList(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnAddToList))).click()
        
    def clickIconShare(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnShare))).click()
        
    def goToHome(self):
        # time.sleep(1)
        # login = LoginPage(self.driver)
        # url = login.url     
        # self.driver.get(url)
        # time.sleep(3)
        
        time.sleep(1)
        setup_driver = SetupDriver(browser=None)
        url = setup_driver.url()
        self.driver.get(url)
        time.sleep(3)