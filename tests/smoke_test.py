import sys; sys.path.append('../holodilnik.ru_project')
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.smartphones_page import SmartphonesPage
from pages.cart_page import CartPage
import time


def test_buy_product(driver):
    
    mp = MainPage(driver)
    mp.open_url(mp.MAIN_URL)
    hp = HeaderPage(driver)
    hp.authorization()
    hp.select_city()
    hp.click_smartphone_btn()
    
    sp = SmartphonesPage(driver)
    items_info = []
    for i in range(2):
        time.sleep(0.5)
        items_info.append(sp.add_to_cart())
    hp.go_to_cart()

    cp = CartPage(driver)
    cp.check_items_in_cart(items_info)
    time.sleep(3)
