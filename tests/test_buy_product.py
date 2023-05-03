import sys; sys.path.append('../holodilnik.ru_project')
from pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By

def test_buy_product(driver):
    bs = BasePage(driver)
    bs.open(bs.BASE_URL)
    bs.authorization()
    time.sleep(2)
