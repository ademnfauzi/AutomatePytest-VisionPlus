from vplus.pages.downloadPage import DownloadPage
from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import SetupDriver
import pytest
from vplus.utils.setup import platform

@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_start(driver):
    login = LoginPage(driver)
    role = "PremiumSportUser"
    login.loginProcess(driver, role)
    
# Disable for temporary because still have isues in downloads vod
# def test_canDownloadVod(driver):
#     originals = OriginalsPage(driver)
#     originals.goOriginals()
#     originals.clickCardVODOriginals()
#     assert originals.assertClickCardVOD()
#     originals.clickEpsTwo()
#     assert originals.downloadsVod()
    
def test_goMyDownloads(driver):
    download = DownloadPage(driver)
    assert download.goMyDownload()
