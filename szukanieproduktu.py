from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)

driver.get("https://pl.aliexpress.com/")
time.sleep(1)
print("Uruchomiono stronę")

button1_accept = driver.find_element(By.XPATH,'//*[@id="gdpr-new-container"]/div/div[2]/button[3]')
button1_accept.click()
time.sleep(1)
print("Zaakceptowano cookies")

popup1_deny = driver.find_element(By.CLASS_NAME, '_24EHh')
popup1_deny.click()
time.sleep(1)
print("Wyłączono pop up z powiadomieniami")

search_box = driver.find_element(By.XPATH, '//*[@id="search-words"]')
search_box.send_keys("lampka nocna")
search_box.send_keys(Keys.RETURN)
time.sleep(1)
print("Test zakończony. Wyszukano produkt")

driver.quit()

