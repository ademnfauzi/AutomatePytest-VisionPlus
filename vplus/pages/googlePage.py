import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from vplus.object.googleObject import objectGoogle
import json

from vplus.object.loginObject import objectLogin
from vplus.object.regisObject import objectRegister


class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        # self.urlSignInGoogle = 'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2F%3Fptid%3D19027681%26ptt%3D8%26fpts%3D0&ec=futura_hpp_co_si_001_p&ifkv=AS5LTAQOuWIWiEEw8Nn4FDfaoL9vtyHrtx-rr8WQOmy38w6u6Pyzwbgzeg89xkRc1MbWByI-RKqGuw&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1526908146%3A1719979218405549&ddm=0'
        # self.urlGmail = 'https://mail.google.com/mail/u/0/#inbox'
        self.wait = WebDriverWait(self.driver, 30)
        self.google = objectGoogle()
        self.login = objectLogin()
        self.register = objectRegister()
        
    def openNewTabSignInGoogle(self):
        # self.driver.switch_to.window(self.driver.window_handles[0])
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.login.buttonLoginRegis)))
        element.send_keys(Keys.COMMAND + 't')
        time.sleep(1)
        element.send_keys(self.urlSignInGoogle)
        
    def loginGoogle(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.google.inputEmail))).send_keys('visionplustesting@gmail.com')
        # time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.google.btnNext))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.google.inputPassword))).send_keys('4321Lupa')
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.google.btnNext))).click()
        time.sleep(5)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.google.txtMore)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def checkEmail(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.google.listEmail))).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.google.txtTitleEmail)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert