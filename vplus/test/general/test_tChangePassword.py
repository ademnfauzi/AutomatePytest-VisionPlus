import pytest
import json
from vplus.pages.changePasswordPage import ChangesPage
from vplus.pages.chooseProfilePage import ChooseProfile
from vplus.pages.loginPage import LoginPage
from vplus.testdata.hash import encodeDecodePassword
from vplus.utils.setup import SetupDriver
from vplus.test.general.user import users
from vplus.utils.setup import platform


@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()
    
def test_passwordSame(driver):
    login = LoginPage(driver)
    changes = ChangesPage(driver)
    chooseProfile = ChooseProfile(driver)
    hashPassword = encodeDecodePassword()
    # login.open()
    with open('vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]["password"]
    stringDecode = hashPassword.decode(password)
    # getusername dari regis
    login.clickLogin(users.getUsername(), stringDecode)
    chooseProfile.chooseProfileAfterLogin()
    # login.skipCreateAvatar()
    changes.clickIconSettings()
    changes.clickSettings()
    changes.clickConfigure()
    changes.inputFormCHangePW(stringDecode, stringDecode)
    assert changes.assertPasswordSame()

def test_invalidPassword(driver):
    changes = ChangesPage(driver)
    changes.removeInput()
    changes.inputFormCHangePWWithoutSwitch("currenT1", "")
    changes.clickChange()
    assert changes.assertPasswordInvalid()
    changes.closePopUp()
    
def test_succesfullyChangePassword(driver):
    changes = ChangesPage(driver)
    hashPassword = encodeDecodePassword()
    with open('vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]["password"]
    stringDecode = hashPassword.decode(password)
    changes.removeInput()
    changes.inputFormCHangePWWithoutSwitch(stringDecode, "")
    changes.removeInputRenewPW()
    changes.inputFormCHangePWWithoutSwitch("", "PasswordBru1")
    changes.clickChange()
    assert changes.assertSuccessChangePW()