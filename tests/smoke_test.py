import sys; sys.path.append('../holodilnik.ru_project')
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.smartphones_page import SmartphonesPage
import time


def test_buy_product(driver):
    
    mp = MainPage(driver)
    mp.open_url(mp.MAIN_URL)
    
    hp = HeaderPage(driver)
    hp.authorization()
    hp.select_city()
    hp.click_smartphone_btn()
    
    sp = SmartphonesPage(driver)
    sp.add_to_cart()
    hp.go_to_cart()
    time.sleep(3)
