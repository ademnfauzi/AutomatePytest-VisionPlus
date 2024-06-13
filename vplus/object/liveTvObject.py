class objectTV:
    def __init__(self):
        self.navLiveTv = "//span[contains(text(), 'Live TV')]"
        self.tombolPause = "//button[@class= 'md-icon-button pause md-button md-ink-ripple']"
        self.iconVolume = "//md-icon[@class='md-font material-icons icon-volume-up']"
        self.searchTv = "(//input[@aria-label ='Go to channel' and @type ='text'])[1]"
        self.getVideo = "//video[@id = 'video']"
        # iconPaused ini ada saat u udah click tombol pause, terus nnti ada iconnya yg ditengah
        self.iconPaused = "#player > div > div.player-paused.layout-align-center-center.layout-column"
        self.formInputPhone = "//input[@id='phone']"
        self.formInputPassword = "//input[@id='fld_Password']"
        self.formClickLogin = "//button[@id='btn_Login']"
        self.myProfile = "(//div[@class='profiles-container lessThanRow']//div//div//div//img)[1]"
        self.channelSportstars = "//div[@class='channel-serviceid' and text()='112']/following-sibling::div[@class='channel-name' and text()='Sportstars']"
        self.channelTVNmovies = "//div[@class='channel-serviceid' and text()='46']/following-sibling::div[@class='channel-name' and text()='TVN Movies']"
        self.subscribe = "//span[@translate=''] [text()='Subscribe']"
        self.closeVideoPause = "//button[@class= 'md-icon-button close md-button md-ink-ripple']"
        self.frameIklan = "(//iframe[@title='Advertisement'])[1]"
        self.player = "//div[@id='player']"
        self.btnSkipAds = "//div[@class='videoAdUiSkipButtonExperimentalText']"
        self.txtAdsTwo = "//div[@class='videoAdUiAttribution']"
        self.txtAllChanels = "(//span[contains(text(),'All Channels')])[1]"
        self.txtDropdownFavorites = "//span[contains(text(),'Favorites')]"
        self.txtEmptyFavorites = "//div[contains(text(),' This channel list is empty ')]"
        self.btnOK = "//span[contains(text(),'OK')]"
        self.channelEuroOne = "//div[@class='channel-serviceid' and text()='1003']/following-sibling::div[@class='channel-name' and text()='EURO 1']"
        self.channelEuroTwo = "//div[@class='channel-serviceid' and text()='1004']/following-sibling::div[@class='channel-name' and text()='EURO 2']"
        self.channelEuroThree = "//div[@class='channel-serviceid' and text()='1005']/following-sibling::div[@class='channel-name' and text()='EURO 3']"
        self.channelEuroFour = "//div[@class='channel-serviceid' and text()='1006']/following-sibling::div[@class='channel-name' and text()='EURO 4']"
        self.channelEuroFive = "//div[@class='channel-serviceid' and text()='1007']/following-sibling::div[@class='channel-name' and text()='EURO 5']"