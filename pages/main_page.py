from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    # URL
    MAIN_URL = 'https://www.holodilnik.ru/'
    
    def check_new_comment(self, timeout=5):
        
        '''Метод проверяет новые отзывы на главной станице'''
        
        NEW_COMMENT_BTN = (By.XPATH, '//a[@href="#item-new-reviews"]')
        TEXT_COMMENT = (By.XPATH, '//div[@id="item-new-reviews"]//p')
        PRODUCT_LINK = (By.XPATH, '//div[@id="item-new-reviews"]//a')
        PRODUCT_COMMENT_BTN = (By.XPATH, '//a[@href="#item-reviews"]')

        new_comment_btn = Wait(self.driver, 5)\
            .until(EC.visibility_of_element_located((NEW_COMMENT_BTN)))
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", new_comment_btn)
        new_comment_btn.click()

        text_comment = Wait(self.driver, 5)\
            .until(EC.visibility_of_element_located((TEXT_COMMENT))).text
        
        return text_comment
