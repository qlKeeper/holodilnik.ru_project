import sys; sys.path.append('../holodilnik.ru_project')
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.smartphones_page import SmartphonesPage
from pages.cart_page import CartPage
from pages.refrigerators_page import RefrigeratorsPage
from pages.computers_page import Computer_page
import time

# Смоук тест покупки смартфонов
def test_buy_smartphones(driver, date_time): 

    header_p = HeaderPage(driver)
    main_p = MainPage(driver)
    smartphones_p = SmartphonesPage(driver)
    cart_p = CartPage(driver)
    
    main_p.open_url(main_p.MAIN_URL)

    header_p.authorization()
    header_p.go_to_cart()
    cart_p.clear_cart()
    header_p.select_city()
    header_p.click_smartphone_btn()
    
    items_info = [] # Для хранения имени товара и цены
    for i in range(2): # Указываем количество товаров для добавления в корзину
        items_info.append(smartphones_p.add_to_cart())
    
    header_p.go_to_cart()
    cart_p.check_items_in_cart(items_info)
    cart_p.take_screenshot()
    time.sleep(2)

# Смоук тест покупки холодильников
def test_buy_refrigerators(driver, date_time): 
    
    header_p = HeaderPage(driver)
    main_p = MainPage(driver)
    refrigerators_p = RefrigeratorsPage(driver)
    cart_p = CartPage(driver)

    main_p.open_url(main_p.MAIN_URL)

    header_p.authorization()
    header_p.go_to_cart()
    cart_p.clear_cart()
    header_p.select_city()
    header_p.click_refrigerators_btn()
    
    items_info = [] # Для хранения имени товара и цены
    for i in range(2): # Указываем количество товаров для добавления в корзину
        items_info.append(refrigerators_p.add_co_cart())
    
    header_p.go_to_cart()
    cart_p.check_items_in_cart(items_info)
    cart_p.take_screenshot()
    time.sleep(2)

# Смоук тест покупки компьютеров
def test_buy_computers(driver, date_time):
    
    header_p = HeaderPage(driver)
    main_p = MainPage(driver)
    computer_p = Computer_page(driver)
    cart_p = CartPage(driver)

    main_p.open_url(main_p.MAIN_URL)

    header_p.authorization()
    header_p.go_to_cart()
    cart_p.clear_cart()
    header_p.select_city()
    header_p.click_computers_btn()

    items_info = [] # Для хранения имени товара и цены
    for i in range(2): # Указываем количество товаров для добавления в корзину
        items_info.append(computer_p.add_to_cart())
    
    header_p.go_to_cart()
    cart_p.check_items_in_cart(items_info)
    cart_p.take_screenshot()
    time.sleep(2)