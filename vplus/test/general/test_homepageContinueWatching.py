# from pages.loginPage import LoginPage
# from pages.chooseProfilePage import ChooseProfile
# from pages.homepagePage import HomepagePage
# from pages.originalsPage import OriginalsPage
# from utils.setup import SetupDriver
# from testdata.hash import encodeDecodePassword
# from pages.originalsPage import OriginalsPage
# import pytest
# import json


# cluster continue watching is being lost
# @pytest.fixture(scope="module")
# def driver():
#     setup_driver = SetupDriver()
#     yield setup_driver.driver
#     setup_driver.driver.quit()

# def test_start(driver):
#     login = LoginPage(driver)
#     role = "FreeUser"
#     login.loginProcess(driver, role)

# def test_slideClusterContinueWatching(driver):
#     homepage = HomepagePage(driver)
#     originals = OriginalsPage(driver)
#     originals.handleMaximumDevice()
#     assert homepage.slideClusterContinueWatching(driver)
    
# def test_openDetailContinueWatching(driver):
#     homepage = HomepagePage(driver)
#     assert homepage.clickCardContinueWatching()

# def test_watchContinueWatchingVod(driver):
#     homepage = HomepagePage(driver)
#     assert homepage.clickIconPlayContinueWatching(driver)