from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SmartphonesPage(BasePage):

    SMARTPHONES_URL = 'https://holodilnik.ru/smartphones_gadgets/smartphones/'