from new_vplus.pages.loginPages import LoginPage
from new_vplus.utils.setup import SetupDriver
from new_vplus.testdata.hash import encodeDecodePassword
import pytest
import json
from new_vplus.utils.setup import platform

# scope function biar gunakan 1 browser buat setiap function
@pytest.fixture(scope="function")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_NewloginLongPhoneNumber(driver):
    login = LoginPage(driver)
    login.goToLogin()
    login.inputFormLoginHP("899777583838383", "1234AAaa")
    assert login.assertButtonLoginDisabled()

def test_NewphoneEmpty(driver):
    login = LoginPage(driver)
    login.goToLogin()
    login.inputFormLoginHP(" ", " ")
    assert login.assertButtonLoginDisabled()

def test_NewLessPhoneNumber(driver):
    login = LoginPage(driver)
    login.goToLogin()
    login.inputFormLoginHP("899777", " ")
    assert login.assertButtonLoginDisabled()

def test_NewloginUnregistered(driver):
    login = LoginPage(driver)
    login.goToLogin()
    login.inputFormLoginHP("899777858585", "1234AAaa")
    login.clickButtonLogin()
    assert login.assertLoginUnregistered()

def test_NewemailEmpty(driver):
    login = LoginPage(driver)
    login.goToLogin()
    login.inputFormEmail(" ", " ")
    assert login.assertButtonLoginDisabled()

def test_NewinccorectEmailFormat(driver):
    login = LoginPage(driver)
    login.goToLogin()
    login.inputFormEmail("baskara@gmail", " ")
    assert login.assertInccorectFormat()

def test_NewunregisteredEmail(driver):
    login = LoginPage(driver)
    login.goToLogin()
    login.inputFormEmail("baskara9023@gmail.com", "1234AAaa")
    login.clickButtonLogin()
    assert login.assertLoginUnregistered()

def test_NewsuccessLoginPhoneNumber(driver):
    login = LoginPage(driver)
    hashPassword = encodeDecodePassword()
    with open('new_vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
            
    username = data['FreeUser'][0]["username"]
    password = data['FreeUser'][0]["password"]

    stringDecode = hashPassword.decode(password)
    
    login.clickLogin(username, stringDecode)
    assert login.assertSuccessLogin()
    # login.closeBrowser()

def test_NewsuccessLoginWithEmail(driver):
    login = LoginPage(driver)
    role = "FreeUserEmail"
    assert login.loginProcessWithEmail(driver, role)

def test_NewloginToLogout(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    login.logout()
    assert login.assertLogout()

def test_NewloginWrongPW(driver):
    login = LoginPage(driver)
    login.clickLogin('8997775838', 'passwordsalah')
    assert login.assertWrongPassword()
    login.closeBrowser()


