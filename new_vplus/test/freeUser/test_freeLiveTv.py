from new_vplus.pages.loginPages import LoginPage
from new_vplus.pages.liveTvPages import LiveTvPage
from new_vplus.pages.originalsPages import OriginalsPage
from new_vplus.pages.searchPages import SearchPage
from new_vplus.utils.setup import SetupDriver
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
    assert login.assertSuccessLogin()

def test_goLiveTv(driver):
    tv = LiveTvPage(driver)
    originals = OriginalsPage(driver)
    # originals.handleMaximumDevice()
    assert tv.goLiveTv()
    
def test_playFreeChannels(driver):
    tv = LiveTvPage(driver)
    assert tv.handleAds()
    tv.hoverLiveTv()
    assert tv.assertAfterClickCardPlaying()
    
def test_pauseLiveTv(driver):
    tv = LiveTvPage(driver)
    assert tv.clickButtonPause()
    
def test_playPremiumChannels(driver):
    search = SearchPage(driver)
    tv = LiveTvPage(driver)
    tv.hoverLiveTv()
    search.clikIconSearch()
    search.inputSearch('TVN')
    search.clickCardResultsearch()
    assert tv.assertUpgradepayment()

def test_playSportChannels(driver):
    search = SearchPage(driver)
    tv = LiveTvPage(driver)
    tv.hoverLiveTv()
    search.clikIconSearch()
    search.deleteInputSearch()
    search.inputSearch('Soccer Channel')
    search.clickCardResultsearch()
    assert tv.assertUpgradepayment()