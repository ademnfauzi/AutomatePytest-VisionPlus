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

def test_start(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)

def test_freeWatchTV(driver):
    tv = TvPage(driver)
    originals = OriginalsPage(driver)
    originals.handleMaximumDevice()
    tv.goTvPage()
    # management device dlu
    tv.managementDevice()
    assert tv.handleAds()
    assert tv.assertTvPlay()

def test_freePauseTV(driver):
    tv = TvPage(driver)
    assert tv.assertTvPause()
    # case sebelumnya pause, jadi diclose dlu pausenya
    tv.tvCloseVideoPaused()
    # abis click button X di video, dia kembali ke player terus ngecheck lagi apakah ada ads
    tv.handleAds()

def test_freeSearchPremiumTvN(driver):
    tv = TvPage(driver)
    tv.tvSearchTvNmovies("tvn")
    assert tv.assertSubscribe()

def test_freeSearchSportstars(driver):
    tv = TvPage(driver)
    # case sebelumnya pause, jadi diclose dlu pausenya
    tv.tvSearchSporstars("sportstars")
    assert tv.assertSubscribe()