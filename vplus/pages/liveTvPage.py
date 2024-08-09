import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from vplus.object.originalsObject import objectOriginals
from vplus.object.liveTvObject import objectTV
from vplus.object.loginObject import objectLogin
from vplus.object.settingsObject import objectSettings
from vplus.pages.loginPage import LoginPage

class TvPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        
        login = LoginPage(driver)
        # self.url = login.url

        # init class objek bagian Tv
        self.tv = objectTV()
        self.login = objectLogin()
        self.originals = objectOriginals()

    # def open(self):
    #     self.driver.get(self.url)

    def goTvPage(self):
        self.driver.find_element(By.XPATH, self.tv.navLiveTv).click()       

    def handleAds(self):
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
            # hover dulu pausenya
            # element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, self.tv.player)))
            # ActionChains(self.driver).move_to_element(element).perform()
            # kembalikan nilai true kalau ada tombol pause, brrti video diplay
            # return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv.tombolPause)))


    def managementDevice(self):
        try:
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice)
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice).click()
        except:
            pass
        
    def managementDevice2(self):
        settings = objectSettings()
        try:
            time.sleep(3)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.btnGoToSettingsMaximumDevice))).click()
            print("eksekusi max device")
            time.sleep(2)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, settings.btnDisconnectAllMManageDevice))).click()
            print('Go To Pop Up Settings For Check Device')
            time.sleep(2)
            self.driver.find_element(By.XPATH, settings.btnDisconnectAcceptModal).click()
            print("eksekusi manage device kelar")
            time.sleep(2)
            self.driver.refresh()            
        except:
            pass

    def assertTvPlay(self):
        # time.sleep(60)
        try:
            element = WebDriverWait(self.driver, 150).until(EC.presence_of_element_located((By.XPATH, self.tv.player)))
            ActionChains(self.driver).move_to_element(element).perform()
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, self.tv.tombolPause)))
            checkAssert = True
        except:
            try:
                element = WebDriverWait(self.driver, 150).until(EC.presence_of_element_located((By.XPATH, self.tv.player)))
                ActionChains(self.driver).move_to_element(element).perform()
                WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, self.tv.iconVolume)))
                checkAssert = True
            except:
                checkAssert = False
            
        return checkAssert

    def assertTvPlayEuro(self):
        # time.sleep(60)
        element = WebDriverWait(self.driver, 150).until(EC.presence_of_element_located((By.XPATH, self.tv.player)))
        ActionChains(self.driver).move_to_element(element).perform()
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.tv.iconVolume)))
            checkAssert = True
        except:
            checkAssert = False
            
        return checkAssert

#   search sportars
    def tvSearch(self, keyword): 
        inputTV = self.driver.find_element(By.XPATH, self.tv.searchTv)
        inputTV.send_keys(keyword)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.channelSportstars))).click()

    def tvSearchAny(self, keyword): 
        inputTV = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.searchTv)))
        inputTV.send_keys(keyword)
        time.sleep(1)
        inputTV.send_keys(Keys.DOWN)
        time.sleep(1)
        inputTV.send_keys(Keys.ENTER)

#   search tvn
    def tvSearchTvNmovies(self, keyword): 
        inputTV = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.searchTv)))
        inputTV.send_keys(keyword)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.channelTVNmovies))).click()
       
    def tvSearchSporstars(self, keyword): 
        inputTV = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.searchTv)))
        inputTV.send_keys(keyword)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.channelSportstars))).click()
        

    def tvCloseVideoPaused(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.closeVideoPause))).click()
        
    def checkBtnPause(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.btnPlayAfterPause))).click()
        except:
            pass

    def assertSubscribe(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.subscribe)))

    def assertValidasiSearch(self):  
        gettitle = self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.getVideo)))
        return gettitle.get_attribute('title')
    
    
    def assertTvPause(self):
        # tunggu ada button pause, lalu click
        element = WebDriverWait(self.driver, 150).until(EC.presence_of_element_located((By.XPATH, self.tv.player)))
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.tombolPause))).click()
        time.sleep(1)
        # return icon paused saat film dipause
        return self.driver.find_element(By.CSS_SELECTOR, self.tv.iconPaused)


# case untuk non login dibawah

    def non_goTvPage(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.navLiveTv))).click()
        time.sleep(2)
       

    def non_formLogin(self, username, password):
        mainWindow = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        time.sleep(2)
        print(username)
        print(password)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.formInputPhone))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.formInputPassword))).send_keys(password)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.formClickLogin))).click()
        time.sleep(2)
        # pilih karakter paling kiri 
        mainWindow = self.driver.window_handles[0]  
        self.driver.switch_to.window(mainWindow)
        time.sleep(3)

    def assertNonCanLogin(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.myProfile)))
         
    def checkFavChannels(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.txtAllChanels))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.txtDropdownFavorites))).click()
        try:
            self.managementDevice()
        except:
            pass
        
        try:
            self.WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, self.tv.txtEmptyFavorites)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.btnOK))).click()
            checkAssert = False
        except:
            checkAssert = True
            
        return checkAssert
    
    def tvSearchEuro1(self, keyword): 
        time.sleep(1)
        inputTV = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.searchTv)))
        inputTV.send_keys(keyword)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.channelEuroOne))).click()
        
    def tvSearchEuro2(self, keyword):
        time.sleep(1) 
        inputTV = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.searchTv)))
        inputTV.send_keys(keyword)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.channelEuroTwo))).click()
        
    def tvSearchEuro3(self, keyword): 
        time.sleep(1)
        inputTV = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.searchTv)))
        inputTV.send_keys(keyword)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.channelEuroThree))).click()
        
    def tvSearchEuro4(self, keyword):
        time.sleep(1) 
        inputTV = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.searchTv)))
        inputTV.send_keys(keyword)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.channelEuroFour))).click()
    
    def tvSearchEuro5(self, keyword):
        time.sleep(1) 
        inputTV = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tv.searchTv)))
        inputTV.send_keys(keyword)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tv.channelEuroFive))).click()
        
    def refresh(self):
        self.driver.refresh()