from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.add_button = (By.XPATH, "//button[text()=' Add ']" )
    
    def navigate_to_admin(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.admin_menu)).click()
    
    def click_add(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_button)).click()
