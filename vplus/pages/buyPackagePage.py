import time
import traceback
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.buyPackageObject import objectBuyPackage
import logging
import json

class BuyPackage:
    def __init__(self, driver):
        self.driver = driver
        self.buyPackage = objectBuyPackage()
        logging.basicConfig(level=logging.DEBUG)
        
    def goBuyPackage(self):
        self.driver.find_element(By.XPATH, self.buyPackage.navBuyPackage).click()
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtPremium30Days)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def choosePayment(self,package, payment, typePayment, role):
        time.sleep(1)
        if(package == 'Premium'):
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtPremium30Days))).click()   
            time.sleep(1)
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnPricePremium30Days))).click()
            except:
                print("Wrong Price or Change Price (1)")
                return False
            time.sleep(1)
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnSubscribe))).click()
            time.sleep(5)
            self.switchToPaymentTab()
            try:
                time.sleep(1)
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtPaymentPremium30Days)))
            except:
                print("Wrong Price or Change Price (2)")
                return False
            
        elif(package == 'Premium Sport'):
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtPremiumSport30Days))).click()
            time.sleep(1)
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnPricePremiumSport30Days))).click()
            except:
                print("Wrong Price or Change Price (1)")
                return False              
            time.sleep(1)
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnSubscribe))).click()
            time.sleep(5)
            self.switchToPaymentTab()
            try:
                time.sleep(1)
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtPaymentPremiumSport30Days)))
            except:
                print("Wrong Price or Change Price (2)")
                return False
        
        # time.sleep(1)
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnPrice))).click()
        # time.sleep(1)
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnSubscribe))).click()
        # time.sleep(3)
        # mainWindow = self.driver.window_handles[1]
        # self.driver.switch_to.window(mainWindow)
        
        if (payment == 'Payment'):
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.choosePayment))).click()
            result = self.RunPayment(typePayment)
            return result
        elif (payment == 'Telco Balance'):
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseTelcoBalance))).click()
            
            try:
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtProvide)))
                result = True
            except:
                result = False
                
            return result            
        elif (payment == 'Other Payment'):
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseOtherPayment))).click()
            result = self.runOtherPayment(typePayment, role)
            return result
            
    def RunPayment(self, typePayment):
        iframe = self.driver.find_element(By.XPATH, self.buyPackage.iframeChoosePayment)
        self.driver.switch_to.frame(iframe)
        
        print("Masuk Iframe")
        if (typePayment == 'BCA'):
            # time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVA))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVABCA))).click()
            try:
                # time.sleep(1)
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtVA)))
                checkAssert = True
            except:
                checkAssert = False
                
        elif (typePayment == 'BRI'):
            # time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVA))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVABRI))).click()
            try:
                # time.sleep(1)
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtVA)))
                checkAssert = True
            except:
                checkAssert = False
                
        elif (typePayment == 'BNI'):
            # time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVA))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVABNI))).click()
            try:
                # time.sleep(1)
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtVA)))
                checkAssert = True
            except:
                checkAssert = False
                
        elif (typePayment == 'Mandiri'):
            # time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVA))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVAMandiri))).click()
            try:
                # time.sleep(1)
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtVA)))
                checkAssert = True
            except:
                checkAssert = False
                
        elif (typePayment == 'Permata'):
            # time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVA))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVAPermata))).click()
            try:
                # time.sleep(1)
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtVA)))
                checkAssert = True
            except:
                checkAssert = False
                
        elif (typePayment == 'Other Bank'):
            # time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVA))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseVAOther))).click()
            try:
                # time.sleep(1)
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtVA)))
                checkAssert = True
            except:
                checkAssert = False
                
        elif (typePayment == 'Shopee Pay'):
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtShopeePay))).click()
            try:
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.imgQrCode)))
                checkAssert = True
            except:
                checkAssert = False
                
        elif (typePayment == 'Gopay'):
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseGopay))).click()
            try:
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.imgQrCode)))
                checkAssert = True
            except:
                checkAssert = False
                
        elif (typePayment == 'QRIS'):
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseQris))).click()
            try:
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.imgQrCode)))
                checkAssert = True
            except:
                checkAssert = False
        
        elif (typePayment == 'Debit Credit'):
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.chooseDebitOrKredit))).click()
            try:
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.inputCvv)))
                checkAssert = True
            except:
                checkAssert = False
        
            
        return checkAssert
    
            
    def runOtherPayment(self, typePayment, role):
        with open('vplus/testdata/dataUser.json') as json_file:
            data = json.load(json_file)
        role_data = data.get(role, [])
        if role_data:
            username = role_data[0]["username"]
            # password = role_data[0]["password"]
            print(username)   
        else:
            print("Not Have Data")
            
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.inputPhoneNumber))).send_keys(username)
        time.sleep(1)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnContinuee))).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.NicePayPage)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def resetPayment(self):
        # Switch back to the main tab without explicitly checking the title
        self.driver.switch_to.window(self.driver.window_handles[0])
        try:
            # Perform additional actions in the main tab if needed
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnPrice)))
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnPrice))).send_keys(Keys.ESCAPE)

            checkAssert = True
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            print("Belum Masuk ke Main Window Tab. Exception:", e)
            traceback.print_exc()
            checkAssert = False

        return checkAssert
    
    def goToPaymentPage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtPremiumSport30Days))).click()            
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnPrice))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnSubscribe))).click()
        time.sleep(3)
        mainWindow = self.driver.window_handles[1]
        self.driver.switch_to.window(mainWindow)
        
    def goTermAndCondtion(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.aTermAndCondition))).click()
        mainWindow = self.driver.window_handles[1]  
        self.driver.switch_to.window(mainWindow)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.termAndConditionPage))) 
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def backPage(self):
        self.driver.back()
        time.sleep(1)                       
        
    def goPrivacyAndPolicy(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.aPrivacyPolicy))).click()
        mainWindow = self.driver.window_handles[1]  
        self.driver.switch_to.window(mainWindow)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.privacyPolicyPage)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def goSoftwareLicence(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.aSoftwareLicence))).click()
        mainWindow = self.driver.window_handles[1]  
        self.driver.switch_to.window(mainWindow)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.softwareLicencePage)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def assertCheckPackageActive(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.cardSubscribePackageActive)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def checkCardPackageEuro(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.cardPackageEuro))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnPriceEuro))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.btnSubscribe))).click()
        time.sleep(3)
        mainWindow = self.driver.window_handles[1]
        self.driver.switch_to.window(mainWindow)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buyPackage.txtPaymentEuro)))
            checkAssert = True
        except:
            checkAssert = False
        
        return checkAssert
    
    def backToMainTab(self):
        mainWindow = self.driver.window_handles[0]
        self.driver.switch_to.window(mainWindow)
        
    def switchToPaymentTab(self):
        mainWindow = self.driver.window_handles[1]
        self.driver.switch_to.window(mainWindow)