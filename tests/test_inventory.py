import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages import LoginPage, InventoryPage
from selenium.common import TimeoutException

from variables_urls import valid_password, valid_username, url_cart_page, url_inventory_page

pytest.mark.usefixtures("driver")
class TestInventory:

    @staticmethod
    def initialization_function(driver):
        login_page = LoginPage(driver)
        login_page.login(valid_username,valid_password)
        inventory_page = InventoryPage(driver)
        return inventory_page


    def test_navigation_to_cart(self,driver):
        inventory_page = self.initialization_function(driver)
        inventory_page.click_cart_button()

        assert "cart.html" in driver.current_url, "Failed to navigate to cart page through cart icon."

    def test_navigation_from_cart_to_inventory(self, driver):
        inventory_page = self.initialization_function(driver)
        driver.get(url_cart_page)
        inventory_page.click_continue_shopping()

        assert "inventory.html" in driver.current_url, "Failed to navigate to inventory through continue shopping button."

    @pytest.mark.parametrize("item_index",range(6))
    def test_add_to_cart_change_to_remove(self,driver, item_index):
        inventory_page = self.initialization_function(driver)
        driver.get(url_inventory_page)
        add_to_cart_buttons = driver.find_elements(inventory_page.add_to_cart_buttons)
        try:
            current_button = add_to_cart_buttons[item_index]
            inventory_page.scroll_to_element(current_button)
            current_button.click()

            assert inventory_page.get_text(current_button) == "Remove"
        except AssertionError:
            pytest.fail(f"Failed to switch to remove text for item: {item_index}")


