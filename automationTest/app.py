from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# this is the test change
# this is the test change2


# Set up the WebDriver
driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
driver.maximize_window()

try:
    # Open the target website
    driver.get("https://example.com/login")  # Replace with the URL of the site to test

    # Locate username and password fields
    username_field = driver.find_element(By.ID, "username")  # Replace with the actual ID or locator
    password_field = driver.find_element(By.ID, "password")  # Replace with the actual ID or locator

    # Enter credentials
    username_field.send_keys("testuser")  # Replace with a test username
    password_field.send_keys("password123")  # Replace with a test password

    # Submit the login form
    password_field.send_keys(Keys.RETURN)  # Simulates pressing the Enter key
    time.sleep(3)  # Wait for the page to load

    # Check for successful login by locating a logout button or success message
    try:
        logout_button = driver.find_element(By.ID, "logout")  # Replace with the actual locator for logout button
        print("Login test passed!")
    except:
        print("Login test failed. Logout button not found.")

finally:
    # Clean up
    driver.quit()
