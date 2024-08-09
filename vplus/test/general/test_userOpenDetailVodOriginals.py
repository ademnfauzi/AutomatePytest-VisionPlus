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
    originals.goOriginals()
    assert originals.assertGoOriginals()
    
# def test_switchCluster(driver):
#     originals = OriginalsPage(driver)
#     assert originals.assertClickCluster()

def test_canOpenDetailVOD(driver):
    originals = OriginalsPage(driver)
    originals.clickCardVODOriginals()
    assert originals.assertClickCardVOD()
    
# Try Add To List
def test_addToList(driver):
    originals = OriginalsPage(driver)
    originals.addToList()
    assert originals.assertAddToList()

# Try Click Like
def test_clickLike(driver):
    originals = OriginalsPage(driver)
    originals.clickLike()
    assert originals.assertClickLike()
    
# Try Click UnLike
def test_clickUnLike(driver):
    originals = OriginalsPage(driver)
    originals.clickUnLike()
    assert originals.assertClickUnLike()

# Try Click Share
# def test_clickShare(driver):
#     originals = OriginalsPage(driver)
#     originals.clickShare()
#     assert originals.assertClickShare()    
    
# Try Click Trailler
# def test_clickTrailler(driver):
#     originals = OriginalsPage(driver)
#     originals.clickTrailler()
#     assert originals.assertTrailler()

    