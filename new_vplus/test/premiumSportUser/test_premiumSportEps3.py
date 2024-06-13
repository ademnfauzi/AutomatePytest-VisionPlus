from new_vplus.pages.searchPages import SearchPage
from new_vplus.pages.originalsPages import OriginalsPage
from new_vplus.pages.loginPages import LoginPage
from vplus.utils.setup import platform
import pytest
from new_vplus.utils.setup import SetupDriver
import json

@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_start(driver):
    login = LoginPage(driver)
    role = "PremiumSportUser"
    login.loginProcess(driver, role)
    assert login.assertSuccessLogin()

def test_watchEps3(driver):
    search = SearchPage(driver)
    eps3 = OriginalsPage(driver)
    search.refreshThePageAfterLogin()
    search.clikIconSearch()
    search.inputSearch("radio")
    search.clickCardResultsearch()
    eps3.clickEpisode3()
    assert eps3.assertPlaying()
    
