from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage:
    
    def __init__(self, driver) -> None:
        self.driver = driver
    
    
    # Метод открытия нужного url
    def open_url(self, url: str):
        '''Открывает нужный URL переданный первым аргументом'''

        self.driver.get(url)
    
    
    # Метод авторизации на сайте
    def authorization(self, timeout=10):
        '''Проходит авторизацию на сайте'''
        
        LOGIN = 'howiv20780@syinxun.com'
        PASSWORD = '159000test'
        
        BTN_LOGIN = (By.XPATH, '//span[text()="Войти"]')
        BTN_FORM_LINK = (By.XPATH, '//a[@class="form__link"]')
        BTN_PASSWORD = (By.XPATH, "//button[text()='По паролю']")
        LOGIN_FIELD = (By.XPATH, '//input[@id="phoneORemail_id"]')
        PASSWORD_FIELD = (By.XPATH, '//input[@id="password_id"]')
        FINAL_BTN = (By.XPATH, '//button[@id="btn_id"]')

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
        time.sleep(1)


    def select_city(self, city="Москва и область", timeout=10):
        '''Открывает список городов, вторым аргументом можно передать название
        города. Если город есть в списке выбирает его, если нет то Москва'''
        
        SELECT_CITY_BTN = (By.XPATH, '//span[@data-smoke="change-region__header"]')
        FIELD_INPUT_CITY = (By.XPATH, '//input[@class="field-control__input"]')
        CITY_SELECT_CONFIRMATION = (By.XPATH, f'//div[@data-default="{city}"]')
        DEFAULT_CITY = (By.XPATH, '//a[@onclick="return changeRegion(1, false);"]')
        
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