from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchUser:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input")
        self.search_button = (By.XPATH, "//button[text()=' Search ']")
        self.result_table = (By.XPATH, "//div[@class='oxd-table-card']")
        self.first_row_username = (By.XPATH, "//div[@class='oxd-table-card']//div[@class='oxd-table-cell oxd-padding-cell'][2]")

    def search_user(self, username):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_box)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button)).click()
        time.sleep(3)

        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.result_table))
        
        found_username = WebDriverWait(self.driver, 100).until(
            EC.visibility_of_element_located(self.first_row_username)
        ).text
              
        print(f"User {username} added successfully!")

        return found_username.strip().lower() == username.strip().lower()