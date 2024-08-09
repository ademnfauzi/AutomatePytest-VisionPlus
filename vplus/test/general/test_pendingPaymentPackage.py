from vplus.pages.buyPackagePage import BuyPackage
from vplus.pages.loginPage import LoginPage
from vplus.pages.transactionHistoryPage import TransactionHistory
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
    role = "FreeUser"
    login.loginProcess(driver, role)
    
def test_goBuyPackage(driver):
    buyPackage = BuyPackage(driver)
    assert buyPackage.goBuyPackage()
    
def test_makePendingPaymentPackage(driver):
    buyPackage = BuyPackage(driver)
    package = 'Premium'
    payment = 'Payment'
    typePayment = 'BCA'
    role = "FreeUser"
    assert buyPackage.choosePayment(package,payment,typePayment,role)
    assert buyPackage.resetPayment()
    
def test_goToTransactionHistory(driver):
    transactionHistory = TransactionHistory(driver)
    assert transactionHistory.goTransactionHistory()
    
def test_openDetailPendingTransactionHistory(driver):
    transactionHistory = TransactionHistory(driver)
    assert transactionHistory.openDetailCardPending()