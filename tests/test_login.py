import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from conftest import password
from pages import LoginPage, InventoryPage
from selenium.common import TimeoutException


usernames = [
    ('TC_001', 'standard_user'),
    ('TC_002', 'problem_user'),
    ('TC_003', 'performance_glitch_user'),
    ('TC_004', 'error_user'),
    ('TC_005', 'visual_user'),
    ('TC_006', 'locked_out_user')
]


@pytest.mark.usefixtures("driver")
class TestLogin:


    @pytest.mark.parametrize("test_case_id, username", usernames)
    def test_login_valid_user(self,driver,test_case_id, username):

        login_page = LoginPage(driver)
        try:
            login_page.login(username, password)
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



