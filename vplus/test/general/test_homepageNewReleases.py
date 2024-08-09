# from pages.loginPage import LoginPage
# from pages.chooseProfilePage import ChooseProfile
# from pages.homepagePage import HomepagePage
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

# def test_login(driver):
#     login = LoginPage(driver)
#     role = "FreeUser"
#     login.loginProcess(driver, role)

# def test_slideClusterNewReleases(driver):
#     homepage = HomepagePage(driver)
#     assert homepage.slideClusterNewReleases(driver)
    
# def test_openDetailVodNewReleases(driver):
#     homepage = HomepagePage(driver)
#     homepage.clickCardNewReleases()
#     assert homepage.assertDetailVod()
    