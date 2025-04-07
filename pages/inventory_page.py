from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.cart_icon = (By.ID,'shopping_cart_container')
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.continue_shopping = (By.ID,'continue-shopping')
        self.inventory_items = (By.CLASS_NAME, 'inventory_item')
        self.item_name =(By.CLASS_NAME, "inventory_item_name")

        self.add_to_cart_buttons =(By.XPATH,"//button[contains(text(),'Add to cart')]")
        self.remove_from_cart_buttons = (By.XPATH, "//button[contains(text(),'Remove')]")

        self.hamburger_menu = (By.ID, 'react-burger-menu-btn')
        self.logout_button = (By.ID, 'logout_sidebar_link')

        self.select_container = (By.CLASS_NAME, 'select_container')
        self.product_sort_container = (By.CLASS_NAME, 'product_sort_container')
        self.item_price = (By.CLASS_NAME, 'inventory_item_price')




    def logout_function(self):
        self.wait.until(EC.visibility_of_element_located(self.hamburger_menu)).click()
        self.wait.until(EC.visibility_of_element_located(self.logout_button))

    def click_cart_button(self):
        self.wait.until(EC.visibility_of_element_located(self.cart_icon))

    def click_continue_shopping(self):
        self.wait.until(EC.visibility_of_element_located(self.continue_shopping))


    def select_container(self,visible_text):
        self.wait.until(EC.visibility_of_element_located(self.select_container))
        self.select_dd(self.product_sort_container,visible_text)




