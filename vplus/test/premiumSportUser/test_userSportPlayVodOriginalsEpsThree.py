from vplus.pages.originalsPage import OriginalsPage
from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import SetupDriver
from vplus.utils.setup import platform
import pytest

@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_login(driver):
    login = LoginPage(driver)
    role = "PremiumSportUser"
    login.loginProcess(driver, role)
    
def test_switchPage(driver):
    originals = OriginalsPage(driver)
    originals.handleMaximumDevice()
    originals.goOriginals()
    assert originals.assertGoOriginals()
    
def test_switchCluster(driver):
    originals = OriginalsPage(driver)
    assert originals.assertClickCluster()
    
# Try Play VOD Eps 3

def test_canOpenDetailVOD(driver):
    originals = OriginalsPage(driver)
    originals.clickCardVODOriginals()
    assert originals.assertClickCardVOD()
    
def test_canClickEpsThree(driver):
    originals = OriginalsPage(driver)
    originals.scroll1500()
    originals.clickEpsThree()

def test_videoPlayerVOD(driver):
    originals = OriginalsPage(driver)
    originals.clickButtonWatch()
    assert originals.assertPlayVOD()

def test_videoPauseVOD(driver):
    originals = OriginalsPage(driver)
    assert originals.assertPauseVOD()  

    