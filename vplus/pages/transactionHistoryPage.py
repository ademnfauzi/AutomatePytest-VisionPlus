import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.buyPackageObject import objectBuyPackage
from vplus.object.settingsObject import objectSettings
from vplus.object.transactionHistoryObject import objectTransactionHistory

class TransactionHistory:
    def __init__(self, driver):
        self.driver = driver
        self.buyPackage = objectBuyPackage()
        self.settings = objectSettings()
        self.transactionHistory = objectTransactionHistory()

        
    def goTransactionHistory(self):
        self.driver.find_element(By.XPATH, self.settings.iconSettings).click()
        time.sleep(1)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.settings.goTransactionHistory))).click() 
        self.driver.switch_to.window(self.driver.window_handles[1])
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.failedTab)))
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.pendingTab)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def openPendingTab(self):
        time.sleep(3)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.pendingTab))).click()
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.statusPending))).click()
            checkAssert = True
        except:
            checkAssert = False
        return checkAssert
    
    def openDetailCardPending(self): 
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.cardPending))).click()
        
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.txtVerifyPending)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def openFailedTab(self):
        time.sleep(3)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.failedTab))).click()
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.statusFailed))).click()
            checkAssert = True
        except:
            checkAssert = False
        return checkAssert
            
            
    def openDetailCardFailed(self): 
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.cardFailed))).click()
        
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.txtPaymentFailed)))
            checkAssert = True   
        except:
            checkAssert = False

        return checkAssert
    
    def openSuccessTab(self):
        time.sleep(3)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.successTab))).click() 
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.statusSuccess))).click()
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def openDetailCardSuccess(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.cardSuccess))).click()
        
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.txtPaymentSuccess)))
            checkAssert = True   
        except:
            checkAssert = False

        return checkAssert
    
    def backPage(self):
        self.driver.back()
        time.sleep(1)
        # self.driver.execute_script("window.history.back()")

        
    def openButtonMore(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.threePoint))).click()
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.btnHelpCenter)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def closeButtonMore(self):
        time.sleep(1)
        for _ in range(10):
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()        
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.btnBuyAgain)))
            checkAssert = False
        except:
            checkAssert = True
            
        return checkAssert
    
    def clickBuyAgain(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.btnBuyAgain))).click()
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.txtPayment)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def clickHelpCenter(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.btnHelpCenter))).click()
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.transactionHistory.txtGetInTouchWithUs)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert