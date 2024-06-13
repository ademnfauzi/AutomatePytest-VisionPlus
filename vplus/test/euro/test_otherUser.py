from vplus.pages.buyPackagePage import BuyPackage
from vplus.pages.liveTvPage import TvPage
from vplus.pages.loginPage import LoginPage
from vplus.pages.originalsPage import OriginalsPage
from vplus.pages.visitorPage import VisitorPage
from vplus.utils.setup import SetupDriver
from vplus.utils.setup import platform
import pytest
import json

@pytest.fixture(scope="function")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()
    
def test_visitor(driver):
    visitor = VisitorPage(driver)
    login = LoginPage(driver)
    # login.open()
    visitor.goLiveTV()
    assert visitor.assertLoginPage()

def test_freeUser(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    originals = OriginalsPage(driver)
    originals.handleMaximumDevice()
    tv = TvPage(driver)
    tv.goTvPage()
    tv.tvSearchEuro1("EURO 1")
    assert tv.assertSubscribe()
    tv.tvSearchEuro2("EURO 2")
    assert tv.assertSubscribe()
    login.logout()
    assert login.assertLogout()
    
def test_premiumUser(driver):
    login = LoginPage(driver)
    role = "PremiumUser"
    login.loginProcess(driver, role)
    originals = OriginalsPage(driver)
    originals.handleMaximumDevice()
    tv = TvPage(driver)
    tv.goTvPage()
    tv.tvSearchEuro1("EURO 1")
    assert tv.assertSubscribe()
    tv.tvSearchEuro2("EURO 2")
    assert tv.assertSubscribe()
    buyPackage = BuyPackage(driver)
    buyPackage.goBuyPackage()
    buyPackage.checkCardPackageEuro()
    buyPackage.backToMainTab()
    originals.backPage()
    login.logout()
    assert login.assertLogout()
    
def test_premiumSportUser(driver):
    login = LoginPage(driver)
    role = "PremiumSportUser"
    login.loginProcess(driver, role)
    originals = OriginalsPage(driver)
    originals.handleMaximumDevice()
    tv = TvPage(driver)
    tv.goTvPage()
    tv.tvSearchEuro1("EURO 1")
    assert tv.assertSubscribe()
    tv.tvSearchEuro2("EURO 2")
    assert tv.assertSubscribe()
    login.logout()
    assert login.assertLogout()