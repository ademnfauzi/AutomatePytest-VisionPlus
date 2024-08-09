from vplus.pages.liveTvPage import TvPage
from vplus.pages.loginPage import LoginPage
from vplus.pages.originalsPage import OriginalsPage
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
    role = "FreeUserMalaysia"
    prefix = "+60"
    login.loginProcessOther(driver, role, prefix)

def test_goToLiveTvAndWwatchDWChannels(driver):
    tv = TvPage(driver)
    originals = OriginalsPage(driver)
    originals.handleMaximumDevice()
    tv.goTvPage()
    tv.managementDevice()
    assert tv.assertSubscribe()
        
def test_freeWatchTRTWorldChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("TRT World")
    assert tv.assertSubscribe()

def test_freeWatchRTChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("150")
    assert tv.assertSubscribe()
    
def test_freeWatchChannelNewsAsiaChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Channel News Asia")
    assert tv.assertSubscribe()
    
def test_freeWatchCGTNChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("156")
    assert tv.assertSubscribe()
    
def test_freeWatchNHKWorldJapanChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("NHK")
    assert tv.assertSubscribe()
    
def test_freeWatchTV5MondeChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("TV5Monde")
    assert tv.assertSubscribe()
    
def test_freeWatchArirangChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Arirang")
    assert tv.assertSubscribe()
    
def test_freeWatchGTVWorldChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("ABC")
    assert tv.assertSubscribe()
    
def test_freeWatchRCTIWorldhannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("RCTI World")
    assert tv.assertSubscribe()
    
def test_freeWatchGTVWorldChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("GTV World")
    assert tv.assertSubscribe()
    
def test_freeWatchMNCTVWorldChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("MNCTV World")
    assert tv.assertSubscribe()
    
def test_freeWatchDramaWorldChannels(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Drama World")
    assert tv.assertSubscribe()