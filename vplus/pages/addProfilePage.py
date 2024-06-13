from vplus.object.addProfileObject import ObjectAddProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from selenium.webdriver.common.keys import Keys


class AddProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.addProfile = ObjectAddProfile()

    def clickIconSettings(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.clickIconSettings))).click()

    def clickSettings(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.clickSettings))).click()

    def clickConfigure(self):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.clickConfigureAddProfile))).click()

    def clickAddProfile(self):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.clickAddProfile))).click()

    def clickImage(self):
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.addProfile.clickImage))).click()

    def chooseAvatar(self):
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.addProfile.avatarNenek))).click()

    def clickDoneAvatar(self):
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.addProfile.clickDone))).click()

    def inputNewAvatar(self):
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.addProfile.inputProfileName))).send_keys("NewAvatar")

    def clickOK(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.clickOK))).click()
        time.sleep(2)

    def deleteAvatar(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.buttonDelete))).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.acceptDelete))).click()
        time.sleep(1)

    def assertSuccessCreateAvatar(self):
        return self.driver.find_element(By.XPATH, self.addProfile.buttonDelete)

    def assertSuccessDeleteAvatar(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.txtAvatarName)))
            checkAssert = False
        except:
            checkAssert = True
            
        return checkAssert