class ObjectGuide:
    def __init__(self):
        self.navGuide = "(//a[contains(text(), 'Guide')])[1]"
        self.checkGuide = "//a[contains(text(), 'Guide') and @aria-current='page']"
        self.imgSportstars = "(//img[@alt='Soccer Channel'])[1]"
        self.chooseSportstars = "(//*[@id='__nuxt']/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[76]/div/div/button[@class='absolute h-full border-x-[0.5px] flex items-center overflow-hidden text-white'])[1]"
        self.imgNick = "(//img[@alt='Nick Jr'])[1]"
        self.chooseNick = "(//*[@id='__nuxt']/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[46]/div/div/button[@class='absolute h-full border-x-[0.5px] flex items-center overflow-hidden text-white'])[1]"