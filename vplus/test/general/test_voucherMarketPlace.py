from vplus.pages.loginPage import LoginPage
from vplus.pages.voucherPage import VoucherPage
from vplus.utils.setup import SetupDriver
from vplus.utils.setup import platform
import pytest

@pytest.fixture(scope="function")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()
    
def test_goHelpCenter(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    voucher = VoucherPage(driver)
    assert voucher.goVoucher()
    assert voucher.goHelpCenter()

def test_goTokopedia(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    voucher = VoucherPage(driver)
    assert voucher.goVoucher()
    voucher = VoucherPage(driver)
    assert voucher.goTokopedia()

# Get blocked website from blibli
# def test_goBlibi(driver):
#     login = LoginPage(driver)
#     role = "FreeUser"
#     login.loginProcess(driver, role)
#     voucher = VoucherPage(driver)
#     assert voucher.goVoucher()
#     voucher = VoucherPage(driver)
#     assert voucher.goBlibi()
    
def test_goLazada(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    voucher = VoucherPage(driver)
    assert voucher.goVoucher()
    voucher = VoucherPage(driver)
    assert voucher.goLazada()
    
def test_goCodashop(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    voucher = VoucherPage(driver)
    assert voucher.goVoucher()
    voucher = VoucherPage(driver)
    assert voucher.goCoda()