# from pages.loginPage import LoginPage
# from pages.chooseProfilePage import ChooseProfile
# from pages.originalsPage import OriginalsPage
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
#     role = "PremiumSportUser"
#     login.loginProcess(driver, role)
    
# def test_clickCardTopTenWeekVOD(driver):
#     homepage = HomepagePage(driver)
#     originals = OriginalsPage(driver)
#     originals.handleMaximumDevice()
#     assert homepage.clickCardVodTopTenWeek(driver)