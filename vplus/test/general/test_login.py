from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import SetupDriver
from vplus.testdata.hash import encodeDecodePassword
from vplus.utils.setup import platform
import pytest
import json

# scope function biar gunakan 1 browser buat setiap function
@pytest.fixture(scope="function")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_loginLongPhoneNumber(driver):
    login = LoginPage(driver)
    # login.open()
    login.goToLogin()
    login.inputFormLoginHP("899777583838383", "1234AAaa")
    assert login.assertButtonLoginDisabled()

def test_phoneEmpty(driver):
    login = LoginPage(driver)
    # login.open()
    login.goToLogin()
    login.inputFormLoginHP(" ", " ")
    assert login.assertButtonLoginDisabled()

def test_LessPhoneNumber(driver):
    login = LoginPage(driver)
    # login.open()
    login.goToLogin()
    login.inputFormLoginHP("899777", " ")
    assert login.assertButtonLoginDisabled()

def test_loginUnregistered(driver):
    login = LoginPage(driver)
    # login.open()
    login.goToLogin()
    login.inputFormLoginHP("899777858585", "1234AAaa")
    login.clickButtonLogin()
    assert login.assertLoginUnregistered()

def test_emailEmpty(driver):
    login = LoginPage(driver)
    # login.open()
    login.goToLogin()
    login.inputFormEmail(" ", " ")
    assert login.assertButtonLoginDisabled()

def test_inccorectEmailFormat(driver):
    login = LoginPage(driver)
    # login.open()
    login.goToLogin()
    login.inputFormEmail("baskara@gmail", " ")
    assert login.assertInccorectFormat()

def test_unregisteredEmail(driver):
    login = LoginPage(driver)
    # login.open()
    login.goToLogin()
    login.inputFormEmail("baskara9023@gmail.com", "1234AAaa")
    login.clickButtonLogin()
    assert login.assertLoginUnregistered()

def test_successLoginPhoneNumber(driver):
    login = LoginPage(driver)
    hashPassword = encodeDecodePassword()
    # login.open()
    with open('vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    username = data['FreeUser'][0]["username"]
    password = data['FreeUser'][0]["password"]
    stringDecode = hashPassword.decode(password)
    login.clickLogin(username, stringDecode)
    assert login.assertSuccessLogin()
#    login.closeBrowser()

def test_successLoginWithEmail(driver):
    login = LoginPage(driver)
    role = "FreeUserEmail"
    assert login.loginProcessWithEmail(driver, role)

def test_loginToLogout(driver):
    login = LoginPage(driver)
    role = "emailFreeUser"
    login.loginProcessWithEmail(driver, role)
    login.logout()
    assert login.assertLogout()

def test_loginWrongPW(driver):
    login = LoginPage(driver)
    # login.open()
    login.clickLogin('8997775838', 'passwordsalah')
    assert login.assertWrongPassword()
    login.closeBrowser()


