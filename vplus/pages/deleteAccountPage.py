import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.deleteAccountObject import objectDeleteAccount
from vplus.object.settingsObject import objectSettings

class DeleteAccount:
    def __init__(self, driver):
        self.driver = driver
        self.deleteAccount = objectDeleteAccount()
        self.settings = objectSettings()
        
    def goDeleteAccount(self):
        self.driver.find_element(By.XPATH, self.settings.iconSettings).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.settings.menuSettings))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.settings.clickConfigureDeleteAccount))).click()
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.deleteAccount.txtIUnderstand)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goDeleteAccountAfterKeepAccount(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.settings.clickConfigureDeleteAccount))).click()
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.deleteAccount.txtIUnderstand)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def keepAccount(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.deleteAccount.btnKeepAccount))).click()
        time.sleep(1)
        mainWindow = self.driver.window_handles[0]  
        self.driver.switch_to.window(mainWindow)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.settings.clickConfigureDeleteAccount)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def goToProcessDeleteAccount(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.deleteAccount.txtIUnderstand))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.deleteAccount.btnProccess))).click()
    
    def processDeleteAccount(self):
        time.sleep(10)
        # self.driver.find_element(By.XPATH, self.deleteAccount.inputPassword).send_keys('4321Lupa')
        self.driver.find_element(By.XPATH, self.deleteAccount.inputPassword).send_keys('PasswordBru1')
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.deleteAccount.btnDeletedAccount))).click()
        
        try:
            # time.sleep(100000)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.deleteAccount.txtSuccessDeleted)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    