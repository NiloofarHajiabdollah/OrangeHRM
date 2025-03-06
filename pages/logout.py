from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.profile_menu = (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def perform_logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.profile_menu)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_button)).click()
        time.sleep(2)

        current_url = self.driver.current_url

        if "login" in current_url:
            return True
        else:
            print("Expected 'login' in URL but got {current_url}") 
            return False