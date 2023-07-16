#!/Users/pramodvijender/PycharmProjects/authentication/venv/chromedriver-Darwin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://github.com/login")

# Find the username and password input fields by their HTML attributes
username_field = driver.find_element(By.ID, "login_field")
password_field = driver.find_element(By.ID, "password")

# Enter your username and password
username_field.send_keys("pramodvijender@gmail.com")
password_field.send_keys("R@ksat727934")

# Send the Input Data by Clicking the form
driver.find_element(By.NAME, "commit").click()
#loginbuttontext = driver.find_element(By.NAME, "commit").tag_name
#print(loginbuttontext + "   This is what the Click is Seeing")




# Wait for the login process to complete
driver.implicitly_wait(5)  # Wait for a maximum of 10 seconds for elements to appear
print(driver.current_url + "This is the current URL")
print(driver.page_source + "This is what the page is seeing")
# Check if login was successful
if "Welcome" in driver.page_source:
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser
driver.quit()
