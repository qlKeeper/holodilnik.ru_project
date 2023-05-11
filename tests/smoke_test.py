import sys; sys.path.append('../holodilnik.ru_project')
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.smartphones_page import SmartphonesPage
from pages.cart_page import CartPage
from pages.refrigerators_page import RefrigeratorsPage
import time

# Смоук тест покупки смартфонов
def test_buy_smartphones(driver, date_time): 

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
    cp.take_screenshot()
    time.sleep(2)

# Смоук тест покупки холодильников
def test_buy_refrigerators(driver, date_time): 
    hp = HeaderPage(driver)
    mp = MainPage(driver)
    rp = RefrigeratorsPage(driver)
    cp = CartPage(driver)

    mp.open_url(mp.MAIN_URL)

    hp.authorization()
    hp.go_to_cart()
    cp.clear_cart()
    hp.select_city()
    hp.click_refrigerators_btn()
    
    items_info = [] # Для хранения имени товара и цены
    for i in range(2): # Указываем количество товаров для добавления в корзину
        items_info.append(rp.add_co_cart())
    
    hp.go_to_cart()
    cp.check_items_in_cart(items_info)
    cp.take_screenshot()
    time.sleep(2)