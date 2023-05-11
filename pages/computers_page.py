from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains as Action
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, random

class Computer_page(BasePage):

    # URL
    COMPUTERS_URL = 'https://www.holodilnik.ru/digital_tech/computers/'
    
    def add_to_cart(self, timeout=5) -> tuple:
        
        '''Добавляет случайный компьютер в корзину из первой страницы, 
        возвращает его название и цену'''
        
        TO_CART_BTN = (By.XPATH, '//div[@class="add2cart2"]')
        COMPUTER_NAME = (By.XPATH, '//a[@class="m-product__header-title"]')
        COMPUTER_PRICE = (By.XPATH, '//div[@class="m-product__price-total"]')
        CONTINUE_SHOPPING = (By.XPATH, \
                             '//div[@class="button button--outline_cerulean"]')
        
        computers = Wait(self.driver, timeout)\
            .until(EC.visibility_of_all_elements_located((TO_CART_BTN)))
        Action(self.driver, timeout)\
            .move_to_element(computers[random.randint(0, 23)])\
                .click().perform()
        
        computer_name :str = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((COMPUTER_NAME))).text
        computer_price :str = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((COMPUTER_PRICE))).text
        
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (CONTINUE_SHOPPING))).click()
        
        return computer_name.strip(), \
            int(computer_price.replace('₽', '').replace(' ', '').strip())