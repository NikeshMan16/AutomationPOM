import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages import LoginPage, InventoryPage
from selenium.common import TimeoutException

from variables_urls import valid_password, valid_username, url_cart_page, url_inventory_page

@pytest.mark.usefixtures("driver")
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


    def test_display_order_price_low_to_high(self, driver):
        inventory_page = self.initialization_function(driver)

        try:
            inventory_page.select_container("Price (low to high)")
            price_elements = driver.find_elements(inventory_page.item_price)
            prices = [float(price.text.replace("$", "")) for price in price_elements]
            assert prices == sorted(prices), "Ordering of the items according to prices(low to high) failed"

        except TimeoutException:
            pytest.fail("Timeout has occurred.")

    def test_display_order_price_high_to_low(self,driver):
        inventory_page = self.initialization_function(driver)
        try:
            inventory_page.select_container("Price (high to low)")
            price_elements = driver.find_elements(inventory_page.item_price)
            prices = [float(price.text.replace("$", "")) for price in price_elements]
            assert prices == sorted(prices,
            reverse=True), "Ordering of the items according to prices(high to low) failed"
        except TimeoutException:
            pytest.fail("Timeout has occurred.")

    def test_display_order_reverse_alphabetical(self, driver):
        inventory_page = self.initialization_function(driver)
        try:
            inventory_page.select_container("Name (Z to A)")
            name_elements = driver.find_elements(inventory_page.item_name)
            names = [name.text for name in name_elements]
            assert names == sorted(names, reverse=True), "Ordering of the items according to Name(Z to A) failed"
        except TimeoutException:
            pytest.fail("Timeout has occurred.")

    def test_display_order_alphabetical(self, driver):
        inventory_page = self.initialization_function(driver)
        try:
            inventory_page.select_container("Name (A to Z)")
            name_elements = driver.find_elements(inventory_page.item_name)
            names = [name.text for name in name_elements]
            assert names == sorted(names), "Ordering of the items according to Name(A to Z) failed"
        except TimeoutException:
            pytest.fail("Timeout has occurred.")



    # def test_add_to_cart_items_count(self,driver):
    #     inventory_page = self.initialization_function(driver)
    #     add_to_cart_buttons =driver.find_elements(inventory_page.add_to_cart_buttons)
    #     expected_count =len(add_to_cart_buttons)
    #     for button in add_to_cart_buttons:
    #         button.click()
    #         time.sleep(1) # Waiting for the number update in cart button
    #     cart_badge = driver.find_element(inventory_page.cart_badge)
    #     cart_badge_text = inventory_page.get_text(cart_badge)
    #     actual_count = int(cart_badge_text)
    #     assert actual_count == expected_count, f"Expected {expected_count} items in cart, but found {actual_count}"
    #
    #
    # def test_remove_from_cart_count


