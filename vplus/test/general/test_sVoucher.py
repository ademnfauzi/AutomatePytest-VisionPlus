from vplus.pages.liveTvPage import TvPage
from vplus.pages.loginPage import LoginPage
from vplus.pages.originalsPage import OriginalsPage
from vplus.pages.programGuidePage import PageProgramGuide
from vplus.pages.voucherPage import VoucherPage
from vplus.utils.setup import SetupDriver
from vplus.testdata.hash import encodeDecodePassword
from vplus.utils.setup import platform
import pytest
import json
from vplus.test.general.user import users

@pytest.fixture(scope="module")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_start(driver):
    login = LoginPage(driver)
    hashPassword = encodeDecodePassword()
    # login.open()
    with open('vplus/testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    password = data['FreeUser'][0]["password"]
    stringDecode = hashPassword.decode(password)
    username = users.getUsername()
    print(username)
    login.clickLogin(username, stringDecode)
    login.skipCreateAvatar()
    
def test_goVoucherPage(driver):
    voucher = VoucherPage(driver)
    assert voucher.goVoucher()
        
def test_inputInvalidCodeVoucher(driver):
    voucher = VoucherPage(driver)
    inputVoucher = "aBcDeFgHiJkLmNoPqRsTuVwXyZ12345678900"
    assert voucher.inputInvalidVoucher(inputVoucher)
    
def test_inputUniqCodeVoucher(driver):
    voucher = VoucherPage(driver)
    inputVoucher = "PRODU2PO4L5KIYUNIQ"
    voucher.clearInputVoucher()
    assert voucher.inputUniqVoucher(inputVoucher)
    
def test_inputNotStartedCodeVoucher(driver):
    voucher = VoucherPage(driver)
    inputVoucher = "EXPLXBT6YPERLBAS"
    voucher.clearInputVoucher()
    assert voucher.inputInvalidVoucher(inputVoucher)
    
def test_inputExpiredCodeVoucher(driver):
    voucher = VoucherPage(driver)
    inputVoucher = "PRODWTF8U8MZ1WEXP"
    voucher.clearInputVoucher()
    assert voucher.inputExpiredVoucher(inputVoucher)
    
def test_inputQuotaHasRunOutCodeVoucher(driver):
    voucher = VoucherPage(driver)
    inputVoucher = "AKTP9LMV26QT9BAS"
    voucher.clearInputVoucher()
    assert voucher.inputInvalidVoucher(inputVoucher)
    
def test_inputSuccessCodeVoucher(driver):
    voucher = VoucherPage(driver)
    inputVoucher = "IKINGGH2WFXO3PREM"
    voucher.clearInputVoucher()
    assert voucher.inputSuccessVoucher(inputVoucher)
    
def test_inputHasBeenRedeemedCodeVoucher(driver):
    voucher = VoucherPage(driver)
    inputVoucher = "IKINGGH2WFXO3PREM"
    voucher.backPage()
    assert voucher.inputUniqVoucher(inputVoucher)

# is being removed 
def test_checkBuyPackageAfterReedemVoucher(driver):
    voucher = VoucherPage(driver)
    assert voucher.checkBuyPackageActive()
    
def test_checkWatchPremiumLiveTvAfterReedemVoucher(driver):
    voucher = VoucherPage(driver)
    tv = TvPage(driver)
    program = PageProgramGuide(driver)
    originals = OriginalsPage(driver)
    voucher.backToTabMain()
    originals.refresh()
    program.clickNavProgramGuidance()
    assert program.checkLiveTvPremium()
    assert tv.assertTvPlay()

def test_checkPremiumVodAfterReedemVoucher(driver):
    originals = OriginalsPage(driver)
    originals.goOriginals()
    originals.clickCardVODOriginals()
    originals.clickEpsThree()
    originals.clickButtonWatch()
    assert originals.assertPlayVOD()