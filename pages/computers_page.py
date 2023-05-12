from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains as Action
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
            .move_to_element(computers[random.randint(0, len(computers) - 1)])\
                .click().perform()
        
        computer_name :str = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((COMPUTER_NAME))).text
        computer_price :str = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((COMPUTER_PRICE))).text
        
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (CONTINUE_SHOPPING))).click()
        
        return computer_name.strip(), \
            int(computer_price.replace('₽', '').replace(' ', '').strip())
    
    
    def change_price_filter(self, min_price: int, max_price: int, timeout=5):

        '''Метод меняет мин и макс цену в фильтре подбора товара'''

        MIN_PRICE_FILD = (By.XPATH, '//input[@id="min_txt_price"]')
        MAX_PRICE_FILD = (By.XPATH, '//input[@id="max_txt_price"]')
        APPLY_BTN = (By.XPATH, '//input[@id="cfilter_btnsubmit"]')

        min_price_fild = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((MIN_PRICE_FILD)))
        max_price_fild = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((MAX_PRICE_FILD)))
        

        for i in range(10):
            min_price_fild.send_keys(Keys.BACKSPACE)
        else:
            min_price_fild.send_keys(min_price)
            max_price_fild.clear()
            max_price_fild.send_keys(max_price)
            max_price_fild.send_keys(Keys.ENTER)
            Wait(self.driver, timeout)\
                .until(EC.visibility_of_element_located((APPLY_BTN))).click()
    
    
    def out_of_stock_checkbox(self, timeout=5):
        
        '''Метод отмечает checkbox Cкрыть товары со статусом "Нет в наличии"'''

        CHECKBOX = (By.XPATH, '//label[@id="cfilter_1324_st_1_hidden_label"]')
        APPLY_BTN = (By.XPATH, '//input[@id="cfilter_btnsubmit"]')
        checkbox = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((CHECKBOX)))
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        checkbox.click()
        Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((APPLY_BTN))).click()
        

    def vendor_selected(self, timeout=5):
        
        '''Метод выбирает случайно доступного производителя из фильтра'''

        APPLY_BTN = (By.XPATH, '//input[@id="cfilter_btnsubmit"]')
        VENDORS = (By.XPATH, \
        '//div[@id="filter-c-item_vendor"]//label[@class="field-checkbox__label form-check-label beforeSelect"]')

        vendors_checkbox = Wait(self.driver, timeout)\
            .until(EC.visibility_of_all_elements_located((VENDORS)))
        vendor_checkbox = vendors_checkbox[random.randint(0, \
                                    len(vendors_checkbox) - 1)]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", \
                                   vendor_checkbox)
        vendor_checkbox.click()
        Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((APPLY_BTN))).click()