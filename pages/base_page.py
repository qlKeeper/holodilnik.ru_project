from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class BasePage:
    
    authorized = False # Была ли авторизация на сайте
    
    def __init__(self, driver) -> None:
        self.driver = driver
    
    
    def open_url(self, url: str):
        
        '''Открывает нужный URL переданный первым аргументом'''

        self.driver.get(url)
    