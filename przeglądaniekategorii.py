from unittest import skip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as excon
import time

def popup1_deny(element_class):
    timeout = 5
    timeout_message = 'Nie znaleziono w wyznaczonym czasie'
    page_position = (By.CLASS_NAME, element_class)
    found = excon.visibility_of_element_located(page_position)
    waiting_time = WebDriverWait(driver, timeout)
    return waiting_time.until(found, timeout_message)


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.aliexpress.com")
time.sleep(1)
print("Uruchomiono stronę")

button1_accept = driver.find_element(By.XPATH,'//*[@id="gdpr-new-container"]/div/div[2]/button[3]')
button1_accept.click()
time.sleep(1)
print("Zaakceptowano cookies")

try:
    deny_button = popup1_deny('pop-close-btn')
    deny_button.click()
    print("Wyłączono pop up reklamowy")
except TimeoutException:
    print('Nie znaleziono')
    skip

popup1_accept = driver.find_element(By.CLASS_NAME, '_24EHh')
popup1_accept.click()
time.sleep(1)
print("Wyłączono pop up z powiadomieniami")

categories_button = driver.find_element(By.CSS_SELECTOR, '#root > div.home--new-home--UXKZmgj > div:nth-child(1) > div > div > div > div.pc2023-header-tab--all-categories-part--FwIOdmw > div')
categories_button.click()
time.sleep(3)

category_select = driver.find_element(By.CSS_SELECTOR, '#root > div.home--new-home--UXKZmgj > div:nth-child(1) > div > div > div > div.pc2023-header-tab--all-categories-part--FwIOdmw > div > div > div:nth-child(1) > div > ul > a:nth-child(1) > li')
category_select.click()
time.sleep(2)

subcategory_select = driver.find_element(By.CSS_SELECTOR, '#root > div > div > div.lv3Category--lv3Category--1hf3Fqv > div > div:nth-child(1) > a > div > div.lv3Category--lv3CategoryContentImg--2GZvdRG > div')
subcategory_select.click()
time.sleep(2)
print("Testy przeglądania kategorii zakończone")

driver.quit()
