import sys; sys.path.append('../holodilnik.ru_project')
from pages.main_page import MainPage
import time

def test_buy_product(driver):
    mp = MainPage(driver)
    mp.open_url(mp.MAIN_URL)
    mp.authorization()
    mp.select_city()
    time.sleep(2)
