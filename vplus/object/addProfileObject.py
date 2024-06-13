class ObjectAddProfile:
    def __init__(self):
        self.clickIconSettings = "//button[@class='md-icon-button settings-button md-button md-ink-ripple']"
        self.clickSettings = "//button[@id='open-settings-button']"
        self.clickConfigureAddProfile = "(//span[@translate=''] [text()='Configure'])[4]"
        self.clickAddProfile = "//span[@translate=''][text()= 'Add profile']"
        self.clickDone = "//button[@data-cy='change-avatar-button']"
        self.inputProfileName = "//input[@data-cy='profile-name']"
        self.clickOK = "//button[@class= 'md-button md-ink-ripple ok-button']"
        self.clickImage= "//div[@class='avatar' and @role= 'button']/img"
        self.avatarNenek= "//img[@src='https://www.visionplus.id/images/profile/avatar/avatar_9.png']"
        self.buttonDelete = "//button[@data-cy='delete-profile']"
        self.acceptDelete= "//button[@data-cy='modal-accept']"
        self.txtAvatarName = "//span[contains(text(),'NewAvatar')]"
