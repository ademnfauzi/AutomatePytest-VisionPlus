import pytest
from new_vplus.pages.forgotPasswordPages import ForgotPasswordPage
from new_vplus.testdata.hash import encodeDecodePassword
from new_vplus.utils.generate import Generate
import json
from new_vplus.utils.setup import SetupDriver
from new_vplus.test.users import users
from new_vplus.utils.setup import platform


@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_successForgot(driver):
    forgotPW = ForgotPasswordPage(driver)
    decoder = encodeDecodePassword()
    generate = Generate()
    # forgotPW.open()
    forgotPW.goToLoginPage()
    forgotPW.clickForgotPassword()
    with open("new_vplus/testdata/dataUser.json") as json_file:
        data = json.load(json_file)
    password = data["FreeUser"][0]["password"]
    decodePassword = decoder.decode(password)
    username = users.getUsername()
    print(username)
    forgotPW.inputForm(username, decodePassword)
    forgotPW.clickSendOTP()
    codeOTP = generate.endpointOTPforgotPW(username)
    forgotPW.inputOTP(codeOTP)
    forgotPW.clickSaveForgotPassword()
    assert forgotPW.assertSuccessForgotPassword()

def test_hidePassword(driver):
    forgotPW = ForgotPasswordPage(driver)
    forgotPW.clickForgotPassword()
    forgotPW.inputForm("", "1234AAaa")
    forgotPW.clickUnhide()
    assert forgotPW.assertSaveRegisterDisabled()

def test_emptyField(driver):
    forgotPW = ForgotPasswordPage(driver)
    forgotPW.deletePhone()
    assert forgotPW.assertSaveRegisterDisabled()
