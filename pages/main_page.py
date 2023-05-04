from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    # URLs
    MAIN_URL = 'https://www.holodilnik.ru/'

    # Locators
    SMARTPHONE_BTN = (By.XPATH, '//a[text()="Смартфоны"]')
    SELECT_CITY_BTN = (By.XPATH, '//span[@data-smoke="change-region__header"]')

    # Actions
    def click_smartphone_btn(self, timeout=10):
        '''Открыть страницу со смартфонами'''
        
        Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
            (self.SMARTPHONE_BTN))).click()


    def select_city(self, city="Москва и область", timeout=10):
        '''Открывает список городов, вторым аргументом можно передать название
        города. Если город есть в списке выбирает его, если нет то Москва'''
        
        FIELD_INPUT_CITY = (By.XPATH, '//input[@class="field-control__input"]')
        CITY_SELECT_CONFIRMATION = (By.XPATH, f'//div[@data-default="{city}"]')
        DEFAULT_CITY = (By.XPATH, '//a[@onclick="return changeRegion(1, false);"]')
        
        Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
            (self.SELECT_CITY_BTN))).click()

        try:
            Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
                (FIELD_INPUT_CITY))).send_keys(city)
        
            Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
                (CITY_SELECT_CONFIRMATION))).click()
        except:
            Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
                (FIELD_INPUT_CITY))).clear()
            
            Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
                (DEFAULT_CITY))).click()
            