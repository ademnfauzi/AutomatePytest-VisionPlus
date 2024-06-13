from vplus.pages.buyPackagePage import BuyPackage
from vplus.pages.loginPage import LoginPage
from vplus.utils.setup import SetupDriver
from vplus.utils.setup import platform
import pytest

@pytest.fixture(scope="function")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_buyPackagePremiumBCA(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium'
    payment = 'Payment'
    typePayment = 'BCA'
    assert buyPackage.choosePayment(package,payment,typePayment,role)

def test_buyPackagePremiumSportGopay(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium Sport'
    payment = 'Payment'
    typePayment = 'Gopay'
    assert buyPackage.choosePayment(package,payment,typePayment,role)
    
def test_buyPackagePremiumShopeePay(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium'
    payment = 'Payment'
    typePayment = 'Shopee Pay'
    assert buyPackage.choosePayment(package,payment,typePayment,role)
    
def test_buyPackagePremiumSportBRI(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium Sport'
    payment = 'Payment'
    typePayment = 'BRI'
    assert buyPackage.choosePayment(package,payment,typePayment,role)

def test_buyPackagePremiumSportBNI(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium'
    payment = 'Payment'
    typePayment = 'BNI'
    assert buyPackage.choosePayment(package,payment,typePayment,role)
    
def test_buyPackagePremiumSportQris(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium Sport'
    payment = 'Payment'
    typePayment = 'QRIS'
    assert buyPackage.choosePayment(package,payment,typePayment,role)
    
def test_buyPackagePremiumSportMandiri(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium'
    payment = 'Payment'
    typePayment = 'Mandiri'
    assert buyPackage.choosePayment(package,payment,typePayment,role)
        
def test_buyPackagePremiumSportPermata(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium Sport'
    payment = 'Payment'
    typePayment = 'Permata'
    assert buyPackage.choosePayment(package,payment,typePayment,role)
    
def test_buyPackagePremiumSportOtherBanks(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium'
    payment = 'Payment'
    typePayment = 'Other Bank'
    assert buyPackage.choosePayment(package,payment,typePayment,role)

def test_buyPackagePremiumSportDebitOrCredit(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium Sport'
    payment = 'Payment'
    typePayment = 'Debit Credit'
    assert buyPackage.choosePayment(package,payment,typePayment,role)

# is being lost
# def test_buyPackagePremiumSportTelcoBalance(driver):
#     login = LoginPage(driver)
#     role = "FreeUser"
#     login.loginProcess(driver, role)
#     buyPackage = BuyPackage(driver)
#     assert buyPackage.goBuyPackage()
#     buyPackage = BuyPackage(driver)
#     package = 'Premium'
#     payment = 'Telco Balance'
#     typePayment = ''
#     assert buyPackage.choosePayment(package,payment,typePayment,role)

def test_buyPackagePremiumSportOvo(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium Sport'
    payment = 'Other Payment'
    typePayment = 'Other Bank'
    assert buyPackage.choosePayment(package,payment,typePayment,role)

def test_buyPackagePremiumSportDana(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium'
    payment = 'Other Payment'
    typePayment = 'Other Bank'
    assert buyPackage.choosePayment(package,payment,typePayment,role)
    
def test_buyPackagePremiumSportLinkAja(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    buyPackage = BuyPackage(driver)
    package = 'Premium Sport'
    payment = 'Other Payment'
    typePayment = 'Other Bank'
    assert buyPackage.choosePayment(package,payment,typePayment,role)

