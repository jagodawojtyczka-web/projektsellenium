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
time.sleep(1)

driver.get("https://pl.aliexpress.com/")
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

popup_deny = driver.find_element(By.CLASS_NAME, '_24EHh')
popup_deny.click()
time.sleep(1)
print("Wyłączono pop up z powiadomieniami")

help_button = driver.find_element(By.CSS_SELECTOR, 'body > div.footer-wrap > div.help-center-y2023 > div > section.section-left > div.f-link-box.f-link-left > ul > li:nth-child(1) > a')
help_button.click()
time.sleep(3)
print("Włączono stronę pomocy")

helpcategory_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/i')
helpcategory_button.click()

helparticle_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]')
helparticle_button.click()
time.sleep(2)
print("Wybrano artykuł")

opinion_button = driver.find_element(By.XPATH, '//*[@id="c_l6ktyxu8-content"]/div[3]/button[1]/span')
opinion_button.click()
print("Wysłano opinie na temat artykułu")
print("Zakończono testy")

driver.quit()
