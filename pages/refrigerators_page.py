from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as Action
import random


class RefrigeratorsPage(BasePage):

    # URL
    REFRIGERATORS_URL = 'https://www.holodilnik.ru/refrigerator/'

    def add_co_cart(self, timeout=5) -> tuple:

        '''Метод добавляет случайный холодильник в корзину из первой страницы, 
        возвращает его название и цену'''

        TO_CART_BTN = (By.XPATH, '//div[@class="add2cart2"]')
        REFRIGERATOR_NAME = (By.XPATH, '//a[@class="m-product__header-title"]')
        REFRIGERATOR_PRICE = (By.XPATH, '//div[@class="m-product__price-total"]')
        CONTINUE_SHOPPING = (By.XPATH, \
                             '//div[@class="button button--outline_cerulean"]')
        
        refrigerators = Wait(self.driver, timeout)\
            .until(EC.visibility_of_all_elements_located((TO_CART_BTN)))
        Action(self.driver, timeout)\
            .move_to_element(refrigerators[random.randint(0, len(refrigerators) - 1)])\
                .click().perform()
        
        refrigerator_name :str = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((REFRIGERATOR_NAME))).text
        refrigerator_price :str = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((REFRIGERATOR_PRICE))).text
        
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (CONTINUE_SHOPPING))).click()
        
        
        return refrigerator_name.strip(), \
            int(refrigerator_price.replace('₽', '').replace(' ', '').strip())