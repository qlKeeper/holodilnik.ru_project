import sys; sys.path.append('../holodilnik.ru_project')
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.smartphones_page import SmartphonesPage
from pages.cart_page import CartPage
from pages.refrigerators_page import RefrigeratorsPage
from pages.computers_page import Computer_page
import time


def test_filters(driver, date_time):

    hp = HeaderPage(driver)
    mp = MainPage(driver)
    computers = Computer_page(driver)
    cp = CartPage(driver)

    mp.open_url(mp.MAIN_URL)
    hp.click_computers_btn()
    items_info = [] # Для хранения имени товара и цены
    for i in range(2): # Указываем количество товаров для добавления в корзину
        items_info.append(computers.add_to_cart())
    time.sleep(3)