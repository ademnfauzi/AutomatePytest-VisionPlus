from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.pinObject import ObjectPin
from vplus.object.changesPasswordObject import ObjectChangePassword
import time

class PagePin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.pin = ObjectPin()
        self.changes = ObjectChangePassword()

    def clickIconSettings(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.changes.clickIconSettings))).click()

    def clickSettings(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.changes.clickSettings))).click()

    def enablePin(self):
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.togglePin))).click()
        togglee = self.driver.find_element(By.XPATH, self.pin.togglePin)
        checkbox_attribute = togglee.get_attribute('aria-checked')
        if checkbox_attribute == 'true':
            print("ketemu 1")
            return True
            # pass
        else:
            print("gk ketemu 1")
            return False

    def disablePin(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.togglePin))).click()
        togglee = self.driver.find_element(By.XPATH, self.pin.togglePin)
        checkbox_attribute = togglee.get_attribute('aria-checked')
        if checkbox_attribute == 'false':
            # pass
            print("ketemu 2")
            return True
        else:
            print("gak ketemu 2")
            return False
        
    def chooseProfile(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.imgProfileOne))).click()
        
    def householdPINToPay(self):
        element = self.driver.find_element(By.XPATH, self.pin.txtHousheholdPINToPay)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        
        
    def enablePinToPay(self):
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.togglePinToPay))).click()
        togglee = self.driver.find_element(By.XPATH, self.pin.togglePinToPay)
        checkbox_attribute = togglee.get_attribute('aria-checked')
        if checkbox_attribute == 'true':
            print("ketemu")
            return True
            # pass
        else:
            print("gk ketemu")
            return False

    def disablePinToPay(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.togglePinToPay))).click()
        togglee = self.driver.find_element(By.XPATH, self.pin.togglePinToPay)
        checkbox_attribute = togglee.get_attribute('aria-checked')
        if checkbox_attribute == 'false':
            # pass
            return True
        else:
            return False
    
    def changePin(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.buttonEditPin))).click()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.inputFieldPin))).send_keys("0000")
        self.driver.find_element(By.XPATH, self.pin.buttonOKPin).click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.inputFieldPin))).send_keys("0000")
        self.driver.find_element(By.XPATH, self.pin.buttonOKPin).click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.inputFieldPin))).send_keys("0000")
        self.driver.find_element(By.XPATH, self.pin.buttonOKPin).click()
        try:
            time.sleep(3)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.buttonOKPin)))
            return False
        except:
            return True

    def clickOptionDownload(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1500)")
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.optionDownload))).click()
        
    def click720p(self):
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.option720p))).click()
        time.sleep(2)
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.option720p))).click()
            return True
        except:
            return False

    def clickNavBuyPackage(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pin.buyPackage).click()

    def clickBuyPackage(self):
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.package365))).click()
    
    def clickButtonBuy(self):
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.button365))).click()

    def confirmBuyPinWrong(self):
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.inputFieldPin))).send_keys("1221")
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.buttonSubscribe))).click()
        try:
            # time.sleep(5)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.pin.txtWrongPinToast)))
            # self.WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.pin.txtToastTop)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert


    def confirmBuyPinCorrectPin(self):
        time.sleep(1)
        inputfield = self.driver.find_element(By.XPATH, self.pin.inputFieldPin)
        inputfield.send_keys(Keys.BACKSPACE * 8)
        time.sleep(1)
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.inputFieldPin))).send_keys("0000")
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pin.buttonSubscribe))).click()
        try:
            time.sleep(5)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.pin.txtWrongPinToast)))
            # self.WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.pin.txtToastTop)))
            checkAssert = False
        except:
            checkAssert = True
            
        return checkAssert
