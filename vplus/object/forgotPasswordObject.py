class ObjectForgotPassword:
    def __init__(self):
        self.buttonForgotPassword = "//*[contains(text(), 'Forgot Password? ')]"
        self.buttonSavePassword = "//p[contains(text(), 'Save Password')]"
        self.inputPhone = "//input[@name= 'phone']"
        self.inputPassword = "//input[@id= 'fld_Password']"
        self.inputOTP = "//input[@class= 'otp-input']"
        self.sendOTP = "//button[@id= 'button-send']"
        self.buttonLogin = "//span[contains(text(), 'Log in/Register')]"
        self.iconHide = "//div[@class='relative']//button"