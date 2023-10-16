from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3712412634&f_AL=true&keywords=software%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

EMAIL = "cankoban.ck@gmail.com"
PASSWORD = "05121996ca"

# Get cookie to click on.
import random
random_sleep = [2, 3, 4]
time.sleep(random.choice(random_sleep))

sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Oturum aç")
sign_in_button.click()
time.sleep(random.choice(random_sleep))


username = driver.find_element(By.ID, value="username")
password = driver.find_element(By.ID, value="password")
username.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(random.choice(random_sleep))

easy_apply = driver.find_element(By.CLASS_NAME, value="jobs-apply-button--top-card").find_element(By.CSS_SELECTOR, value="button")
easy_apply.click()
time.sleep(random.choice(random_sleep))

next_button = driver.find_element(By.CLASS_NAME, value="display-flex.justify-flex-end.ph5.pv4").find_element(By.CSS_SELECTOR, value="button")
next_button.click()