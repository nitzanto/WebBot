from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get("https://www.booking.com")
