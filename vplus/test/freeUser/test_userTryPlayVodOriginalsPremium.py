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
    
# Play VOD

def test_canOpenDetailVODPremium(driver):
    originals = OriginalsPage(driver)
    originals.clickCardVODOriginalsPremium()
    assert originals.assertClickCardVOD()

def test_cantPlayVOD(driver):
    originals = OriginalsPage(driver)
    originals.clickButtonSubscribe()
    
def test_popUpSubscribe(driver):
    originals = OriginalsPage(driver)
    assert originals.assertPopUpSubscribe()    

def test_clickPackagePremium(driver):
    originals = OriginalsPage(driver)
    assert originals.assertClickPackagePremium()
