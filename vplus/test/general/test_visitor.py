from vplus.pages.loginPage import LoginPage
from vplus.pages.visitorPage import VisitorPage
from vplus.testdata.hash import encodeDecodePassword
from vplus.utils.setup import SetupDriver
from vplus.utils.setup import platform
import pytest
import json

@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_clickButtonLoginOrRegis(driver):
    visitor = VisitorPage(driver)
    login = LoginPage(driver)
    # login.open()
    visitor.goToLogin()
    assert visitor.assertLoginPage()

def test_clickIconSettings(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.goIconSettings()
    assert visitor.assertLoginPage()
    
def test_clickMyDownloads(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.goIconSettings()
    assert visitor.assertLoginPage()
    
def test_clickBuyPackage(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.goBuyPackage()
    assert visitor.assertLoginPage()
    
def test_clickBuyPackage(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.goBuyPackage()
    assert visitor.assertLoginPage()
    
def test_clickLiveTv(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.goLiveTV()
    assert visitor.assertLoginPage()
    
def test_clickIconProfile(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.goIconProfile()
    assert visitor.assertLoginPage()
    
def test_clickButtonWatchVod(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.goOpenDetail()
    visitor.clickButtonWatch()
    assert visitor.assertLoginPage()
    
def test_clickIconAddToList(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.clickIconAddToList()
    assert visitor.assertLoginPage()
    
def test_clickIconLike(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.clickIconLike()
    assert visitor.assertLoginPage()
    
def test_clickIconUnLike(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.clickIconUnLike()
    assert visitor.assertLoginPage()
    
def test_clickIconShare(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.clickIconShare()
    assert visitor.assertLoginPage()
    
def test_clickButtonWatchProgramGuide(driver):
    visitor = VisitorPage(driver)
    visitor.backToMainTab()
    visitor.goToHome()
    visitor.goOpenDetailProgramGuide()
    visitor.clickButtonWatch()
    assert visitor.assertLoginPage()
    
def test_loginAfterBecomeVisitor(driver):
    visitor = VisitorPage(driver)
    login = LoginPage(driver)
    hashPassword = encodeDecodePassword()
    visitor.backToMainTab()
    visitor.goToHome()
    visitor.goLiveTV()
    assert visitor.assertLoginPage()
    with open('vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
            
    username = data['FreeUser'][0]["username"]
    password = data['FreeUser'][0]["password"]

    stringDecode = hashPassword.decode(password)
    login.inputFormLogin(username, stringDecode)
    assert login.assertSuccessLogin()