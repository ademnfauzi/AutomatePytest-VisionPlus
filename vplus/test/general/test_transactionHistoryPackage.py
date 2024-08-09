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
    role = "PremiumSportUser"
    login.loginProcess(driver, role)
    
def test_goToTransactionHistory(driver):
    transactionHistory = TransactionHistory(driver)
    assert transactionHistory.goTransactionHistory()
    
def test_pendingTab(driver):
    transactionHistory = TransactionHistory(driver)
    assert transactionHistory.openPendingTab()
    
def test_openAndCloseButtonMore(driver):
    transactionHistory = TransactionHistory(driver)
    assert transactionHistory.openButtonMore()
    assert transactionHistory.closeButtonMore()
    
def test_openDetailPendingTransactionHistory(driver):
    transactionHistory = TransactionHistory(driver)
    assert transactionHistory.openDetailCardPending()
    
def test_failedTab(driver):
    transactionHistory = TransactionHistory(driver)
    transactionHistory.backPage()
    assert transactionHistory.openFailedTab()

# def test_openBuyAgainInFailedTab(driver):
#     transactionHistory = TransactionHistory(driver)
#     transactionHistory.openButtonMore()
#     assert transactionHistory.clickBuyAgain()
#     transactionHistory.backPage()    

# def test_openHelpCenterFailedTab(driver):
#     transactionHistory = TransactionHistory(driver)
#     transactionHistory.openButtonMore()
#     assert transactionHistory.clickHelpCenter()
#     transactionHistory.backPage()

def test_openDetailFailedTransactionHistory(driver):
    transactionHistory = TransactionHistory(driver)
    assert transactionHistory.openDetailCardFailed()
    
def test_successTab(driver):
    transactionHistory = TransactionHistory(driver)
    transactionHistory.backPage()
    assert transactionHistory.openSuccessTab()
    
# def test_openBuyAgainInSuccessTab(driver):
#     transactionHistory = TransactionHistory(driver)
#     transactionHistory.openButtonMore()
#     assert transactionHistory.clickBuyAgain()
#     transactionHistory.backPage()    

# def test_openHelpCenterSuccessTab(driver):
#     transactionHistory = TransactionHistory(driver)
#     transactionHistory.openButtonMore()
#     assert transactionHistory.clickHelpCenter()
#     transactionHistory.backPage()

def test_openDetailSuccessTransactionHistory(driver):
    transactionHistory = TransactionHistory(driver)
    transactionHistory.backPage()
    assert transactionHistory.openDetailCardSuccess()