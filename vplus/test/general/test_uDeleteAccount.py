from vplus.pages.deleteAccountPage import DeleteAccount
from vplus.pages.loginPage import LoginPage
from vplus.pages.chooseProfilePage import ChooseProfile
from vplus.utils.setup import SetupDriver
from vplus.testdata.hash import encodeDecodePassword
from vplus.test.general.user import users
from vplus.utils.setup import platform
import pytest

@pytest.fixture(scope="function")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_deleteAccountSuccess(driver):
    login = LoginPage(driver)
    chooseProfile = ChooseProfile(driver)
    deleteAccount = DeleteAccount(driver)
    hashPassword = encodeDecodePassword()
    # login.open()
    stringDecode = "PasswordBru1"
    # stringDecode = "4321Lupa"
    login.clickLogin(users.getUsername(), stringDecode)
    chooseProfile.chooseProfileAfterLogin()
    deleteAccount.goDeleteAccount()
    assert deleteAccount.keepAccount()
    deleteAccount.goDeleteAccountAfterKeepAccount()
    deleteAccount.goToProcessDeleteAccount()
    assert deleteAccount.processDeleteAccount()

def test_loginAfterDeleted(driver):
    login = LoginPage(driver)
    # login.open()
    stringDecode = "4321Lupa"
    login.clickLogin(users.getUsername(), stringDecode)
    assert login.assertLoginUnregistered()
    