class ObjectChooseProfile:
    def __init__(self):
        self.imgChooseProfile = "(//div[@class='profiles-container lessThanRow']//div//div//div//img)[1]"
        self.imgChooseProfile2 = "(//div[@class='profiles-container']//div//div//div//img)[1]"
        self.buttonLoginRegis = "//span[contains(text(), 'Log in/Register')]"
        self.checkedProfileFalse = "//md-switch[@aria-checked='false']"