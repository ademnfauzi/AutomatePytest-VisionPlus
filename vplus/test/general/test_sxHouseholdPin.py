from vplus.pages.addProfilePage import AddProfilePage
from vplus.pages.pinPage import PagePin
from vplus.testdata.hash import encodeDecodePassword
from vplus.pages.loginPage import LoginPage
from vplus.pages.chooseProfilePage import ChooseProfile
from vplus.utils.setup import SetupDriver
from vplus.test.general.user import users
from vplus.utils.setup import platform
import pytest
import json

@pytest.fixture(scope='module')
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_start(driver):
    login = LoginPage(driver)
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
    
def test_enablePinHouseholdPinAddProfiles(driver):
    pin = PagePin(driver)
    pin.clickIconSettings()
    pin.clickSettings()
    assert pin.enablePin()
    assert pin.disablePin()
    
def test_changePin(driver):
    pin = PagePin(driver)
    assert pin.changePin()
    
# def test_disabledPin(driver):
#     pin = PagePin(driver)
#     pin.disablePin()

def test_enablePinHouseholdPinToPay(driver):
    pin = PagePin(driver)
    addProfile = AddProfilePage(driver)
    addProfile.clickConfigure()
    pin.chooseProfile()
    # pin.householdPINToPay()
    assert pin.enablePinToPay()
    assert pin.disablePinToPay()