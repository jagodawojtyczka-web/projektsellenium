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
search_box.send_keys('okulary')
search_box.send_keys(Keys.RETURN)
time.sleep(1)

add_to_cart_button1 = driver.find_element(By.CSS_SELECTOR, "#card-list > div:nth-child(1) > div > div > a > div.multi--image--2bIiWPB.multi--imagesGallery--3xCP4Ci.cards--image--1nakz5t > div.multi--shopCart--darm7xs.multi--shopLtr--1kiOXiJ.multi--shopCartImage--2DX88PV")
add_to_cart_button1.click()
time.sleep(3)

add_to_cart_button2 = driver.find_element(By.XPATH, '/html/body/div[10]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[6]/button')
add_to_cart_button2.click()
time.sleep(1)
print("Test zakończony. Dodano do koszyka")

driver.quit()
