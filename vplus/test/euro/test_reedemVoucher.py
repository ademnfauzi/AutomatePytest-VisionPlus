# from vplus.pages.liveTvPage import TvPage
# from vplus.pages.loginPage import LoginPage
# from vplus.pages.originalsPage import OriginalsPage
# from vplus.pages.programGuidePage import PageProgramGuide
# from vplus.pages.regisPage import registerPage
# from vplus.pages.transactionHistoryPage import TransactionHistory
# from vplus.pages.voucherPage import VoucherPage
# from vplus.utils.generate import Generate
# from vplus.utils.setup import SetupDriver
# from vplus.testdata.hash import encodeDecodePassword
# from vplus.test.general.user import users
# from vplus.utils.setup import platform
# import pytest
# import json


# @pytest.fixture(scope="module")
# def driver(platform):
#     setup_driver = SetupDriver(browser=platform)
#     yield setup_driver.get_driver()
#     setup_driver.driver.quit()

# def test_login(driver):
#     register = registerPage(driver)
#     hashPassword = encodeDecodePassword()
#     generate = Generate()
#     # register.open()
#     register.goToRegister()
#     with open("vplus/testdata/dataUser.json") as json_file:
#         data = json.load(json_file)
#     password = data["FreeUser"][0]["password"]
#     stringDecode = hashPassword.decode(password)
#     # stringDecode = "PasswordBru1"
#     username = generate.numberRandom()
#     print(username)
#     register.inputFormRegis_clickRegis(username, stringDecode)
#     assert register.assertDiscoverProfile()
#     users.setUsername(username)
#     login = LoginPage(driver)
#     login.skipCreateAvatar()


# def test_goVoucherPage(driver):
#     voucher = VoucherPage(driver)
#     assert voucher.goVoucher()


# def test_inputValidCodeVoucher(driver):
#     voucher = VoucherPage(driver)
#     inputVoucher = "testingRKZ0DKDN1ZUauto"
#     assert voucher.inputSuccessVoucher(inputVoucher)


# def test_checkBuyPackageAfterReedemVoucher(driver):
#     voucher = VoucherPage(driver)
#     trsHistory = TransactionHistory(driver)
#     assert voucher.checkBuyPackageActive()
#     trsHistory.goTransactionHistory()
#     trsHistory.openSuccessTab()
#     assert trsHistory.openDetailCardSuccess()
#     trsHistory.backPage()


# def test_checkWatchPremiumLiveTv(driver):
#     voucher = VoucherPage(driver)
#     tv = TvPage(driver)
#     program = PageProgramGuide(driver)
#     originals = OriginalsPage(driver)
#     voucher.backToTabMain()
#     originals.refresh()
#     program.clickNavProgramGuidance()
#     assert program.checkLiveTvPremium()
#     assert tv.assertTvPlay()


# def test_checkWatchEuroOneLiveTv(driver):
#     voucher = VoucherPage(driver)
#     tv = TvPage(driver)
#     tv.goTvPage()
#     tv.tvSearchEuro1("EURO 1")
#     assert tv.assertTvPlayEuro()


# def test_checkWatchEuroTwoLiveTv(driver):
#     voucher = VoucherPage(driver)
#     tv = TvPage(driver)
#     tv.tvSearchEuro2("EURO 2")
#     assert tv.assertTvPlayEuro()
    
# def test_checkWatchEuroThreeLiveTv(driver):
#     voucher = VoucherPage(driver)
#     tv = TvPage(driver)
#     tv.tvSearchEuro3("EURO 3")
#     assert tv.assertTvPlayEuro()
    
# def test_checkWatchEuroFourLiveTv(driver):
#     voucher = VoucherPage(driver)
#     tv = TvPage(driver)
#     tv.tvSearchEuro4("EURO 4")
#     assert tv.assertTvPlayEuro()
    
# # def test_checkWatchEuroFiveLiveTv(driver):
# #     voucher = VoucherPage(driver)
# #     tv = TvPage(driver)
# #     tv.tvSearchEuro5("EURO 5")
# #     assert tv.assertTvPlayEuro()


# def test_checkWatchOtherSportsLiveTv(driver):
#     voucher = VoucherPage(driver)
#     tv = TvPage(driver)
#     tv.tvSearch("SPORTSTARS")
#     assert tv.assertSubscribe()


# def test_checkPremiumVodAfterReedemVoucher(driver):
#     originals = OriginalsPage(driver)
#     originals.goOriginals()
#     originals.clickCardVODOriginals()
#     originals.clickEpsThree()
#     originals.clickButtonWatch()
#     assert originals.assertPlayVOD()


# def test_logout(driver):
#     originals = OriginalsPage(driver)
#     login = LoginPage(driver)
#     originals.backPage()
#     originals.backPage()
#     login.upScroll()
#     login.logout()
#     assert login.assertLogout()
