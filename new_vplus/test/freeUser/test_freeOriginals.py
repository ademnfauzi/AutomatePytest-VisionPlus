from new_vplus.pages.originalsPages import OriginalsPage
from new_vplus.pages.loginPages import LoginPage
import pytest
from new_vplus.utils.setup import SetupDriver
from new_vplus.utils.setup import platform
from new_vplus.pages.liveTvPages import LiveTvPage


@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()
    
def test_start(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)

def test_watchOriginalsSuccess(driver):
    originals = OriginalsPage(driver)
    tv = LiveTvPage(driver)
    originals.clickNavOriginals()
    originals.clickCardOriginalsFirst()
    originals.clickButtonWatch()
    assert originals.assertOriginalsPlaying()

def test_pauseLiveTv(driver):
    originals = OriginalsPage(driver)
    originals.clickPause()