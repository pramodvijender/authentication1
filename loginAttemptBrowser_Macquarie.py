#!/Users/pramodvijender/PycharmProjects/authentication/venv/chromedriver-Darwin
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#this is is using a browser

driver = webdriver.Chrome()

# Open the website login page
driver.get("https://online.macquarie.com.au/personal/#/")

# Find the username and password input fields by their HTML attributes
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Enter your username and password
username_field.send_keys("68217646")
time.sleep(10)
password_field.send_keys("Dig!secTest2023")
driver.implicitly_wait(10)
# Submit the login form
time.sleep(10)
response = password_field.send_keys(Keys.RETURN)

try:
    returntext = driver.find_element(By.XPATH, "//*[contains(@class, 'ng-star-inserterd')]").text
# Wait for the login process to complete
    print(returntext)
except:
    returntext = driver.find_element(By.XPATH, "//*[contains(@class, 'auth-heading')]").text
    if returntext == "Something went wrong":
        print("This was picked up by botman")
    else:
        print(returntext)
#viewport_content = driver.execute_script('return document.querySelector("meta[name=viewport]").getAttribute("content")')
#viewport_content = driver.execute_script('return document.querySelector("meta[name=viewport]").getAttribute(
#print(viewport_content)

# Close the browser
driver.quit()
