from vplus.pages.liveTvPage import TvPage
from vplus.pages.loginPage import LoginPage
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
    role = "PremiumSportUser"
    login.loginProcess(driver, role)

def test_sportWatchTV(driver):
    tv = TvPage(driver)
    tv.goTvPage()
    # management device dlu
    tv.managementDevice()
    assert tv.assertTvPlay()

def test_sportPauseTV(driver):
    tv = TvPage(driver)
    assert tv.assertTvPause()

def test_sportSearchPremiumTvN(driver):
    tv = TvPage(driver)
    # case sebelumnya pause, jadi diclose dlu pausenya
    tv.tvCloseVideoPaused()
    tv.tvSearchTvNmovies("tvn")
    assert tv.assertTvPlay()

def test_freeSearchSportstars(driver):
    tv = TvPage(driver)
    # case sebelumnya pause, jadi diclose dlu pausenya
    tv.tvSearchSporstars("sportstars")
    assert tv.assertTvPlay()
