class objectDeleteAccount:
    def __init__(self):
        self.txtIUnderstand = "//label[contains(text(),'I understand the information and I want to delete my account')]"
        self.btnKeepAccount = "//div[contains(text(),'Keep Account')]"
        self.btnProccess = "//div[contains(text(),'Proceed to Delete Account')]"
        self.btnProcessDisabled = "//button[@class='bg-black border border-[#073634] text-[#073634] w-full p-2.5 rounded-[5px] font-medium mt-6 2xl:h-14']/div[contains(text(),'Proceed to Delete Account')]"
        self.inputPassword = "//input[@name='password']"
        self.btnDeletedAccount = "//div[contains(text(),'Delete Account')]"
        self.btnDeletedAccountDisabled = "//button[@class='bg-[#07E3D0] text-black disabled:bg-[#073634] disabled:text-[#00625E] w-full p-2.5 rounded-[5px] font-medium mt-6 2xl:h-14 -mb-4']/div[contains(text(),'Deleted Account')]"
        self.iconOpenPassword = "//img[@alt='visibility']"
        self.txtInvalidPassword = "//p[contains(text(),'Invalid password')]"
        self.txtSuccessDeleted = "//*[contains(text(),'Your account is deleted')]"
        self.btnOK = "//div[contains(text(),'OK')]"
        