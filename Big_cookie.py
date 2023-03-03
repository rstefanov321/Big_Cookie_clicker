
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = r"C:\Users\rstef\Desktop\Development_chrome_driver\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

cookie_url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(cookie_url)

time.sleep(3)
manage_options = driver.find_element(By.CSS_SELECTOR, ".fc-primary-button p")
manage_options.click()

# fc_slider = driver.find_elements(By.CSS_SELECTOR, ".fc-slider-el")

# for i in fc_slider[1::2]:
#     i.click()
#     time.sleep(0.5)

time.sleep(2)
confirm_choices = driver.find_element(By.ID, "langSelect-EN")
confirm_choices.click()

time.sleep(2.3)

cookie = driver.find_element(By.ID, "bigCookie")

# product_unlocked = driver.find_elements(By.CLASS_NAME, "product unlocked enabled")

time.sleep(7)


def start_clicking():
    now = time.time()
    timer = 0
    while timer <= 360:
        cookie.click()
        end = time.time()
        timer = round(end-now)


start_clicking()





