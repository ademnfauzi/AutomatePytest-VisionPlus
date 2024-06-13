from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from vplus.object.originalsObject import objectOriginals
from vplus.object.programGuideObject import objectProgramGuide

class PageProgramGuide:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.program = objectProgramGuide()
        self.originals = objectOriginals()

    def clickNavProgramGuidance(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.program.navbarProgramGUidance))).click()

    def clickDropdownChannel(self):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.program.opsiChannel))).click()
        time.sleep(1)

    def clickDropdownFavorites(self):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.program.ddFavorites))).click()
        time.sleep(1)
    
    def clickDropdownDate(self):
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.opsiDate))).click()
        time.sleep(1)

    def goToFavorites(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddFavorites))).click()

    def unloveRcti(self):
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.clickLoveFav))).click()
    
    def goToNationalTV(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddNasionalTV))).click()

    def loveRcti(self):
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.clickLove))).click()
        time.sleep(20)

    def assertNoYesterday(self):
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.program.textyesterday)
        #   karena dia expected kaga ada
            return False
        except:
            return True

    def assertDropdownDatePremium(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.oneDayBefore)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.twoDayBefore)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.threeDayBefore)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.fourDayBefore)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.fiveDayBefore)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.sixDayBefore)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.today)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.oneDayAfter)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.twoDayAfter)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.threeDayAfter)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.fourDayAfter)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.fiveDayBefore)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.sixDayAfter)))
        return True

    def assertDropdownAllchannels(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.dropdownAllchannel)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddFavorites)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddEntertainment)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddNews)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddKnowledge)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddKids)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddMovies)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddKnowledge)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddSports)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddMusic)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddReligion)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddLifestyle)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.program.ddNasionalTV)))
        return True
    
    def checkLiveTvPremium(self):
        time.sleep(1)
        card = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.program.cardTransTvCurrent))).click()
        time.sleep(1)
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.btnWatch)))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnWatch))).click()
            checkAssert = True
        except:
            checkAssert = False
        return checkAssert        