from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains as Action
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class HeaderPage(BasePage):

    def authorization(self, timeout=3):
        
        '''Проходит авторизацию на сайте'''
        
        LOGIN = 'howiv20780@syinxun.com'
        PASSWORD = '159000test'
        
        BTN_LOGIN = (By.XPATH, '//span[text()="Войти"]')
        BTN_FORM_LINK = (By.XPATH, '//a[@class="form__link"]')
        BTN_PASSWORD = (By.XPATH, '//button[@data-smoke="AuthByPasswdBtn"]')
        LOGIN_FIELD = (By.XPATH, '//input[@id="phoneORemail_id"]')
        PASSWORD_FIELD = (By.XPATH, '//input[@id="password_id"]')
        FINAL_BTN = (By.XPATH, '//button[@id="btn_id"]')

        self.driver.execute_script("window.scrollBy(0,-5000)")

        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (BTN_LOGIN))).click()
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (BTN_FORM_LINK))).click()
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (BTN_PASSWORD))).click()
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (LOGIN_FIELD))).send_keys(LOGIN)
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (PASSWORD_FIELD))).send_keys(PASSWORD)
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (FINAL_BTN))).click()
        
        BasePage.authorized = True
        
        time.sleep(1)


    def select_city(self, city="Москва и область", timeout=2):
        
        '''Открывает список городов, вторым аргументом можно передать название
        города. Если город есть в списке выбирает его, если нет, то по умолчанию'''
        
        SELECT_CITY_BTN = (By.XPATH, '//span[@data-smoke="change-region__header"]')
        FIELD_INPUT_CITY = (By.XPATH, '//input[@class="field-control__input"]')
        CITY_SELECT_CONFIRMATION = (By.XPATH, f'//div[@data-default="{city}"]')
        DEFAULT_CITY = (By.XPATH, '//a[@onclick="return changeRegion(1, false);"]')
        
        self.driver.execute_script("window.scrollBy(0,-5000)")

        Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
            (SELECT_CITY_BTN))).click()

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
            

    def go_to_cart(self, timeout=5):

        '''Переход в корзину'''

        CART_BTN = (By.XPATH, '//span[contains(text(), "Корзина")]')
        
        self.driver.execute_script("window.scrollBy(0,-5000)")
        
        Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
            (CART_BTN)))
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (CART_BTN))).click()


    def click_smartphone_btn(self, timeout=5):
        
        '''Открыть страницу со смартфонами'''
        
        SMARTPHONE_BTN = (By.XPATH, '//a[text()="Смартфоны"]')

        self.driver.execute_script("window.scrollBy(0,-5000)")
        
        Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
            (SMARTPHONE_BTN))).click()
        

    def click_refrigerators_btn(self, timeout=5):

        '''Метод открывает сраницу с холодильниками'''

        REFRIGERATORS_BTN = (By.XPATH, '//div/a[text()="Холодильники"]')

        self.driver.execute_script("window.scrollBy(0,-5000)")

        Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
            (REFRIGERATORS_BTN))).click()
        

    def click_computers_btn(self, timeout=5):

        '''Метод открывет страницу с компьютерами'''

        CATALOG_BTN = (By.XPATH, \
                       '//span[@class="site-header__search-burger-button-text"]')
        COMPUTER_LIST = (By.XPATH, \
                         '//a[@href="//www.holodilnik.ru/digital_tech/"]')
        SELECT_COMPUTER = (By.XPATH, '//a[@id="cm-1324"]')
        Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
            (CATALOG_BTN))).click()
        comp_list = Wait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((COMPUTER_LIST)))
        
        Action(self.driver).move_to_element(comp_list).perform()
        Wait(self.driver, timeout).until(EC.visibility_of_element_located(\
            (SELECT_COMPUTER))).click()

