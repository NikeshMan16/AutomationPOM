from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.hamburger_menu = (By.ID, 'react-burger-menu-btn')
        self.logout_button = (By.ID, 'logout_sidebar_link')


    def logout_function(self):
        self.wait.until(EC.visibility_of_element_located(self.hamburger_menu)).click()
        self.wait.until(EC.visibility_of_element_located(self.logout_button))

