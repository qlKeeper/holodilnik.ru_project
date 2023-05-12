from selenium.webdriver.common.action_chains import ActionChains as Action
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

with webdriver.Chrome() as driver:
    
    driver.maximize_window()
    driver.get('https://www.holodilnik.ru/digital_tech/computers/')
    
    acer_checkbox = Wait(driver, 3)\
        .until(EC.visibility_of_element_located(\
            (By.XPATH, '//label[@id="cfilter_1324_vendor_1_label"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", acer_checkbox)
    acer_checkbox.click()
    # Action(driver).move_to_element(acer_checkbox).click().perform()
    submit_btn = driver.find_element(By.XPATH, '//input[@id="cfilter_btnsubmit"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", acer_checkbox)
    
    
    time.sleep(4)