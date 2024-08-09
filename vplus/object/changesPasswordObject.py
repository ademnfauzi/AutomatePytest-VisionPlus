class ObjectChangePassword:
    def __init__(self):
        self.clickIconSettings = "//button[@class='md-icon-button settings-button md-button md-ink-ripple']"
        self.clickSettings = "//button[@id='open-settings-button']"
        self.clickConfigureChange = "(//span[@translate=''] [text()='Configure'])[1]"
        self.inputCurrentPW = "//input[@name = 'password']"
        self.inputnewPW = "//input[@name = 'newPassword']"
        self.next = "//div[contains(text(), 'Next')]"
        self.assertSuccessChange = "//label[text() ='Password Succesfully Changed']"
        self.assertInvalidPassword = "//p[text() = 'Invalid password']"
        self.assertPasswordSame = "//p[text() = 'New password must be different from the current password.']"
        self.buttonOkInvalid = "//button[text() = ' OK ']"
        self.configureDevice = "(//span[@translate=''] [text()='Configure'])[5]"