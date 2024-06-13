from vplus.pages.programGuidePage import PageProgramGuide
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
    role = "FreeUser"
    login.loginProcess(driver, role)

def test_programGuidanceNoYesterday(driver):
    program = PageProgramGuide(driver)
    program.clickNavProgramGuidance()
    program.clickDropdownDate()
    assert program.assertNoYesterday()
    
    