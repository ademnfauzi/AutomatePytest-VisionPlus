import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.buyPackageObject import objectBuyPackage
from vplus.object.settingsObject import objectSettings
from vplus.object.voucherObject import objectVoucher

class VoucherPage:
    def __init__(self, driver):
        self.driver = driver
        self.voucher = objectVoucher()
        self.buyPackage = objectBuyPackage()
        self.settings = objectSettings()
        
    def goVoucher(self):
        self.driver.find_element(By.XPATH, self.settings.iconSettings).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.goVoucher))).click()
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.voucher.inputVoucherId)))
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.voucher.btnReedem)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def inputInvalidVoucher(self,voucher):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.inputVoucherId))).send_keys(voucher)
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.btnReedem))).click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.txtErrorMessageInputVoucher)))
            checkAssert = True            
        except:
            checkAssert = False        
            
        return checkAssert
    
    def inputUniqVoucher(self,voucher):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.inputVoucherId))).send_keys(voucher)
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.btnReedem))).click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.txtHasBeenReedemed)))
            checkAssert = True            
        except:
            checkAssert = False        
            
        return checkAssert
    
    def inputExpiredVoucher(self,voucher):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.inputVoucherId))).send_keys(voucher)
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.btnReedem))).click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.txtVoucherHasExpired)))
            checkAssert = True            
        except:
            checkAssert = False        
            
        return checkAssert
    
            
    def clearInputVoucher(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.inputVoucherId)))
        element.send_keys(Keys.COMMAND + 'a')
        time.sleep(1)
        element.send_keys(Keys.DELETE)
        
    def inputSuccessVoucher(self,voucher):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.inputVoucherId))).send_keys(voucher)
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.btnReedem))).click()        
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.btnSeeMyStatus))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.txtPaymentSuccess)))
            checkAssert = True            
        except:
            checkAssert = False
            
        return checkAssert
    
    def checkBuyPackageActive(self):
        self.backToTabMain()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.navBuyPackage))).click()        
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.cardSubscribePackageActive)))
            checkAssert = True            
        except:
            checkAssert = False
            
        return checkAssert
    
    def backPage(self):
        self.driver.back()
        time.sleep(1)
        
    def goHelpCenter(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.aHelpCenter))).click()        
        time.sleep(1)
        try:
            # time.sleep(3)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.txtDiscoverWhatNew)))
            checkAssert = True            
        except:
            checkAssert = False
            
        return checkAssert
    
    def goTokopedia(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.aTokopedia))).click()        
        time.sleep(1)
        mainWindow = self.driver.window_handles[2]  
        self.driver.switch_to.window(mainWindow)
        try:
            # time.sleep(3)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.tokpedPageVision)))
            checkAssert = True            
        except:
            checkAssert = False
            
        return checkAssert
    
    def goLazada(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.aLazada))).click()        
        time.sleep(1)
        mainWindow = self.driver.window_handles[2]  
        self.driver.switch_to.window(mainWindow)
        # time.sleep(5)
        try:
            # time.sleep(3)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.lazadaPageVision)))
            checkAssert = True            
        except:            
            try:
                # time.sleep(3)
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.iframeLazada)))
                checkAssert = True            
            except:
                checkAssert = False
            
            
        return checkAssert
    
    def goBlibi(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.aBlibi))).click()        
        time.sleep(1)
        mainWindow = self.driver.window_handles[2]  
        self.driver.switch_to.window(mainWindow)
        # time.sleep(5)
        
        try:
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.txtBlibiChatSeller)))
            checkAssert = True
            print("Appear chat seller")
        except:
            try:
                time.sleep(3)
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.voucher.blibiPageVision)))
                checkAssert = True     
                print("Appear title shop")       
            except:
                print("Disappear")       
                checkAssert = False
            
        return checkAssert
    
    def goCoda(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.voucher.aCodashop))).click()        
        time.sleep(1)
        mainWindow = self.driver.window_handles[2]  
        self.driver.switch_to.window(mainWindow)
        # time.sleep(5)
        try:
            # time.sleep(3)
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.voucher.codashopPageVision)))
            checkAssert = True            
        except:
            checkAssert = False
            
        return checkAssert
    
    def backToTabVoucher(self):
        mainWindow = self.driver.window_handles[1]  
        self.driver.switch_to.window(mainWindow)
        
    def backToTabMain(self):
        mainWindow = self.driver.window_handles[0]  
        self.driver.switch_to.window(mainWindow)