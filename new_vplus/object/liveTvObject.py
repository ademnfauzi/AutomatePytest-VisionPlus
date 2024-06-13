class ObjectLiveTv:
    def __init__(self):
        self.navLiveTv = "(//a[contains(text(), 'Live TV')])[1]"
        self.checkLiveTv = "//a[contains(text(), 'Live TV') and @aria-current='page']"
        self.cardRCTI = "//a[@href='/vision/livetv?channel=1']"
        self.btnPause = "(//button[@class='btn btn-ghost'])[1]"
        self.btnPauseOnCenter = "//*[@id='__nuxt']/div[2]/div[3]/div[1]/div/div/div[2]/span"
        self.upgradePayment = "//div[text()='Upgrade']"
        self.liveTvSection = "//p[contains(text(), 'Your Favorite TV Channel')]"
        self.RCTISelectedLiveTv = "//div[@class='cell-channel selected' and @id='channel-00000000000000000002']"
        self.slideRightLiveTvFavorite = "//*[@id='strip-element-7']/div[2]/div/div[2]/md-icon"
        self.slideLeftLiveTvFavorite = "//*[@id='strip-element-7']/div[2]/div/div[1]/md-icon"
        self.frameIklan = "(//iframe[@title='Advertisement'])[1]"
        self.btnSkipAds = "//div[@class='videoAdUiSkipButtonExperimentalText']"
        self.txtAdsTwo = "//div[@class='videoAdUiAttribution']"
        self.objOutsideNuxt = "//div[@class='h-full absolute w-full flex items-center justify-center inset-0 text-white']"
        