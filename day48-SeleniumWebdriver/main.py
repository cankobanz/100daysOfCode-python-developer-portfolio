from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Stonemaier-Games-STM600-Scythe-Board/dp/B01IPUGYK6/ref=sr_1_1?crid=2ID9VJM43KU9A&keywords=schyte&qid=1695886741&sprefix=schyte%2Caps%2C187&sr=8-1&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, 'a-price-whole')
# price_cent = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The Price is {price_dollar.text}.{price_cent.text}.")

# driver.get("https://www.python.org/")
#
# search_bar = driver.find_element(By.NAME, "q")
# button = driver.find_element(By.ID, "submit")
#
# element = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
# print(element.text)

# CHALLANGE 1
# driver.get("https://www.python.org/")
# time_elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# event_elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
# event = {}
#
# for i in range(len(time_elements)):
#     event[i] = {"time" : "2023-" + time_elements[i].text,
#                  "event" : event_elements[i].text
#                 }
#
# print(event)

# CHALLANGE 2

driver.quit()