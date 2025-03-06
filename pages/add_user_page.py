from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class AddUserPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_role_dropdown = (By.XPATH, "//label[text()='User Role']/following::div[@class='oxd-select-text-input']")
        self.admin_option = (By.XPATH, "//div[@role='listbox']//span[text()='Admin']")
        self.status_dropdown = (By.XPATH, "//label[text()='Status']/following::div[@class='oxd-select-text-input']")
        self.enabled_option = (By.XPATH, "//div[@role='listbox']//span[text()='Enabled']")
        self.employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.employee_name_dropdown = (By.XPATH, "//div[@role='listbox']//span[text()='Qwerty Qwerty LName']")
        self.username = (By.XPATH, "//label[text()='Username']/following::input[1]")
        self.password = (By.XPATH, "//label[text()='Password']/following::input[1]")
        self.confirm_password = (By.XPATH, "//label[text()='Confirm Password']/following::input[1]")
        self.save_button = (By.XPATH, "//button[text()=' Save ']" )
    
    def add_user(self, emp_name, user_name, pwd):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.user_role_dropdown)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.admin_option)).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.status_dropdown)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.enabled_option)).click()

        self.driver.find_element(*self.employee_name).send_keys(emp_name)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.employee_name_dropdown)).click()
        self.driver.find_element(*self.username).send_keys(user_name)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.confirm_password).send_keys(pwd)
        self.driver.find_element(*self.save_button).click()
        time.sleep(5)
