import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.originalsObject import objectOriginals
from vplus.object.sportObject import objectSport

class SportPage:
    def __init__(self, driver):
        self.driver = driver
        self.sport = objectSport()
        self.originals = objectOriginals()
        
    def goSport(self):
        self.driver.find_element(By.XPATH, self.sport.goSports).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.goSportsSelected)))
            checkAssert = True   
        except:
            checkAssert = False
            
        return checkAssert
    
    def backPage(self):
        self.driver.back()
        time.sleep(1)
        
    def goLiveTvSportChannels(self):
        # self.driver.execute_script("window.scrollBy(0,1000)")
        element = self.driver.find_element(By.XPATH, self.sport.txtLiveTv)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardLiveTvSoccerChannels))).click()
        time.sleep(1)
        originals = objectOriginals()
        
        try:
            print("eksekusi btncnct")
            # time.sleep(19999)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, originals.btnConnectDevice)))
            self.driver.find_element(By.XPATH, originals.btnConnectDevice).click()
            time.sleep(3)
        except:
            print("ga eksek btnconect")
            pass
        
        try:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.sport.playerLiveTv)))
            ActionChains(self.driver).move_to_element(element).perform()
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.btnPauseLiveTv)))
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.soccerChannelsSelected)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def goWatchVodSports(self):
        try:
            element = self.driver.find_element(By.XPATH, self.sport.txtCatchYourMatch)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch))).click()
        except:
            try:
                self.driver.execute_script("window.scrollBy(0,500)")
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch2))).click()
            except:
                try:
                    self.driver.execute_script("window.scrollBy(0,700)")
                    WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch3))).click()
                except:
                    try:
                        self.driver.execute_script("window.scrollBy(0,900)")
                        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch4))).click()
                    except:
                        try:
                            self.driver.execute_script("window.scrollBy(0,120)")
                            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch5))).click()
                        except:
                            print("Cluster Catch Your Match Not Found")
        
        # scroll_amount = 200
        # card_index = 1

        # Scroll and find the txtCatchYourMatch element
        # while True:
        #     try:
        #         element = self.driver.find_element(By.XPATH, self.sport.txtCatchYourMatch)
        #         self.driver.execute_script("arguments[0].scrollIntoView();", element)
        #         break
        #     except:
        #         self.driver.execute_script("window.scrollBy(0,{})".format(scroll_amount))

        # # Check for card elements sequentially and click the first one found
        # while True:
        #     try:
        #         WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch + card_index))).click()
        #         return
        #     except:
        #         self.driver.execute_script("window.scrollBy(0,{})".format(scroll_amount))
        #         card_index += 1

        #     # Reset card index to loop through card elements again after scrolling
        #     if card_index > 5:
        #         card_index = 1
        #         self.driver.execute_script("window.scrollBy(0,{})".format(scroll_amount))

        # print("Cluster Catch Your Match Not Found")
                    
        # self.driver.execute_script("window.scrollBy(0,2350)")
        # element = self.driver.find_element(By.XPATH, self.sport.txtCatchYourMatch)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(1)
        # WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch))).click()
        # # time.sleep(1)
        # try:
        #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.sport.btnWatch))).click()
        # except:
        #     pass
        
        try:
            print("eksekusi btncnct")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnConnectDevice)))
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice).click()
            time.sleep(3)
        except:
            print("ga eksek btnconect")
            pass
        
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.btnPauseVod)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert
    
    def goWatchVodSportsWithPremium(self):
        # self.driver.execute_script("window.scrollBy(0,2350)")
        # element = self.driver.find_element(By.XPATH, self.sport.txtCatchYourMatch)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # originals = objectOriginals()
        # WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch))).click()
        
        try:
            element = self.driver.find_element(By.XPATH, self.sport.txtCatchYourMatch)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch))).click()
        except:
            try:
                self.driver.execute_script("window.scrollBy(0,500)")
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch2))).click()
            except:
                try:
                    self.driver.execute_script("window.scrollBy(0,700)")
                    WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch3))).click()
                except:
                    try:
                        self.driver.execute_script("window.scrollBy(0,900)")
                        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch4))).click()
                    except:
                        try:
                            self.driver.execute_script("window.scrollBy(0,120)")
                            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.sport.cardCatchYourMatch5))).click()
                        except:
                            print("Cluster Catch Your Match Not Found")
        
        
        
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.originals.btnSubscribe))).click()
        except:
            pass
        
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.originals.popUpSubscribe)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert