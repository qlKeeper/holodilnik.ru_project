import sys; sys.path.append('../holodilnik.ru_project')
from pages.main_page import MainPage
import time
from selenium.webdriver.common.by import By

def test_buy_product(driver):
    mp = MainPage(driver)
    mp.open(mp.MAIN_URL)
    mp.authorization()
    mp.select_city()
    time.sleep(2)
