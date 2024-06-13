# from pages.loginPage import LoginPage
# from pages.chooseProfilePage import ChooseProfile
# from pages.homepagePage import HomepagePage
# from pages.originalsPage import OriginalsPage
# from utils.setup import SetupDriver
# from testdata.hash import encodeDecodePassword
# import pytest
# import json

# @pytest.fixture(scope="module")
# def driver():
#     setup_driver = SetupDriver()
#     yield setup_driver.driver
#     setup_driver.driver.quit()

# def test_start(driver):
#     login = LoginPage(driver)
#     role = "FreeUser"
#     login.loginProcess(driver, role)

# def test_slideFavoriteChannelsLiveTv(driver):
#     homepage = HomepagePage(driver)
#     originals = OriginalsPage(driver)
#     originals.handleMaximumDevice()
#     homepage.slideLiveTvChannelsFavorite(driver)
    
# def test_listLiveTvHomepage(driver):
#     homepage = HomepagePage(driver)
#     homepage.clickCardRCTI()
#     assert homepage.assertAfterClickCardRCTI()