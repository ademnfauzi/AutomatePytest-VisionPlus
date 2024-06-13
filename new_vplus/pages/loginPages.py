from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from new_vplus.object.loginObject import ObjectLogin
from new_vplus.testdata.hash import encodeDecodePassword
from new_vplus.object.settingsObject import ObjectSettings
import json

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.login = ObjectLogin()
        self.settings = ObjectSettings()
            
    # ke halaman page login
    def goToLogin(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.login.buttonLogin))).click()
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break

    def inputFormLoginHP(self, username, password):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login.form_inputPhone).send_keys(username)
        self.driver.find_element(By.XPATH, self.login.form_inputPassword).send_keys(password)
    
    def inputFormEmail(self, username, password):
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.login.formEmail))).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login.form_inputEmail).send_keys(username)
        self.driver.find_element(By.XPATH, self.login.form_inputPassword).send_keys(password)
        time.sleep(1)


    def clickButtonLogin(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login.form_buttonLogin))).click()
        time.sleep(3)
    
    # buat sukses case, dari click button login regis, input sampe click login lagi
    def clickLogin(self, username, password):
        print(username)
        print(password)
        self.driver.find_element(By.XPATH, self.login.buttonLogin).click()
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.login.form_inputPhone).send_keys(username)
        self.driver.find_element(By.XPATH, self.login.form_inputPassword).send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login.form_buttonLogin).click()
        # wait ganti element
        time.sleep(5)
       
       
    def inputFormLogin(self, username, password):
        mainWindow = self.driver.window_handles[1]  
        self.driver.switch_to.window(mainWindow)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.login.form_inputPhone).send_keys(username)
        self.driver.find_element(By.XPATH, self.login.form_inputPassword).send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login.form_buttonLogin).click()
        # wait ganti element
        time.sleep(5)

    def assertInccorectFormat(self):
        return self.driver.find_element(By.XPATH, self.login.inccorectEmailFormat)
    
    def assertButtonLoginDisabled(self):
        buttonLogin = self.driver.find_element(By.XPATH, self.login.form_buttonLogin)
        if buttonLogin.is_enabled():
            return True
        else:
            return False
    
    def assertLoginUnregistered(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.login.popLoginUnregistered)))

    def assertWrongPassword(self):
        return self.driver.find_element(By.XPATH, self.login.popWrongPW)


    def loginProcess(self, driver, role):
        print(role)
        hashPassword = encodeDecodePassword()
        # self.open()
        with open('new_vplus/testdata/dataUser.json') as json_file:
            data = json.load(json_file)

        role_data = data.get(role, [])
        if role_data:
            username = role_data[0]["username"]
            password = role_data[0]["password"]
            print(username)
            print(password)
            
            stringDecode = hashPassword.decode(password)
            print(stringDecode)
            
            self.clickLogin(username, stringDecode)
        #     self.assertSuccessLogin()
            
        #     profile = ObjectChooseProfile(driver)
        #     assert profile.assertChooseProfile()
            
        # else:
        #     print(f"Role '{role}' not found in the dataUser.json file")
        #     assert False
            
    def loginProcessWithEmail(self, driver, role):
        print(role)
        hashPassword = encodeDecodePassword()
        # self.open()
        with open('new_vplus/testdata/dataUser.json') as json_file:
            data = json.load(json_file)

        role_data = data.get(role, [])
        if role_data:
            username = role_data[0]["username"]
            password = role_data[0]["password"]
            print(username)
            print(password)
            
            stringDecode = hashPassword.decode(password)
            print(stringDecode)
            
            self.goToLogin()
            self.inputFormEmail(username,stringDecode)
            self.clickButtonLogin()
            
            # profile = ObjectChooseProfile(driver)
            # profile.chooseProfileAfterLogin2()
            
            wait = WebDriverWait(self.driver, 5)
            # profile = objectChooseProfile()
            login = ObjectLogin()
            try:
                # wait.until(EC.presence_of_element_located((By.XPATH, profile.imgChooseProfile)))
                wait.until(EC.presence_of_element_located((By.XPATH, login.buttonLogin)))
                checkAssert = False
            except:
                checkAssert = True
            
            return checkAssert
            
        else:
            print(f"Role '{role}' not found in the dataUser.json file")
            # assert False
            return False

    def logout(self):
        time.sleep(3)
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, self.settings.iconSettings))).click()
        self.driver.find_element(By.XPATH, self.settings.iconSettings).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.settings.btnLogout).click()
        
    def assertLogout(self):
        time.sleep(3) 
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.login.buttonLogin)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def upScroll(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, -1000);")
    
    def assertSuccessLogin(self):
        time.sleep(3) 
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.login.buttonLoginRegis)))
            checkAssert = False
        except:
            checkAssert = True
        
        self.driver.refresh()      
            
        return checkAssert