import pytest
from vplus.pages.addProfilePage import AddProfilePage
from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import SetupDriver
from vplus.utils.setup import platform


@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_start(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)

def test_successAddProfile(driver):
    addProfile = AddProfilePage(driver)
    addProfile.clickIconSettings()
    addProfile.clickSettings()
    addProfile.clickConfigure()
    addProfile.clickAddProfile()
    addProfile.clickImage()
    addProfile.chooseAvatar()
    addProfile.clickDoneAvatar()
    addProfile.inputNewAvatar()
    addProfile.clickOK()
    assert addProfile.assertSuccessCreateAvatar()

def test_deleteAvatar(driver):
    addProfile = AddProfilePage(driver)
    addProfile.deleteAvatar()
    assert addProfile.assertSuccessDeleteAvatar()
