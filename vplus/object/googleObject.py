class objectGoogle:
    def __init__(self):
        self.inputEmail = "//input[@id='identifierId']"
        self.btnNext = "//span[contains(text(),'Next')]"
        self.checkboxRecaptcha = "//*[@id='recaptcha-anchor'']"
        self.inputPassword = "//*[@id='password']/div[1]/div/div[1]/input"
        self.txtSimplyYourSignIn = "//span[contains(text(),'Simplify your sign-in')]"
        self.btnNotNow = "//span[contains(text(),'Not now')]"
        self.txtMore = "//span[contains(text(),'More')]"
        self.listEmail = "(/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div[8]/div/div[1]/div[2]/div/table/tbody/tr)[1]"
        self.txtTitleEmail = "(//*[contains(text(),'Verify your account to start enjoying Vision+')])[4]"