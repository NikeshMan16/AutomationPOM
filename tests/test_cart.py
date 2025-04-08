import pytest
from pages import LoginPage,InventoryPage,CartPage
from variables_urls import valid_password,valid_username,url_cart_page,url_inventory_page,url_checkout_page_one,url_checkout_complete,url_checkout_page_two

@pytest.mark.usefixtures("driver")
class TestCart:

    @staticmethod
    def initialization_function(driver):
        login_page = LoginPage(driver)
        login_page.login(valid_username,valid_password)
        inventory_page = InventoryPage(driver)
        return inventory_page

    def test_order_item_flow(self, driver):
        inventory_page = self.initialization_function(driver)
        cart_page = CartPage(driver)
        cart_page.add_item_to_cart() # An item is added
        inventory_page.click_cart_button() # Navigation to cart page
        assert "cart.html" in driver.current_url, "Failed to navigate to the cart page."

        cart_page.proceed_to_checkout()
        assert "checkout-step-one.html" in driver.current_url, "Failed to navigate to checkout"

        cart_page.confirm_order_details(fname="Harvey",lname="Elliot",zip="24")
        assert  "checkout-step-two.html" in driver.current_url, "Failed to confirm details of the user and navigate to Checkout Overview"

        cart_page.proceed_to_finish()
        assert "checkout-complete.html" in driver.current_url, "Failed to navigate to Checkout Complete"

        final_message = cart_page.get_order_complete_message()
        assert final_message == "Thank you for your order!", f"Failed to display the confirmation message, shown {final_message}"





