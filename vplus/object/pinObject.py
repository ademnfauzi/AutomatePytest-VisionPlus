class ObjectPin:
    def __init__(self):
        self.togglePin = "//md-switch[@aria-label= 'Request PIN to create profiles']"
        self.buttonEditPin = "//span[@translate='' and text() = 'Edit']"
        self.buttonOKPin = "//span[@translate='' and text() = 'OK']"
        self.toastSuccessChangePIN = "//*[contains(text),'      Household PIN changed successfully    ']"
        self.buttonSubscribe = "//span[text() = 'Subscribe']"
        self.txtWrongPinToast = "//*[contains(text(),' Wrong household PIN. Please, try again ')]"
        self.txtToastTop = "//body[@class='md-dialog-is-showing md-toast-open-top']"
        self.inputFieldPin = "//input[@id = 'pin']"
        self.optionDownload = "//md-select[@class='selector ng-pristine ng-untouched ng-valid md-auto-horizontal-margin ng-empty']"
        self.option720p = "(//span[text()= '720p'])[1]"
        self.buyPackage = "//span[text() = 'Buy Package']"
        self.package365 = "//div[text() = 'Premium Sports 30 Days']"
        self.button365 = "//button[@class= 'md-raised md-accent md-button md-ink-ripple']"
        self.imgProfileOne = "(//div/div[@data-cy='profile-settings-item'][1]/img)[1]"
        self.txtHousheholdPINToPay = "//*[@contains(text(),'Household PIN to pay']"
        self.togglePinToPay = "//md-switch[@aria-label= 'Secure mode']"
        
      