import sys; sys.path.append('../holodilnik.ru_project')
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.smartphones_page import SmartphonesPage
from pages.cart_page import CartPage
from pages.refrigerators_page import RefrigeratorsPage
from pages.computers_page import Computer_page
import time, random


def test_filters(driver, date_time):

    header_p = HeaderPage(driver)
    main_p = MainPage(driver)
    computers_p = Computer_page(driver)
    cart_p = CartPage(driver)

    main_p.open_url(main_p.MAIN_URL)
    header_p.click_computers_btn()
    computers_p.out_of_stock_checkbox()
    computers_p.change_price_filter(10000, random.randint(20000, 100000))
    computers_p.vendor_selected()
    time.sleep(10)