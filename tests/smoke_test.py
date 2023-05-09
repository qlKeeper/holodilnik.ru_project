import sys; sys.path.append('../holodilnik.ru_project')
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.smartphones_page import SmartphonesPage
from pages.cart_page import CartPage
import time


def test_buy_product(driver):
    
    hp = HeaderPage(driver)
    mp = MainPage(driver)
    sp = SmartphonesPage(driver)
    cp = CartPage(driver)
    
    mp.open_url(mp.MAIN_URL)
    hp.authorization()
    hp.go_to_cart()
    cp.clear_cart()
    hp.select_city()
    hp.click_smartphone_btn()
    
    items_info = [] # Для хранения имени товара и цены
    for i in range(2): # Указываем количество товаров для добавления в корзину
        items_info.append(sp.add_to_cart())
    
    hp.go_to_cart()
    cp.check_items_in_cart(items_info)
    time.sleep(2)
