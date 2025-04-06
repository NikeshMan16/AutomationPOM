from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def select_dd(self, locator: tuple[str, str], option: str) -> None:
        element = self.wait.until(EC.presence_of_element_located(locator))  # Ensure element is present
        dropdown = Select(element)  # Wrap WebElement in Select
        dropdown.select_by_visible_text(option)

    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except:
            return False

    def navigate_to(self, url):
        self.driver.get(url)



