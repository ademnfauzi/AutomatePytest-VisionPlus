from vplus.pages.loginPage import LoginPage
from vplus.pages.tonightPage import TonightPage
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
    
def test_goTonight(driver):
    tonight = TonightPage(driver)
    assert tonight.goTonight()
    
def test_goTabFilms(driver):
    tonight = TonightPage(driver)
    assert tonight.goTabFilms()
    
def test_goTabSports(driver):
    tonight = TonightPage(driver)
    assert tonight.goTabSports()
    
def test_goTabNews(driver):
    tonight = TonightPage(driver)
    assert tonight.goTabNews()
    
def test_goTabChildren(driver):
    tonight = TonightPage(driver)
    assert tonight.goTabChildren()
    
def test_goTabSeries(driver):
    tonight = TonightPage(driver)
    assert tonight.goTabSeriess()
    
def test_goTabEntertainment(driver):
    tonight = TonightPage(driver)
    assert tonight.goTabEntertainment()
    
def test_goTabCulture(driver):
    tonight = TonightPage(driver)
    assert tonight.goTabCulture()
    
def test_goTabMusic(driver):
    tonight = TonightPage(driver)
    assert tonight.goTabMusic()
    
def test_filterByProgress(driver):
    tonight = TonightPage(driver)
    assert tonight.goFilterByProgress()
    
def test_filterByChannels(driver):
    tonight = TonightPage(driver)
    assert tonight.goFilterByChannels()
    
def test_filterByAlphabet(driver):
    tonight = TonightPage(driver)
    assert tonight.goFilterByAlphabets()