from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class BasePage:
    
    authorized = False # Была ли авторизация на сайте
    
    def __init__(self, driver) -> None:
        self.driver = driver
    
    
    def open_url(self, url: str):
        
        '''Открывает нужный URL переданный первым аргументом'''

        self.driver.get(url)
        self.driver.add_cookie({'name': '_defnice', 'value': '1'}) # Accept
    
    def take_screenshot(self):
        
        '''Метод делает скриншот'''
        
        now_date = datetime.now().strftime('%m.%d.%Y - %H:%M:%S')
        name_screenshot = f'screenshot[{now_date}].png'
        self.driver.save_screenshot('screenshots/' + name_screenshot)