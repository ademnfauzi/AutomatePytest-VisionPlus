import pytest
from vplus.pages.favoriteChannelsPage import FavoriteChannelsPage
from vplus.pages.liveTvPage import TvPage
from vplus.pages.loginPage import LoginPage
from vplus.pages.originalsPage import OriginalsPage
from vplus.utils.setup import SetupDriver
from vplus.utils.setup import platform


@pytest.fixture(scope="function")
def driver(platform):
    setup_driver = SetupDriver(browser=platform)
    yield setup_driver.get_driver()
    setup_driver.driver.quit()

def test_addFavoriteChannels(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)    
    favChannels = FavoriteChannelsPage(driver)
    originals = OriginalsPage(driver)
    originals.handleMaximumDevice()
    favChannels.clickIconSettings()
    favChannels.clickSettings()
    favChannels.clickConfigureProfile()
    favChannels.clickProfile()
    favChannels.clickConfigureFavChannels()
    assert favChannels.clickAnyCardToAddFavChannels("RCTI")
    assert favChannels.clickButtonCancel()
    favChannels.clickConfigureFavChannels()
    assert favChannels.clickAnyCardToAddFavChannels("RCTI")
    favChannels.removeInputSearchChannels()
    assert favChannels.clickAnyCardToAddFavChannels("Trans")
    favChannels.removeInputSearchChannels()
    assert favChannels.clickAnyCardToAddFavChannels("Sport")
    assert favChannels.clickButtonSave()
    favChannels.refresh()
    tv = TvPage(driver)
    tv.goTvPage()
    assert tv.checkFavChannels()
    
def test_removeFavoriteChannels(driver):
    login = LoginPage(driver)
    role = "FreeUser"
    login.loginProcess(driver, role)
    favChannels = FavoriteChannelsPage(driver)
    favChannels.clickIconSettings()
    favChannels.clickSettings()
    favChannels.clickConfigureProfile()
    favChannels.clickProfile()
    favChannels.clickConfigureFavChannels()
    assert favChannels.clickAnyCardToRemoveFavChannels("RCTI")
    favChannels.removeInputSearchChannels()
    assert favChannels.clickAnyCardToRemoveFavChannels("Trans")
    favChannels.removeInputSearchChannels()
    assert favChannels.clickAnyCardToRemoveFavChannels("Sport")
    favChannels.removeInputSearchChannels()
    assert favChannels.clickButtonSave()
    favChannels.refresh()
        