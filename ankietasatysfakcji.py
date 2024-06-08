from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

button1_survey = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/section[1]/div[1]/ul/li[4]/a')
button1_survey.click()
time.sleep(1)

question1_answer = driver.find_element(By.XPATH,'//*[@id="704892858_8080142156_label"]')
question1_answer.click()
next1_button = driver.find_element(By.CSS_SELECTOR, '#patas > main > article > section > form > div.survey-submit-actions.center-text.clearfix > button')
next1_button.click()
time.sleep(1)
print("Odpowiedziano na 1 pytanie")

question2_select1 = driver.find_element(By.CSS_SELECTOR, '#question-field-704893778 > fieldset > div > div:nth-child(2) > div:nth-child(7) > div > label > span.checkbox-button-display')
question2_select1.click()
question2_select2 = driver.find_element(By.CSS_SELECTOR, '#question-field-704893778 > fieldset > div > div:nth-child(1) > div:nth-child(2) > div > label')
question2_select2.click()
next2_button = driver.find_element(By.CSS_SELECTOR,'#patas > main > article > section > form > div.survey-submit-actions.center-text.clearfix > button.btn.small.next-button.survey-page-button.user-generated.notranslate')
next2_button.click()
time.sleep(1)
print("Odpowiedziano na drugie pytanie")

try:
    question3_box = driver.find_element(By.ID, '663330668')
except:
    question3_box = driver.find_element(By.XPATH, '//*[@id="663330668"]')
question3_box.send_keys("nothing")
question3_box.send_keys(Keys.RETURN)
print("Odpowiedziano na trzecie pytanie")

try:
    question4_select1 = driver.find_element(By.CSS_SELECTOR, '#\36 63329566_7656133568_7656133566_label')
except:
    print("Nie znaleziono interaktywnego pola po SELECTOR, szukam po XPATH")
    question4_select1 = driver.find_element(By.XPATH,'//*[@id="663329566_7656133568_7656133566"]')
question4_select1.click()
print("Opowiedziano na czwarte pytanie")

question5_select1 = driver.find_element(By.XPATH, '//*[@id="663330594_7656143635_7656143630"]')
question5_select1.click()
print("Odpowiedziano na piąte pytanie")

question6_select1 = driver.find_element(By.XPATH, '//*[@id="663330627_9263574255"]')
question6_select1.click()
print("Odpowiedziano na szóste pytanie")
submit_button = driver.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button[2]')
submit_button.click()
time.sleep(1)
print("Zakończono testy. Wysłano odpowiedź")

driver.quit()


