from vplus.pages.loginPage import LoginPage
from vplus.pages.originalsPage import OriginalsPage
from vplus.pages.sportPage import SportPage
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
    role = "PremiumUser"
    login.loginProcess(driver, role)

def test_goSport(driver):
    sport = SportPage(driver)
    originals = OriginalsPage(driver)
    # originals.handleMaximumDevice()
    assert sport.goSport()
    
def test_userWatchVodSport(driver):
    sport = SportPage(driver)
    assert sport.goWatchVodSportsWithPremium()