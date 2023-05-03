

class BasePage:
    
    def __init__(self, driver, url: str) -> None:
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
    