from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from new_vplus.object.downloadObject import ObjectDownload
from new_vplus.object.originialsObject import ObjectOriginals
from new_vplus.object.settingsObject import ObjectSettings
from new_vplus.pages.loginPages import LoginPage


class OriginalsPage:
    def __init__(self, driver):
        self.driver = driver
        self.originals = ObjectOriginals()
        self.settings = ObjectSettings()
        self.wait = WebDriverWait(self.driver, 10)
        
    def goOriginals(self):
        self.driver.find_element(By.XPATH, self.originals.navOriginals).click()
        
    def assertGoOriginals(self):
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, self.originals.sectionComingSoon)
        element.click()
        return element

    def clickCluster(self):
        self.driver.find_element(By.XPATH, self.originals.slideRightCluster).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.originals.slideLeftCluster).click()
            
    def assertClickCluster(self):
        originals = ObjectOriginals()
        wait = WebDriverWait(self.driver, 10)
        try:
            self.wait.untill(EC.presence_of_element_located((By.XPATH, originals.slideRightCluster)))
            checkAssert = False
        except:
            checkAssert = True
        
        return checkAssert
            
    def clickCardVODOriginalsPremium(self):
        # homepage = objectHomepage()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.originals.iconSearch).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.originals.inputSearch).send_keys('Pengejar Angin')
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.originals.cardResultSearch).click()
        time.sleep(1)
            
    
    def assertClickPackagePremium(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.originals.premium30DaysFromPopUpSubscribe).click()
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, self.originals.btnPricePackage)
        return element
        
    
    def clickCardVODOriginals(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,800)")
        card = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.originals.cardOriginals)))
        ActionChains(self.driver).move_to_element(card).perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.originals.titleCardOriginals))).click()
        
    def assertClickCardVOD(self):
        try:
            self.driver.find_element(By.XPATH, self.originals.sypnosis)
            checkAssert = True
        except:
            checkAssert = False
        
        return checkAssert
        
    def redirectToHome(self):
        time.sleep(1)
        login = LoginPage(self.driver)
        url = login.url     
        self.driver.get(url)
        time.sleep(5)
        
    def assertClosePopUpVOD(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        originals = ObjectOriginals()
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, originals.btnWatch)))
            checkAssert = False
        except:
            checkAssert = True
        return checkAssert

