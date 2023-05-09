import pytest
from selenium import webdriver
from datetime import datetime

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.fixture()
def date_time():
    print(f"\nТест запущен {datetime.now().strftime('%m.%d.%Y - %H:%M:%S')}")
    yield
    print(f"\nТест закончен {datetime.now().strftime('%m.%d.%Y - %H:%M:%S')}")