from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page/")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

search = driver.find_element(By.CLASS_NAME, "search")
print(search.size)
# search.send_keys("python")
# search.send_keys(Keys.ENTER)
driver.quit()