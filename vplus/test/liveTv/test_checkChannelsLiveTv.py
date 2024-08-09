from vplus.pages.liveTvPage import TvPage
from vplus.pages.loginPage import LoginPage
from vplus.pages.originalsPage import OriginalsPage
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
    originals = OriginalsPage(driver)
    role = "PremiumSportUser"
    login.loginProcess(driver, role)
    originals.handleMaximumDevice()
    
def test_channelsRCTI(driver):
    tv = TvPage(driver)
    tv.goTvPage()
    assert tv.assertTvPlay()
    # tv.assertTvPause()
    # tv.tvCloseVideoPaused()
    
def test_channelsMncTv(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("MNCTV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()

def test_channelsGtv(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("GTV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsINews(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("iNews")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsSindoNews(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("SindoNews")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsTransTv(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Trans TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsTrans7(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Trans 7")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsANTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("ANTV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsRTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("RTV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsTVOne(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("TVOne")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsKompasTv(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Kompas TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsMetroTv(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Metro TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsBTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("BTV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsTVRI(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("TVRI")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsSeaToday(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("SEA Today")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsDAAITv(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("DAAI TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsNetTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Net TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsJakTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("JAK TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsBaliTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Bali TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsBandungTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Bandung TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsTV9(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("TV 9")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsTawaf(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Tawaf")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsTVMU(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("TV MU")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsTV9(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("TV 9")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCinemachi(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Cinemachi")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCinemachiKids(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Cinemachi Kids")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCinemachiXtra(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Cinemachi Xtra")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCinemachiMax(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Cinemachi Max")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCinemachiAction(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Cinemachi Action")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsThrill(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Thrill")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsHitsMovies(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Hits Movies")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
# def test_channelsCinemaWorld(driver):
#     tv = TvPage(driver)
#     tv.tvSearchAny("Cinema World")
#     tv.refresh()
#     tv.checkBtnPause()
#     assert tv.assertTvPlay()

def test_channelsCelestialMovies(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Celestial Movies")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCCM(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("CCM")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCCM(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("TVN Movies")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsZeeBioskop(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Zee Bioskop")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsMyFamilyChannel(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("My Family Channel")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsMyCinema(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("My Cinema")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsMyCinemaAsia(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("My Cinema Asia")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsKidsTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Kids TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()

def test_channelsMoonbug(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Moonbug")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()    
    
def test_channelsCbeebies(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Cbeebies")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsNickJr(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Nick Jr")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsZooMoo(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Zoo Moo")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
# Need alone search function
def test_channelsNick(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("64")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsAnimax(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Animax")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsMyKidz(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("My Kidz")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsDreamWorks(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Dream Works")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsFoodTravel(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Food Travel")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsOKTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("OK TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsEntertainment(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Entertainment")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
# Need alone function
def test_channelsTVN(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("73")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
# Need alone function
def test_channelsOne(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("74")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
# Need alone function
def test_channelsKix(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("75")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
# def test_channelsNHKWorldPremium(driver):
#     tv = TvPage(driver)
#     tv.tvSearchAny("NHK World Premium")
#     tv.refresh()
#     tv.checkBtnPause()
#     assert tv.assertTvPlay()
    
# Need alone function
def test_channelsHits(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("77")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsAXN(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("AXN")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsLifetime(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Lifetime")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsVisionPrime(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Vision Prime")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCelebritiesTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Celebrities TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsOkezoneTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("89")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsRockEntertainment(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Rock Entertainment")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsRockAction(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Rock Action")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCrimeInvestigation(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Crime Investigation")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsOutdoorChannel(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Outdoor Channel")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsBBCEarth(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("BBC Earth")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsGlobalTrekker(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Global Trekker")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsHistory(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("History")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsLoveNature(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("LoveNature")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()

def test_channelsSportstars(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Sportstars")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsSportstars2(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Sportstars 2")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsSoccerChannel(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Soccer Channel")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()

def test_channelsSpoTV1(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("SpoTV1")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsSpoTV2(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("SpoTV2")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsIDX(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("IDX")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsBBCWorldNews(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("BBC World News")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsMuslimTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Muslim TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
# Need alone function
def test_channelsLife(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("138")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsReformed21(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Reformed 21")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsMusicTv(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Music TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsMTVLive(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("MTV Live")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsMTV90s(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("MTV 90s")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsDW(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("DW")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsFrance24(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("France 24")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsTRTWorld(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("TRT World")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsAljazeera(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Aljazeera")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsRT(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("150")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsChannelNewsAsia(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Channel News Asia")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsAlQuranAlKareem(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Al Quran Al Kareem")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsEWTN(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("EWTN")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCGTNDocumentary(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("CGTN Documentary")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsCGTN(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("156")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsAnhui(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Anhui")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsXingKongTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Xing kong TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsShanghaiDragonTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Shanghai Dragon TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsHunanTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Hunan TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsJiangsuTV(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Jiangsu TV")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsNHKWorldJapan(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("162")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsTV5Monde(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("TV5Monde")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsArirang(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("Arirang")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsDENSFoodChannel(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("DENS Food Channel")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsDENSPlayChannel(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("DENSPlay Channel")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
def test_channelsDENSShowbiz(driver):
    tv = TvPage(driver)
    tv.tvSearchAny("DENS Showbiz")
    tv.refresh()
    tv.checkBtnPause()
    assert tv.assertTvPlay()
    
# def test_channelsVPlusLive(driver):
#     tv = TvPage(driver)
#     tv.tvSearchAny("V+ LIVE")
#     tv.refresh()
#     tv.checkBtnPause()
#     assert tv.assertTvPlay()
    
# def test_channelsRPlusLive(driver):
#     tv = TvPage(driver)
#     tv.tvSearchAny("R+ LIVE")
#     tv.refresh()
#     tv.checkBtnPause()
#     assert tv.assertTvPlay()
    
# def test_channelsVPlusLive2(driver):
#     tv = TvPage(driver)
#     tv.tvSearchAny("V+ LIVE 2")
#     tv.refresh()
#     tv.checkBtnPause()
#     assert tv.assertTvPlay()

# def test_channelsVPlusSports(driver):
#     tv = TvPage(driver)
#     tv.tvSearchAny("V+ SPORTS")
#     tv.refresh()
#     tv.checkBtnPause()
#     assert tv.assertTvPlay()
    
# def test_channelsVPlusLive3(driver):
#     tv = TvPage(driver)
#     tv.tvSearchAny("V+ LIVE 3")
#     tv.refresh()
#     tv.checkBtnPause()
#     assert tv.assertTvPlay()
    
# def test_channelsVPlusLive4(driver):
#     tv = TvPage(driver)
#     tv.tvSearchAny("V+ LIVE 4")
#     tv.refresh()
#     tv.checkBtnPause()
#     assert tv.assertTvPlay()