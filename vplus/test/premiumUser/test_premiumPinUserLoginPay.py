from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import SetupDriver
from vplus.testdata.hash import encodeDecodePassword
from vplus.pages.pinPage import PagePin
from vplus.utils.setup import platform
import pytest
import json

@pytest.fixture(scope='module')
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_chooseProfileWrongPin(driver):
    login = LoginPage(driver)
    pin = PagePin(driver)
    decoder = encodeDecodePassword()
    with open('vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    username = data["PremiumUser"][0]["username"]
    password = data["FreeUser"][0]["password"]
    decodePassword = decoder.decode(password)
    # login.open()
    login.clickLogin(username,decodePassword)
    login.clickProfileWithPin()
    assert login.inputPinProfilewrong()

def test_chooseProfileCorrectPin(driver):
    login = LoginPage(driver)
    assert login.inputPinProfile()

def test_buyPackageWrongPin(driver):
    pin = PagePin(driver)
    pin.clickNavBuyPackage()
    pin.clickBuyPackage()
    pin.clickButtonBuy()
    assert pin.confirmBuyPinWrong()

def test_buyPackageCorrectPin(driver):
    pin = PagePin(driver)
    assert pin.confirmBuyPinCorrectPin()
