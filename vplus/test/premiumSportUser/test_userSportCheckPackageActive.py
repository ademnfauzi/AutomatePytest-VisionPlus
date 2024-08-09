from vplus.pages.buyPackagePage import BuyPackage
from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import SetupDriver
from vplus.utils.setup import platform
import pytest

# is being removed
@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_login(driver):
    login = LoginPage(driver)
    role = "PremiumSportUser"
    login.loginProcess(driver, role)

def test_checkPackageActive(driver):
    buyPackage = BuyPackage(driver)
    buyPackage.goBuyPackage()
    assert buyPackage.assertCheckPackageActive()
    