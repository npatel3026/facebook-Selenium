from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import os

# Get absolute path of geckodriver.exe in the same folder
driver_path = os.path.join(os.getcwd(), "geckodriver.exe")
service = Service(driver_path)

# Create Firefox driver
driver = webdriver.Firefox(service=service)

# Open Facebook
driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(2)

# Check title
expected_title = "Facebook – log in or sign up"
actual_title = driver.title
if expected_title == actual_title:
    print("Title Test Passed ")
else:
    print("Title Test Failed ", actual_title)

# Check email field
try:
    email_field = driver.find_element(By.ID, "email")
    print("Email Field Test Passed ")
except:
    print("Email Field Test Failed ")

# Check password field
try:
    password_field = driver.find_element(By.ID, "pass")
    print("Password Field Test Passed ")
except:
    print("Password Field Test Failed ")

# Check login button
try:
    login_button = driver.find_element(By.NAME, "login")
    print("Login Button Test Passed ")
except:
    print("Login Button Test Failed ")

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
login = driver.find_element(By.NAME, "login")

email.send_keys("test@gmail.com")
password.send_keys("123")  # too short
login.click()
element = driver.find_element(By.CLASS_NAME, "_9ay7")
if "incorrect" in element.text.lower():
    print(" Success -incorrect")
else:
    print(" Failed -incorrect -->"+element.text)

time.sleep(2)

# Close browser
driver.quit()
