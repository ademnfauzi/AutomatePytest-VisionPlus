from vplus.object.addProfileObject import ObjectAddProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

from vplus.object.favoriteChannelsObject import ObjectFavoriteChannels


class FavoriteChannelsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.favChannels = ObjectFavoriteChannels()
        self.addProfile = ObjectAddProfile()

    def clickIconSettings(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.clickIconSettings))).click()

    def clickSettings(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.clickSettings))).click()

    def clickConfigureProfile(self):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.addProfile.clickConfigureAddProfile))).click()
    
    def clickProfile(self):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.favChannels.iconProfile))).click()
        
    def clickConfigureFavChannels(self):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.favChannels.btnConfigureFavoriteChannels))).click()
        
    def clickAnyCardToAddFavChannels(self, channels):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.favChannels.fieldSearchChannels))).send_keys(channels)
        time.sleep(1)
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.favChannels.cardLeftNotSelected))).click()
        except:
            print("Card Channels has selected")
            
        time.sleep(1)
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.favChannels.cardLeftSelected)))
            checkAssert = True
        except:
            print("Card Channels has not selected")
            checkAssert = False
            
        return checkAssert
    
    def clickButtonSave(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.favChannels.btnSave))).click()
        time.sleep(1)
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.favChannels.txtChangesSaved)))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.favChannels.btnOK))).click()
            checkAssert = True
        except:
            print("Not Success Save")
            checkAssert = False
            
        return checkAssert
        
    def clickButtonCancel(self):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.favChannels.btnCancel))).click()
        time.sleep(1)
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.favChannels.btnConfigureFavoriteChannels)))
            checkAssert = True
        except:
            print("Not Success Cancel")
            checkAssert = False
            
        return checkAssert
    
    def refresh(self):
        self.driver.refresh()
        
    def clickAnyCardToRemoveFavChannels(self, channels):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.favChannels.fieldSearchChannels))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.favChannels.fieldSearchChannels))).send_keys(channels)
        time.sleep(1)
        
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.favChannels.cardLeftSelected))).click()
        except:
            print("Card Channels has not selected")
            
        time.sleep(1)
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.favChannels.cardLeftNotSelected)))
            checkAssert = True
        except:
            print("Card Channels has not selected")
            checkAssert = False
            
        return checkAssert
    
    def removeInputSearchChannels(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.favChannels.fieldSearchChannels)))
        element.send_keys(Keys.COMMAND + 'a')
        time.sleep(1)
        element.send_keys(Keys.DELETE)