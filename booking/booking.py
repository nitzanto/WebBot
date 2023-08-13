from selenium.webdriver.common.by import By

import booking.constants as const
import os
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown  # Context Manager
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)  # Until element is found in the website
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()
