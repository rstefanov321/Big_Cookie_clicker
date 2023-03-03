import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Making the window stay open until user interaction
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Enter the path to your Chrome driver
chrome_driver_path = r"directory_path\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

# Enter the link to the website
cookie_url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(cookie_url)

# Deal with some "cookie" settings on popup windows
time.sleep(3)
manage_options = driver.find_element(By.CSS_SELECTOR, ".fc-primary-button p")
manage_options.click()

time.sleep(2)

# Select the language in which you want the game to displayed
confirm_choices = driver.find_element(By.ID, "langSelect-EN")
confirm_choices.click()

time.sleep(2.3)

# find the cookie on the webpage
cookie = driver.find_element(By.ID, "bigCookie")

time.sleep(3)

def start_clicking():
    now = time.time()
    timer = 0
    while timer <= 360:
        cookie.click()
        end = time.time()
        timer = round(end-now)


start_clicking()





