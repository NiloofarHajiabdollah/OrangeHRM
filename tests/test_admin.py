import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import random
import time
import pandas as pd
from selenium import webdriver
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage
from pages.search_user import SearchUser
from pages.logout import Logout

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.maximize_window()

df = pd.read_excel("user_data.xlsx")
emp_name, username, password = df.iloc[0]['EmployeeName'], df.iloc[0]['Username'], df.iloc[0]['Password']
username = f"{username}{random.randint(1000, 999999)}"


login_page = LoginPage(driver)
login_page.login("Admin", "admin123")


admin_page = AdminPage(driver)
admin_page.navigate_to_admin()
admin_page.click_add()

add_user_page = AddUserPage(driver)
add_user_page.add_user(emp_name, username, password)


search_user = SearchUser(driver)
if search_user.search_user(username):
    print("User added successfully!")
else:
    print("User addition failed!")


logout = Logout(driver)
if logout.perform_logout():
    print("User logout successfully!")
else:
    print("User logout failed!")

driver.quit()
