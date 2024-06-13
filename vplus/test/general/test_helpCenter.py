from vplus.pages.buyPackagePage import BuyPackage
from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import platform
from vplus.utils.setup import SetupDriver
import pytest

@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()
    
def test_start(driver):
    login = LoginPage(driver)
    buyPackage = BuyPackage(driver)
    role = "PremiumUser"
    login.loginProcess(driver, role)
    assert buyPackage.goBuyPackage()

def test_goTermAndCondition(driver):
    buyPackage = BuyPackage(driver)
    assert buyPackage.goTermAndCondtion()
    
def test_goPrivacyAndPolicy(driver):
    buyPackage = BuyPackage(driver)
    # buyPackage.backPage()
    assert buyPackage.goPrivacyAndPolicy()
    
def test_goSoftwareLicence(driver):
    buyPackage = BuyPackage(driver)
    # buyPackage.backPage()
    assert buyPackage.goSoftwareLicence()
    