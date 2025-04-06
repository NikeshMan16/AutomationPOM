import os
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver

def take_screenshot(driver: WebDriver,test_name: str, screenshot_dir = "screenshots"):
    """
    Takes screenshots and saves it to specified directory

    Args:
        driver: The Selenium webdriver instance
        test_name: The name of the test (used in the filename)
        screenshot_dir: The directory to save the screenshots
    """
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(screenshot_dir,filename)

    try:
        driver.save_screenshot(filepath)
        print(f"Screenshot saved to: {filepath}")
    except Exception as e:
        print(f"Failed to save the screenshot: {e}")