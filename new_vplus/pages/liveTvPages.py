from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from new_vplus.object.liveTvObject import ObjectLiveTv
import time


class LiveTvPage:
    def __init__(self, driver):
        self.driver = driver
        self.tv = ObjectLiveTv()
        self.wait = WebDriverWait(self.driver, 10)
        
    def goLiveTv(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.tv.navLiveTv))).click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.tv.checkLiveTv))).click()
            checkAssert = True
        except:
            checkAssert = False
        
        return checkAssert

    def clickButtonPause(self):
        try:
            # Hover over the Live TV element
            self.hoverLiveTv()

            # Wait for the pause button to be present
            pause_button = self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.btnPause)))
            
            # Scroll the pause button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", pause_button)
            
            # Use JavaScript to click the pause button
            self.driver.execute_script("arguments[0].click();", pause_button)
            
            # Ensure the pause action was successful
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.btnPauseOnCenter)))
            
            return True
        except Exception as e:
            print(f"Error in clickButtonPause: {e}")
            return False



        
    def clickCardRCTI(self):
        # driver.execute_script("window.scrollBy(0,1400)")
        # time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.tv.cardRCTI))).click()    
        except:
            self.driver.find_element(By.XPATH, self.tv.cardRCTI).click()
        
    # def btnConnectDevice(self):
    #     time.sleep(3)
    #     try:
    #         self.driver.find_element(By.XPATH, self.originals.btnConnectDevice)
    #         self.driver.find_element(By.XPATH, self.originals.btnConnectDevice).click()
    #     except:
    #         pass
    #     time.sleep(1)
    
    def hoverLiveTv(self):
        card = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.tv.objOutsideNuxt)))
        ActionChains(self.driver).move_to_element(card).perform()
        
    def assertAfterClickCardPlaying(self):
        self.hoverLiveTv()
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH, self.tv.btnPause)))
            checkAssert = True
        except:
            checkAssert = False
        return checkAssert
    
    def assertUpgradepayment(self):
        time.sleep(1)
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH, self.tv.upgradePayment)))
            checkAssert = True
        except:
            checkAssert = False
        return checkAssert
    
    def handleAds(self):
        time.sleep(1)
        try:
            iframe_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.tv.frameIklan)))
            try:
                # Switch to the iframe
                self.driver.switch_to.frame(iframe_element)
                # Perform actions within the iframe
                try:
                    time.sleep(7)
                    element_inside_iframe = self.driver.find_element(By.XPATH, self.tv.btnSkipAds)
                    # element_inside_iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.tv.btnSkipAds)))
                    element_inside_iframe.click()
                    print("Click Skip ads one")
                    try:
                        time.sleep(7)
                        element_inside_iframe = self.driver.find_element(By.XPATH, self.tv.btnSkipAds)
                        element_inside_iframe.click()
                        print("Click Skip ads two")
                    except:
                        print("Doenst appear skip ads two")
                        
                    self.driver.switch_to.default_content()
                except:
                    print('No skip ads button, just pass')
                    self.driver.switch_to.default_content()
                    time.sleep(120)
                    pass

            except:
                print("Gaada skip ads")
                self.driver.switch_to.default_content()
                time.sleep(120)
                pass

            return iframe_element
        
        except:
            print("ga ad iklan, eksekusi script dibawah")
            return False
        
        
    def checkAdsForPremium(self):
        time.sleep(1)
        try:
            iframe_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.tv.frameIklan)))
            try:
                # Switch to the iframe
                self.driver.switch_to.frame(iframe_element)
                # Perform actions within the iframe
                try:
                    time.sleep(7)
                    element_inside_iframe = self.driver.find_element(By.XPATH, self.tv.btnSkipAds)
                    # element_inside_iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.tv.btnSkipAds)))
                    element_inside_iframe.click()
                    print("Click Skip ads one")
                    try:
                        time.sleep(7)
                        element_inside_iframe = self.driver.find_element(By.XPATH, self.tv.btnSkipAds)
                        element_inside_iframe.click()
                        print("Click Skip ads two")
                    except:
                        print("Doenst appear skip ads two")
                        
                    self.driver.switch_to.default_content()
                except:
                    print('No skip ads button, just pass')
                    self.driver.switch_to.default_content()
                    time.sleep(120)
                    pass

            except:
                print("Gaada skip ads")
                self.driver.switch_to.default_content()
                time.sleep(120)
                pass

            return iframe_element, False
        
        except:
            print("ga ad iklan, eksekusi script dibawah")
            return True