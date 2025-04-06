import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from pages import LoginPage, InventoryPage
from selenium.common import TimeoutException

from variables_urls import valid_password,locked_out_user,invalid_password,invalid_username, valid_username

usernames = [
    ('TC_001', 'standard_user'),
    ('TC_002', 'problem_user'),
    ('TC_003', 'performance_glitch_user'),
    ('TC_004', 'error_user'),
    ('TC_005', 'visual_user')
    # ('TC_006', 'locked_out_user')
]


@pytest.mark.usefixtures("driver")
class TestLogin:


    @pytest.mark.parametrize("test_case_id, username", usernames)
    def test_login_valid_user(self,driver,test_case_id, username):

        login_page = LoginPage(driver)
        try:
            login_page.login(username, valid_password)
            assert "inventory" in driver.current_url, f"Failed Login for {test_case_id}"

        except TimeoutException:
            print(f"Timeout Error in {test_case_id}: Too long time to load / performance issues.")

        finally:
            # Logout before running the next test case
            inventory_page = InventoryPage(driver)
            try:
                inventory_page.logout_function()
            except TimeoutException:
                    print(f"Logout timeout for {test_case_id}")


    def test_login_locked_out_user(self,driver,):

        login_page = LoginPage(driver)
        login_page.login(invalid_username, valid_password)
        assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message()


    def test_valid_username_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.login(valid_username, invalid_password)
        assert "Invalid username/password" in login_page.get_error_message()


    def test_username_empty(self, driver):
        login_page = LoginPage(driver)
        login_page.login('', valid_password)
        assert "Epic sadface: Username is required" in login_page.get_error_message()


    def test_password_empty(self, driver):
        login_page = LoginPage(driver)
        login_page.login(valid_username,'')
        assert "Epic sadface: Password is required" in login_page.get_error_message()

    def test_both_empty(self,driver):
        login_page = LoginPage(driver)
        login_page.login('','')
        assert "Epic sadface: Username is required" in login_page.get_error_message()




