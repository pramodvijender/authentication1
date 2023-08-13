#!/Users/pramodvijender/PycharmProjects/authentication/venv/chromedriver-Darwin
import time
from sys import argv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

#driver = webdriver.firefox()
options=Options()
# Set the path to the Chrome driver executable
driver_path = '/Users/pramodvijender/PycharmProjects/authentication/node_modules/geckodriver'

# Create a new instance of the Chrome driver
# make this a headless Browser



# Open the website login page
ff_options = webdriver.FirefoxOptions()
ff_options.add_argument("--headless")
ff_options.add_argument('--no-sandbox')
ff_options.add_argument('--disable-dev-shm-usage')
ff_options.add_argument('--enable-javascript')


with open('/Users/pramodvijender/PycharmProjects/authentication/usernames') as myfile:
    for line in myfile.readlines():

         driver = webdriver.Firefox(options=ff_options)
         driver.get("https://online.macquarie.com.au/personal/#/")
         time.sleep(10)
         wait = WebDriverWait(driver, 1)

# Find the username and password input fields by their HTML attributes
#adding Wait Times until th fields are found
         username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
         password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))

         login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'btn btn-lg btn-primary btn-block ladda-button')]")))

# Enter your username and password

         username_field.send_keys(line)
         print(line + "This is the username being sent")
         password_field.send_keys("Dig!secTest2023")
         response = password_field.send_keys(Keys.RETURN)
         login_button.click()
         print("Button Clicked")
# Send the Input Data by Clicking the form
         try:
              returntext = driver.find_element(By.XPATH, "//*[@id='mq-mfa-validate-description']").text
              print(returntext)
         except:
              returntext = driver.find_element(By.XPATH, "//*[contains(@class, 'auth-heading')]").text
              if returntext == "Something went wrong":
                   print(returntext + " This was picked up by botman")
              else:
                   print(returntext + " This was not picked up by botman")
# Wait for the login process to complete


#else:

driver.quit()
