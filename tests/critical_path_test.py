import sys; sys.path.append('../holodilnik.ru_project')
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.smartphones_page import SmartphonesPage
from pages.cart_page import CartPage
from pages.refrigerators_page import RefrigeratorsPage
import time


def test_filters(driver, date_time):

    hp = HeaderPage(driver)
    mp = MainPage(driver)
    
    cp = CartPage(driver)

    mp.open_url(mp.MAIN_URL)
    hp.click_computers_btn()
    time.sleep(3)