# manajement device
    def clickButtonWatch(self):
        settings = ObjectSettings()
        time.sleep(1)
        # time.sleep(599)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.btnWatch))).click()
        # time.sleep(500)
        
        try:
            print("coba ekseks manage device")
            self.manageMaximumDevice()
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnWatch))).click()

        except:
            print("ga ekseks max device")
            pass
        
        try:
            print("eksekusi btncnct")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnConnectDevice)))
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice).click()
            time.sleep(1)


        except:
            print("ga eksek btnconect")
            pass
            
        time.sleep(2)

    def handlePopUpWatch(self):
        try:
            print("coba ekseks manage device")
            self.manageMaximumDevice()
            time.sleep(2)
            self.clickResultAfterSearch()  

        except:
            print("ga ekseks max device")
            pass
        
        try:
            print("eksekusi btncnct")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnConnectDevice)))
            self.driver.find_element(By.XPATH, self.originals.btnConnectDevice).click()
            self.driver.find_element(By.XPATH, self.originals.cardResultSearch).click()

            time.sleep(3)


        except:
            print("ga eksek btnconect")
            pass
            
        time.sleep(3)
     

        
    def clickButtonSubscribe(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.originals.btnSubscribe).click()
        time.sleep(3)
        
    def assertPlayVOD(self):
        print("eksekusiPlayVOD")
        wait = WebDriverWait(self.driver,100)
        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, self.originals.player)))
            ActionChains(self.driver).move_to_element(element).perform()
            wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.btnPause)))
            # print('element ditemukan')
            playVOD = True
        except:
            playVOD = False
        return playVOD
        
    def scroll1500(self):
        self.driver.execute_script("window.scrollBy(0, 1500);")

    def assertPauseVOD(self):
        wait = WebDriverWait(self.driver, 100)
        originals = ObjectOriginals()
        time.sleep(2)        
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.player)))
            ActionChains(self.driver).move_to_element(element).perform()
            wait.until(EC.element_to_be_clickable((By.XPATH, originals.btnPauseVideo))).click()
            checkAssert = True
        except:
            checkAssert = False
        return checkAssert
      
    def skipAds(self):
        time.sleep(5)
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.originals.frameAds)))
        print("masuk ke frame")
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.originals.buttonSkipAds))).click()
            print("coba buat clickskipads")
        except:
            print("ga click clickskipads")
            time.sleep(40)
        finally:
            self.driver.switch_to.default_content()
            

    def assertAppearAds(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 30)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, self.originals.iFrameAds)))
            print("ketemu framenya")
            self.skipAds()
            frameIklan = True
        except:
            print("Disappear Iframe Ads")
            frameIklan = False
            
        return frameIklan
        
    

    def assertNoAds(self):
        time.sleep(3)
        originals = ObjectOriginals()
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, self.originals.timeAds)))
            # kalau ada iklan dia false
            frameIklan = False
        except:
            # kalau g ada true, soale sports
            frameIklan = True
        return frameIklan
        
        
    def clickEpsThree(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.originals.cardEpsThree).click()
        time.sleep(5)
        
    def clickEpsTwo(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.originals.cardEpsTwo).click()
        time.sleep(5)
    
    def assertPopUpSubscribe(self):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.originals.popUpSubscribe)        
        return element
    
    def addToList(self):
        time.sleep(1)
        originals = ObjectOriginals()
        try:
            self.driver.find_element(By.XPATH, self.originals.btnAddToListTrue)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.originals.btnAddToListTrue).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.originals.btnAddToList).click()
        except:
            self.driver.find_element(By.XPATH, self.originals.btnAddToList).click()
        
        time.sleep(3)
        
    def assertAddToList(self):
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, self.originals.btnAddToListTrue)        
        return element
    
    def clickLike(self):
        time.sleep(1)
        originals = ObjectOriginals()
        try:
            self.driver.find_element(By.XPATH, originals.btnLikeTrue)
            time.sleep(2)
            self.driver.find_element(By.XPATH, originals.btnLikeTrue).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, originals.btnLike).click()
        except:
            self.driver.find_element(By.XPATH, originals.btnLike).click()
        
        time.sleep(3)
        
    def assertClickLike(self):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.originals.btnLikeTrue)        
        return element
    
    def clickUnLike(self):
        time.sleep(1)
        originals = ObjectOriginals()
        try:
            self.driver.find_element(By.XPATH, originals.btnUnLikeTrue)
            time.sleep(2)
            self.driver.find_element(By.XPATH, originals.btnUnLikeTrue).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, originals.btnUnLike).click()
        except:
            self.driver.find_element(By.XPATH, originals.btnUnLike).click()
            
    def assertClickUnLike(self):
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, self.originals.btnUnLikeTrue)        
        return element
    
    def clickShare(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.originals.btnShare).click()
    
    def assertClickShare(self):
        time.sleep(3)
        try:
            self.driver.find_element(By.XPATH, self.originals.btnFacebook)        
            element = True
            time.sleep(1)
            # self.wait.until(EC.presence_of_element_located((By.XPATH, self.originals.btnShare))).click()
        except:
            element = False
        return element
    
    def clickTrailler(self):
        time.sleep(1)
        originals = ObjectOriginals()
        self.driver.find_element(By.XPATH, originals.btnUnLike).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, originals.btnTrailer).click()
        # time.sleep(10)
        
    def assertTrailler(self):
        # time.sleep(10)
        time.sleep(3)
        wait = WebDriverWait(self.driver,120)
        originals = ObjectOriginals()                
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='end flex-nogrow']/span")))
        span_value = element.text

        if ':' in span_value:

            time_parts = span_value.split(':')

            # Check if the time_parts list has three elements
            if len(time_parts) == 3:
                time_delta = timedelta(hours=int(time_parts[0]), minutes=int(time_parts[1]), seconds=int(time_parts[2]))

                # Check if the time is more than 3 minutes
                if time_delta > timedelta(minutes=3):
                    print("More than 3 Minutes")
                    playVOD = False
                else:
                    print("Less than 3 Minutes")
                    playVOD = True
            else:
                print("Invalid time format")
                playVOD = False
        else:
            print("Invalid time format")
            playVOD = False

        return playVOD
    
    def manageMaximumDevice(self):
        settings = ObjectOriginals()
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

       
    def clickResultAfterSearch(self):  
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.cardResultSearch))).click()
 
    def handleMaximumDevice(self):
        settings = ObjectSettings()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.change.clickIconSettings))).click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.change.clickSettings))).click()
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.change.configureDevice))).click()
        time.sleep(1)
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, settings.btnDisconnectAllMManageDevice)))
            time.sleep(1)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, settings.btnDisconnectAllMManageDevice))).click()
            time.sleep(1)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, settings.btnDisconnectAcceptModal))).click()
            time.sleep(2)
        except:
            pass
        self.driver.refresh()
        
    def downloadsVod(self):
        download = ObjectDownload()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.originals.btnDownload))).click()
        time.sleep(1)
        
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.originals.btnCancelDownload)))
            checkAssert = True
        except:
            pass
        
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.originals.btnCancelDownload)))
            checkAssert = True
        except:
            checkAssert = False
        
        return checkAssert
        
    def backPage(self):
        self.driver.back()
        
    def refresh(self):
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)

    def clickNavOriginals(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.navOriginals))).click()
        # wait page load
        time.sleep(2)
    
    def clickCardOriginalsFirst(self):
        # dapetin card pertama originals
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.originals.cardIntoView)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # modifikasi attribute hidden dihilangkan
        hover = self.driver.find_element(By.XPATH, self.originals.cardOriginalsFirst)
        time.sleep(2)
        self.driver.execute_script("arguments[0].classList.remove('hidden')", hover)
        time.sleep(1)  

        # Verifikasi atribut 'hidden' sudah dihapus
        is_hidden = hover.get_attribute('hidden')
        if is_hidden is None:
            print("Atribut 'hidden' berhasil dihapus.")
        else:
            print("Atribut 'hidden' masih ada, nilai:", is_hidden)

        hover.click()

    def clickButtonWatch(self):
        # load modal
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.buttonWatch))).click()

    def assertOriginalsPlaying(self):
        # page load
        time.sleep(3)
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.buttonPause)))
            # self.driver.find_element(By.XPATH, self.originals.buttonPause)
            return True
        except:
            return False
        

    def clickPause(self):
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.originals.buttonPause)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.buttonPause))).click()
        
    def clickEpisode3(self):
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.clickEpisode3))).click()

    def assertUpgrade(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.textUpgrade)))
            return True
        except:
            return False
        
    def assertPlaying(self):
        # wait page load
        time.sleep(2)
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.originals.tvIsPlaying)))
            return True
        except:
            return False
