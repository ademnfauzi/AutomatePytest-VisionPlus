from vplus.pages.programGuidePage import PageProgramGuide
from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import SetupDriver
from vplus.utils.setup import platform
import pytest

@pytest.fixture(scope='module')
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_login(driver):
    login = LoginPage(driver)
    role = "PremiumUser"
    login.loginProcess(driver, role)

def test_programGuidanceDropdownChannel(driver):
    program = PageProgramGuide(driver)
    program.clickNavProgramGuidance()
    program.clickDropdownChannel() 
    assert program.assertDropdownAllchannels()

def test_programGuidanceLoveUnlove(driver):    
    program = PageProgramGuide(driver)
    program.goToFavorites()
    program.unloveRcti()
    program.clickDropdownFavorites()
    program.goToNationalTV()
    program.loveRcti()

def test_programGuidanceDropdownDate(driver):
    program = PageProgramGuide(driver)
    program.clickDropdownDate()
    assert program.assertDropdownDatePremium()
    
    