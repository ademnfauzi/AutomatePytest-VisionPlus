class objectSport:
    def __init__(self):
        self.goSports = "//span[contains(text(),'Sports')]"
        self.goSportsSelected = "//li[@class='md-nav-item selected' and @name='Sports']"
        self.cardLiveTvSoccerChannels = "//*[@id='scroll-surface-2']/div[1]/node-snapshot/div/div[3]"
        self.soccerChannelsSelected = "//div[@id='channel-00000000000000000115' and @class='cell-channel selected']"
        self.btnPauseLiveTv = "//button[@class='md-icon-button pause md-button md-ink-ripple']"
        self.cardCatchYourMatch = "//*[@id='scroll-surface-6']/div[1]/node-snapshot/div/div[3]"
        self.txtCatchYourMatch = "//div[contains(text(),'Catch Your Match')]"
        self.txtLiveTv = "//div[contains(text(),'Live TV Sports Channels')]"
        self.btnWatch = "//button[@aria-label='Watch']"
        self.btnPauseVod = "//button[@aria-label='Pause']"
        self.playerLiveTv = "//div[@id='player']"