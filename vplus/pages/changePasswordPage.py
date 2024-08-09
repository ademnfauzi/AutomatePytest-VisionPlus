from vplus.object.changesPasswordObject import ObjectChangePassword
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys


class ChangesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.changes = ObjectChangePassword()

    def clickIconSettings(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.changes.clickIconSettings))).click()

    def clickSettings(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.changes.clickSettings))).click()

    def clickConfigure(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.changes.clickConfigureChange))).click()

    def inputFormCHangePW(self, passwordLama, passwordBaru):
        time.sleep(2)
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.changes.inputCurrentPW))).send_keys(passwordLama)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.changes.inputnewPW))).send_keys(passwordBaru)
        time.sleep(1)

    def inputFormCHangePWWithoutSwitch(self, passwordLama, passwordBaru):
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.changes.inputCurrentPW))).send_keys(passwordLama)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.changes.inputnewPW))).send_keys(passwordBaru)
        time.sleep(1)

    def removeInput(self):
        inputCurrent = self.driver.find_element(By.XPATH, self.changes.inputCurrentPW)
        time.sleep(1)
        inputCurrent.send_keys(Keys.BACKSPACE * 8)
    
    def removeInputRenewPW(self):
        inputRenew = self.driver.find_element(By.XPATH, self.changes.inputnewPW)
        time.sleep(1)
        inputRenew.send_keys(Keys.BACKSPACE * 8)

    def closePopUp(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.changes.buttonOkInvalid))).click()

    def clickChange(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.changes.next))).click()

    def assertSuccessChangePW(self):
        time.sleep(2)
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.changes.assertSuccessChange)))
  
    def assertPasswordSame(self):
        time.sleep(2)
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.changes.assertPasswordSame)))
 
    def assertPasswordInvalid(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.changes.assertInvalidPassword)))