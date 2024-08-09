from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from vplus.object.loginObject import objectLogin
from vplus.object.regisObject import objectRegister
from vplus.pages.loginPage import LoginPage
from vplus.utils.generate import Generate
from selenium.webdriver.common.keys import Keys
import time

class registerPage:
    def __init__(self, driver):
        self.driver = driver
        login = LoginPage(driver)
        # self.url = login.url
        self.wait = WebDriverWait(self.driver, 30)
        self.register = objectRegister()
        self.generate = Generate()

    # def open(self):
    #     self.driver.get(self.url)

    def goToRegister(self):
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.buttonLoginRegis))).click()
        # mainWindow = self.driver.current_window_handle  
        # for handle in self.driver.window_handles:  
        #     if handle != mainWindow:
        #         self.driver.switch_to.window(handle)
        #         break
        self.driver.switch_to.window(self.driver.window_handles[1])
        # self.driver.find_element(By.XPATH, self.register.clickRegister).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.clickRegister))).click()

    def inputFormRegis_clickRegis(self, username, password):   
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.inputPhone))).send_keys(username)      
        self.driver.find_element(By.XPATH, self.register.inputPassword).send_keys(password)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.clickSendOtp))).click()
        
        try: 
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.txtViaSMS))).click()
            print("Appear pop up whatsapp")
        except:
             print("Disappear pop up whatsapp")
             
        if password == '1234AAaa':
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.inputOTP))).send_keys(self.generate.endpointOTP("89977758355"))
            # self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTP("89977758355"))
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.register.formBtonRegister).click()   
        else:
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.inputOTP))).send_keys(self.generate.endpointOTP(username))

            # self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTP(username))
            time.sleep(3)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.register.clickRegister))).click()   
            time.sleep(5)
            
    def inputFormRegis_clickRegisWithEmail(self, username, password):   
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.halamanEmail))).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.register.inputEmail).send_keys(username)
        self.driver.find_element(By.XPATH, self.register.inputPassword).send_keys(password)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.clickSendOtp))).click()
        time.sleep(1)
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.txtViaSMS))).click()
            print("Appear pop up otp via whatsapp")
        except:
            print("Disappear pop up otp via whatsapp")
    
        if password == '1234AAaa':
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.inputOTP))).send_keys(self.generate.endpointOTP("89977758355"))
            # self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTP("89977758355"))
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.register.formBtonRegister).click()   
        else:
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.inputOTP))).send_keys(self.generate.endpointOTP(username))

            # self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTP(username))
            time.sleep(3)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.register.clickRegister))).click()   
            time.sleep(5)
    

    def inputFormRegis(self, username, password):   
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.inputPhone))).send_keys(username)      
        self.driver.find_element(By.XPATH, self.register.inputPassword).send_keys(password)
    
    def inputFormRegis_clickRegis_2menit(self, username, password):   
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.inputPhone))).send_keys(username)      
        self.driver.find_element(By.XPATH, self.register.inputPassword).send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.register.clickSendOtp).click()
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.txtViaSMS))).click()
            print("Appear pop up otp via whatsapp")
        except:
            print("Disappear pop up otp via whatsapp")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.inputOTP))).send_keys(self.generate.endpointOTP(username))   
        time.sleep(123)
        
    def inputFormRegisEmail(self, username, password):
        time.sleep(1)
        print(username)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.halamanEmail))).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.register.inputEmail).send_keys(username)
        self.driver.find_element(By.XPATH, self.register.inputPassword).send_keys(password)
        

    def clickSendOTP(self):
        self.driver.find_element(By.XPATH, self.register.clickSendOtp).click()
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.txtViaSMS))).click()
            print("Appear pop up otp via whatsapp")
        except:
            print("Disappear pop up otp via whatsapp")
        time.sleep(2)
        # self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.clickSendOtp))).click()
        # time.sleep(2)

    def clickButtonRegister(self, username):
        print(username)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.inputOTP))).send_keys(self.generate.endpointOTP(username))   
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.register.clickRegister).click()  
        time.sleep(5)  
        
    def clickButtonRegisterAfterDeleted(self, username):
        print(username)
        self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTPafterDeleted(username))
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.register.clickRegister).click()  
        time.sleep(5) 
        
    def assertInvalidEmail(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.formattEmail)))
        
    #assert sendOTP masih tag P bukan button, karena nomor/data salah jadi sendOTP ga bisadiclick
    def assertInvalidData(self):
        return self.driver.find_element(By.XPATH, self.register.clickSendOtpInactive)
    
    # assert message invalidOTP
    def assertOTPSalah(self):
        time.sleep(2)
        return self.driver.find_element(By.XPATH, self.register.messageInvalidOTP)
    
    def assertDiscoverProfile(self):
        time.sleep(5)
        login = objectLogin()
        mainWindow = self.driver.window_handles[0]  
        self.driver.switch_to.window(mainWindow)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, login.skip)))
            checkAssert = True
        except:
            print("Doesnt appear button skip")
            checkAssert = False
        
        return checkAssert

    def assertButtonRegisterDisabled(self):
        time.sleep(2)
        buttonRegister = self.driver.find_element(By.XPATH, self.register.clickRegister)
        # cek pake isenabled, kalau buttonregisnya disabled, maka kita return true, tapi kalau enable kita return false
        if buttonRegister.is_enabled():
            return True
        else:
            return False 

    def assertOTP2times(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.register.clickSendOtp).click()
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.txtViaSMS))).click()
            print("Appear pop up otp via whatsapp")
        except:
            print("Disappear pop up otp via whatsapp")
        time.sleep(2)
        enableOTP2times = self.driver.find_element(By.XPATH, self.register.txtResend)
        return enableOTP2times

    def assertAccountRegistered(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.accountRegistered)))

    def inputFormRegis_clickRegisWithEmailCheckOTP(self, username, password):   
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.halamanEmail))).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.register.inputEmail).send_keys(username)
        self.driver.find_element(By.XPATH, self.register.inputPassword).send_keys(password)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.clickSendOtp))).click()
        time.sleep(1)
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.txtViaSMS))).click()
            print("Appear pop up otp via whatsapp")
        except:
            print("Disappear pop up otp via whatsapp")        



