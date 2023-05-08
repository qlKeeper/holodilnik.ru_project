from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class SmartphonesPage(BasePage):

    # URL
    SMARTPHONES_URL = 'https://holodilnik.ru/smartphones_gadgets/smartphones/'

    
    def add_to_cart(self, timeout=10) -> tuple:
        
        '''Добавляет случайный смартфон в корзину из первой страницы, возвращает его
        название и цену'''
        
        TO_CART_BTN = (By.XPATH, '//div[@class="add2cart2"]')
        SMARTPHONE_NAME = (By.XPATH, '//a[@class="m-product__header-title"]')
        SMARTPHONE_PRICE = (By.XPATH, '//div[@class="m-product__price-total"]')
        CONTINUE_SHOPPING = (By.XPATH, \
                             '//div[@class="button button--outline_cerulean"]')
        
        smartphones = Wait(self.driver, timeout)\
            .until(EC.visibility_of_all_elements_located((TO_CART_BTN)))
        
        smartphones[random.randint(0, 23)].click()
        phone_name = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((SMARTPHONE_NAME))).text
        phone_price = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((SMARTPHONE_PRICE))).text
        
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (CONTINUE_SHOPPING))).click()
        
        
        return phone_name, phone_price
