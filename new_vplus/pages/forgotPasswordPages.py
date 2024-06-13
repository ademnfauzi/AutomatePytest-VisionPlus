from new_vplus.object.forgotPasswordObject import ForgotPasswordPage
from new_vplus.pages.loginPages import NewLoginObject
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.login = NewLoginObject()
        self.forgot = ForgotPasswordPage()

    def goToLoginPage(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login.buttonLogin))).click()
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        # mainWindow = self.driver.window_handles[1]  
        # self.driver.switch_to.window(mainWindow)

    def clickForgotPassword(self):
        time.sleep(3)
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.forgot.buttonForgotPassword))).click()
        self.driver.find_element(By.XPATH, self.forgot.buttonForgotPassword).click()
        # time.sleep(1000)

    def inputForm(self, username, password):
        print(username)
        print(password)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.forgot.inputPhone))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.forgot.inputPassword))).send_keys(password)
        time.sleep(1)

    def deletePhone(self):
        phoneElement = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.forgot.inputPassword)))
        phoneElement.send_keys(Keys.BACKSPACE * 8)
        time.sleep(3)

    def clickUnhide(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.forgot.iconHide))).click()

    def clickSendOTP(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.forgot.sendOTP))).click()

    def inputOTP(self, codeOTP):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.forgot.inputOTP))).send_keys(codeOTP)    
        
    def assertSuccessForgotPassword(self):
        time.sleep(10)
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.forgot.buttonSavePassword)))       
            checkAssert = False
        except:
            checkAssert = True
        return checkAssert

    def clickSaveForgotPassword(self):
        time.sleep(1)
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.forgot.buttonSavePassword))).click()
        self.driver.find_element(By.XPATH, self.forgot.buttonSavePassword).click()
        time.sleep(3)

    def assertSaveRegisterDisabled(self):
        saveRegister = self.wait.until(EC.presence_of_element_located((By.XPATH, self.forgot.buttonSavePassword)))
        if saveRegister.is_enabled():
            result = True
        else:
            result = False
        return result