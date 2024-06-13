class ObjectRegistrasi:
    def __init__(self):
        self.clickRegister = "//p[contains(text(), 'Register')]"
        self.inputPhone = "//input[@id='phone']"
        self.inputPassword = "//input[@id='fld_Password']"
        self.inputEmail = "//input[@id='fld_Email']"
        self.clickSendOtp = "//button[contains(text(), 'Send OTP')]"
        self.txtResend = "//p[contains(text(), 'Resend in ')]"
        self.clickSendOtpInactive = "//p[contains(text(), 'Send OTP')]"
        self.inputOTP = "(//input[@class='otp-input'])[1]"
        self.formBtonRegister = "//p[contains(text(), 'Register')]"
        self.buttonLoginRegis = "//button[text() = 'LOG IN']"
        self.messageInvalidOTP = "//p[contains(text(), 'Wrong OTP code')]"
        self.discoverProfile = "//span[contains(text(), 'Discover profiles')]"
        self.accountRegistered = "//h3[contains(text(), 'This account has been registered')]"
        self.halamanEmail = "//p[contains(text(), 'Email')]"
        self.formattEmail = "//p[contains(text(), 'Invalid email')]"
    