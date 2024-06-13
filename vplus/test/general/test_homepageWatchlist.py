# from pages.loginPage import LoginPage
# from pages.chooseProfilePage import ChooseProfile
# from pages.homepagePage import HomepagePage
# from pages.liveTvPage import TvPage
# from pages.originalsPage import OriginalsPage
# from utils.setup import SetupDriver
# from testdata.hash import encodeDecodePassword
# import pytest
# import json
# Because Intermittent for xpath
# @pytest.fixture(scope="module")
# def driver():
#     setup_driver = SetupDriver()
#     yield setup_driver.driver
#     setup_driver.driver.quit()

# def test_start(driver):
#     login = LoginPage(driver)
#     role = "FreeUser"
#     login.loginProcess(driver, role)
    
# def test_slideClusterWatchlist(driver):
#     homepage = HomepagePage(driver)
#     assert homepage.slideClusterWatchlist(driver)
    
# def test_detailWatchlistVod(driver):
#     homepage = HomepagePage(driver)
#     tv = TvPage(driver)
#     originals = OriginalsPage(driver)
#     homepage.listWatchlist(driver)
#     assert homepage.AddOrRemoveWatchList()
#     assert homepage.assertDetailVod()
#     originals.clickButtonWatch()
#     assert originals.assertAppearAds()
#     assert originals.assertPlayVOD()
    