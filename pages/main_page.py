from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    # URL
    MAIN_URL = 'https://www.holodilnik.ru/'

    # Locators
    SMARTPHONE_BTN = (By.XPATH, '//a[text()="Смартфоны"]')

    # Actions
    def click_smartphone_btn(self, timeout=10):
        '''Открыть страницу со смартфонами'''
        
        Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
            (self.SMARTPHONE_BTN))).click()
        