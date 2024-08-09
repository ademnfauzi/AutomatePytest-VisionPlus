from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import SetupDriver
from vplus.pages.regisPage import registerPage
from vplus.testdata.hash import encodeDecodePassword
from vplus.utils.generate import Generate
from vplus.utils.setup import platform
from vplus.test.general.user import users
import pytest
import json


@pytest.fixture(scope='function')
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_registerLongPhoneNumber(driver):
    register = registerPage(driver)
    # register.open()
    register.goToRegister()
    register.inputFormRegis("89977758388888", "1234AAaa")
    assert register.assertInvalidData()

def test_registerLessPhoneNumber(driver):
    register = registerPage(driver)
    # register.open()
    register.goToRegister()
    register.inputFormRegis("899777", "1234AAaa")
    assert register.assertInvalidData()

def test_registerLessPassword(driver):
    register = registerPage(driver)
    # register.open()
    register.goToRegister()
    register.inputFormRegis("8997775838", "1234Aa")
    assert register.assertInvalidData()

def test_registerEmptyOTP(driver):
    register = registerPage(driver)
    generate = Generate()
    # register.open()
    register.goToRegister()
    username = generate.numberRandom()
    register.inputFormRegis(username, "1234AAaa")
    register.clickSendOTP()
    register.assertButtonRegisterDisabled()

def test_registerWrongOTP(driver):
    register = registerPage(driver)
    generate = Generate()
    hashPassword = encodeDecodePassword()
    # register.open()
    with open('vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]["password"]
    stringDecode = hashPassword.decode(password)
    register.goToRegister()
    username = generate.numberRandom()
    register.inputFormRegis_clickRegis(username, "1234AAaa")
    assert register.assertOTPSalah()

def test_registerSuccess(driver):
    register = registerPage(driver)
    hashPassword = encodeDecodePassword()
    generate = Generate()
    # register.open()
    register.goToRegister()
    with open('vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]["password"]
    stringDecode = hashPassword.decode(password)
    username = generate.numberRandom()
    register.inputFormRegis_clickRegis(username, stringDecode)
    users.setUsername(username)
    assert register.assertDiscoverProfile()
    # login = LoginPage(driver)
    # login.skipCreateAvatar()

def test_registerEmailSuccess(driver):
    register = registerPage(driver)
    generate = Generate()
    hashPassword = encodeDecodePassword()
    # register.open()
    register.goToRegister()
    numberRandom = generate.numberRandomForEmail()
    username = "A-"+numberRandom+"qa@visionplus.id"
    with open('vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]['password']
    stringDecode = hashPassword.decode(password)
    print(username)
    register.inputFormRegis_clickRegisWithEmail(username, stringDecode)
    assert register.assertDiscoverProfile()

def test_accountRegistered(driver):
    register = registerPage(driver)
    # register.open()
    register.goToRegister()
    register.inputFormRegis("8997775838", "1234AAaa")
    register.clickSendOTP()
    assert register.assertAccountRegistered()

def test_accountEmailEmpty(driver):
    register = registerPage(driver)
    # register.open()
    register.goToRegister()
    register.inputFormRegisEmail(" ", " ")
    assert register.assertButtonRegisterDisabled()

def test_accountInvalidEmail(driver):
    register = registerPage(driver)
    generate = Generate()
    # register.open()
    register.goToRegister()
    numberRandom = generate.numberRandom()
    username = "baskarati"+numberRandom+"@mncgr1"
    register.inputFormRegisEmail(username, " ")
    assert register.assertInvalidEmail()
    
def test_clickOTP2times(driver):
    register = registerPage(driver)
    hashPassword = encodeDecodePassword()
    generate = Generate()
    # register.open()
    register.goToRegister()
    with open('vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]["password"]
    stringDecode = hashPassword.decode(password)
    username = generate.numberRandom()
    register.inputFormRegis_clickRegis_2menit(username, stringDecode)
    assert register.assertOTP2times()
