class ObjectFavoriteChannels:
    def __init__(self):
        self.btnConfigureFavoriteChannels = "(//span[@translate=''] [text()='Configure'])[6]"
        self.cardLeftNotSelected = "(//md-grid-list/md-grid-tile[1]/figure/div/div[2])[1]"
        self.cardLeftSelected = "//md-dialog-content[@class='md-padding fav-channels-list']/md-grid-list/md-grid-tile[@class='item item-channel background-checked'][1]"
        self.fieldSearchChannels = "//input[@placeholder='Go to channel']"
        self.btnCancel = "//span[contains(text(),'Cancel')]"
        self.btnSave = "//span[contains(text(),'Save')]"
        self.btnOK = "//span[contains(text(),'OK')]"
        self.txtChangesSaved = "//div[contains(text(),'Changes saved')]"
        self.iconProfile = "//md-dialog-content/div/div/img"
        self.txtSportstars = "(//div[contains(text(),'Sportstars')])[1]"
        self.txtTransTv = "(//div[contains(text(),'Trans TV')])[1]"
        self.txtRCTI = "(//div[contains(text(),'RCTI')])[1]"