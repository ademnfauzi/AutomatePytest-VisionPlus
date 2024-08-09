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
    role = "FreeUser"
    login.loginProcess(driver, role)
    
def test_switchPage(driver):
    originals = OriginalsPage(driver)
    originals.handleMaximumDevice()
    originals.goOriginals()
    assert originals.assertGoOriginals()
    
def test_switchCluster(driver):
    originals = OriginalsPage(driver)
    assert originals.assertClickCluster()
    
# Play VOD

def test_canOpenDetailVOD(driver):
    originals = OriginalsPage(driver)
    originals.clickCardVODOriginals()
    assert originals.assertClickCardVOD()

def test_canPlayVODcheckModalHandle(driver):
    originals = OriginalsPage(driver)
    originals.clickButtonWatch()

def test_adsAppear(driver):
    originals = OriginalsPage(driver)
    assert originals.assertAppearAds()
    
def test_videoPlayerVOD(driver):
    originals = OriginalsPage(driver)
    assert originals.assertPlayVOD()

def test_videoPauseVOD(driver):
    originals = OriginalsPage(driver)
    assert originals.assertPauseVOD()
