from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage:
    
    def __init__(self, driver) -> None:
        self.driver = driver
    
    
    # Метод открытия нужного url
    def open(self, url: str):
        self.driver.get(url)
    
    
    # Метод авторизации на сайте
    def authorization(self, timeout=10):
        
        LOGIN = 'howiv20780@syinxun.com'
        PASSWORD = '159000test'
        
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (By.XPATH, '//span[text()="Войти"]'))).click()
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (By.XPATH, '//a[@class="form__link"]'))).click()
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (By.XPATH, "//button[text()='По паролю']"))).click()
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (By.XPATH, '//input[@id="phoneORemail_id"]'))).send_keys(LOGIN)
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (By.XPATH, '//input[@id="password_id"]'))).send_keys(PASSWORD)
        Wait(self.driver, timeout).until(EC.element_to_be_clickable(\
            (By.XPATH, '//button[@id="btn_id"]'))).click()
        time.sleep(1)
        