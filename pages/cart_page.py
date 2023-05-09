from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class CartPage(BasePage):

    # URL
    CART_URL = 'https://www.holodilnik.ru/usercp/orders/'
    
    # Metods
    def clear_cart(self, timeout=10):

        '''Метод очищает корзину от всех товаров'''

        CLEAR_BTN = (By.XPATH, '//span[text()="Очистить корзину"]')
        DELETE_BTN = (By.XPATH, \
                      '//button[@onclick="appBasket.basketClearProceed()"]')
        EMPTY_CART = (By.XPATH, '//div[@class="basket__empty"]')

        try:    
            Wait(self.driver, timeout=2)\
                .until(EC.invisibility_of_element_located((EMPTY_CART)))
            Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
                (CLEAR_BTN))).click()
            Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
                (DELETE_BTN))).click()
        except:
            return
    
    def check_items_in_cart(self, items_info, timeout=10):

        '''Метод проверяет соответсивие товаров в корзине, имена товаров, цену 
        и итоговую сумму. Первым аргументом принимает список выбранных товаров 
        из функции add_to_cart()'''

        ITEMS_NAME = (By.XPATH, '//a[@class="basket__items-element-name-link"]')
        ITEMS_PRICE = (By.XPATH, '//span[@data-basket-element-total]')
        TOTAL_PRICE = (By.XPATH, '//div/span[@data-basket-total]')

        names = Wait(self.driver, timeout)\
                    .until(EC.visibility_of_all_elements_located((ITEMS_NAME)))
        
        prices = Wait(self.driver, timeout)\
                    .until(EC.visibility_of_all_elements_located((ITEMS_PRICE)))
        
        total_price_in_cart = Wait(self.driver, timeout)\
                    .until(EC.visibility_of_element_located((TOTAL_PRICE)))
        
        cart_names = True
        i = 0
        for name in names:
            if not (name.text == items_info[i][0]):
                cart_names = False
            i += 1
        else:
            assert cart_names, 'Product names do not match'

        cart_price = True
        i = 0
        for price in prices:
            if not (int(price.text.replace(' ', '')) == items_info[i][1]):
                cart_price = False
            i += 1
        else:
            assert cart_price, 'Product prices do not match'

        total_price_in_items = 0
        i = 0
        for price in items_info:
            total_price_in_items += items_info[i][1]
            i += 1
        else:
            assert int(total_price_in_cart.text.replace(' ', '')) == \
                total_price_in_items, "Product total prices do not match"

        if BasePage.authorized:
            self.clear_cart()
