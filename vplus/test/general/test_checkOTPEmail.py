from vplus.pages.forgotPasswordPage import ForgotPage
from vplus.pages.googlePage import GooglePage
from vplus.utils.setup import SetupDriver
from vplus.pages.regisPage import registerPage
from vplus.utils.setup import platform
import pytest

@pytest.fixture(scope='function')
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()
    
@pytest.fixture(scope='function')
def driver2(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driverGmail()
    setup_driver.driver.quit()

def test_registerAndCheckEmail(driver, driver2):
    # Register Page actions
    register = registerPage(driver)
    register.goToRegister()
    username = "vp1204740@gmail.com"
    password = "4321Lupa"
    register.inputFormRegis_clickRegisWithEmailCheckOTP(username, password)

    # Google Page actions
    google = GooglePage(driver2)
    assert google.loginGoogle()
    assert google.checkEmail()
    
def test_forgotPasswordAndCheckEmail(driver, driver2):
    # Register Page actions
    forgotPW = ForgotPage(driver)
    forgotPW.goToLoginPage()
    forgotPW.clickForgotPassword()
    username = "visionplustesting@gmail.com"
    password = "4321Lupa"
    forgotPW.inputFormEmail(username, password)
    forgotPW.clickSendOTP()

    # Google Page actions
    google = GooglePage(driver2)
    assert google.loginGoogle()
    assert google.checkEmail()

if __name__ == "__main__":
    pytest.main()