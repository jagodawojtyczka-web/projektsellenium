from unittest import skip
from selenium import webdriver
from selenium.webdriver import Keys
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

#instrukcja try...except dodana ze względu na pop up, który pokazuje się tymczasowo na stronie
try:
    deny_button = popup1_deny('pop-close-btn')
    deny_button.click()
    print("Wyłączono pop up reklamowy")
except TimeoutException:
    print('Nie znaleziono')
    skip

popup1_deny = driver.find_element(By.CLASS_NAME, '_24EHh')
popup1_deny.click()
time.sleep(1)
print("Wyłączono pop up z powiadomieniami")

account_button = driver.find_element(By.CSS_SELECTOR, '#_full_container_header_23_ > div.pc-header--right--2cV7LB8 > div > div.pc-header--items--tL_sfQ4 > div.my-account--menuItem--1GDZChA')
account_button.click()
time.sleep(3)

login_button = driver.find_element(By.CLASS_NAME, 'my-account--signin--RiPQVPB')
login_button.click()
time.sleep(3)

try:
    insert_login = driver.find_element(By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div/div[1]/div[3]/div[2]/div/span/span[1]/span[1]/input')  # zła nazwa
except:
    print('Nie znaleziono interaktywnego pola po XPATH, szukam po CLASS_NAME')
    insert_login = driver.find_element(By.CLASS_NAME, 'cosmos-input')
insert_login.clear()
insert_login.send_keys("pythondeveloptest20@gmail.com")
insert_login.send_keys(Keys.ENTER)
time.sleep(3)

try:
    insert_password = driver.find_element(By.NAME, 'new-password')
except:
    print("Nie znaleziono interaktywnego pola po NAME, szukam po XPATH")
    insert_password = driver.find_element(By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div/div[2]/div[2]/div/span/span[1]/input')
insert_password.clear()
insert_password.send_keys("Testy.python3!")
insert_password.send_keys(Keys.RETURN)
print("Testy zakończone")

driver.quit()



