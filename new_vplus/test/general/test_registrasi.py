from new_vplus.utils.setup import SetupDriver
from new_vplus.pages.registrasiPages import RegistrasiPage
from new_vplus.testdata.hash import encodeDecodePassword
from new_vplus.utils.generate import Generate
from new_vplus.test.users import users
from new_vplus.utils.setup import platform
import pytest
import json


@pytest.fixture(scope='function')
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_registerLongPhoneNumber(driver):
    register = RegistrasiPage(driver)
    register.goToRegister()
    register.inputFormRegis("89977758388888", "1234AAaa")
    assert register.assertInvalidData()

def test_registerLessPhoneNumber(driver):
    register = RegistrasiPage(driver)
    register.goToRegister()
    register.inputFormRegis("899777", "1234AAaa")
    assert register.assertInvalidData()

def test_registerLessPassword(driver):
    register = RegistrasiPage(driver)
    register.goToRegister()
    register.inputFormRegis("8997775838", "1234Aa")
    assert register.assertInvalidData()

def test_registerEmptyOTP(driver):
    register = RegistrasiPage(driver)
    generate = Generate()
    register.goToRegister()
    username = generate.angkaRandom()
    register.inputFormRegis(username, "1234AAaa")
    register.clickSendOTP()
    register.assertButtonRegisterDisabled()

def test_registerWrongOTP(driver):
    register = RegistrasiPage(driver)
    generate = Generate()
    hashPassword = encodeDecodePassword()
    with open('new_vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]["password"]
    stringDecode = hashPassword.decode(password)
    register.goToRegister()
    username = generate.angkaRandom()
    register.inputFormRegis_clickRegis(username, "1234AAaa")
    assert register.assertOTPSalah()

def test_registerSuccess(driver):
    register = RegistrasiPage(driver)
    hashPassword = encodeDecodePassword()
    generate = Generate()
    register.goToRegister()
    with open('new_vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]["password"]
    stringDecode = hashPassword.decode(password)
    username = generate.angkaRandom()
    register.inputFormRegis_clickRegis(username, stringDecode)
    users.setUsername(username)
    assert register.assertDiscoverProfile()

def test_registerEmailSuccess(driver):
    register = RegistrasiPage(driver)
    generate = Generate()
    hashPassword = encodeDecodePassword()
    register.goToRegister()
    angkarandom = generate.angkaRandom()
    username = "automate"+angkarandom+"@visionplus.id"
    with open('new_vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]['password']
    stringDecode = hashPassword.decode(password)
    register.inputFormRegisEmail(username, stringDecode)
    register.clickSendOTP()
    register.clickButtonRegister(username)
    assert register.assertDiscoverProfile()

def test_accountRegistered(driver):
    register = RegistrasiPage(driver)
    register.goToRegister()
    register.inputFormRegis("8997775838", "1234AAaa")
    register.clickSendOTP()
    assert register.assertAccountRegistered()

def test_accountEmailEmpty(driver):
    register = RegistrasiPage(driver)
    register.goToRegister()
    register.inputFormRegisEmail(" ", " ")
    assert register.assertButtonRegisterDisabled()

def test_accountInvalidEmail(driver):
    register = RegistrasiPage(driver)
    generate = Generate()
    register.goToRegister()
    angkarandom = generate.angkaRandom()
    username = "baskarati"+angkarandom+"@mncgr1"
    register.inputFormRegisEmail(username, " ")
    assert register.assertInvalidEmail()
    
def test_clickOTP2times(driver):
    register = RegistrasiPage(driver)
    hashPassword = encodeDecodePassword()
    generate = Generate()
    register.goToRegister()
    with open('new_vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]["password"]
    stringDecode = hashPassword.decode(password)
    username = generate.angkaRandom()
    register.inputFormRegis_clickRegis_2menit(username, stringDecode)
    assert register.assertOTP2times()
