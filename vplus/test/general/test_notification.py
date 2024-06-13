from vplus.pages.loginPage import LoginPage
from vplus.pages.notificationPage import NotificationPage
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
    
def test_goToNotification(driver):
    notif = NotificationPage(driver)
    notif.goToNotification()
    assert notif.assertNotification()

