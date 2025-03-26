from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

kw = input("Enter your Keyword: ")

service = Service(executable_path='venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://dhthanhit.pythonanywhere.com/')

k = driver.find_element(By.NAME, 'keyword')
k.send_keys(kw)
btn = driver.find_element(By.CSS_SELECTOR, 'nav button[type=submit]')

btn.click()

driver.set_page_load_timeout(360)
time.sleep(1)
products = driver.find_elements(By.CSS_SELECTOR, '.card-title')

for p in products:
    try:
        print(p.text)
    except:
        pass

details = driver.find_elements(By.CSS_SELECTOR, '.card-body a.btn.btn-primary')
urls = [d.get_attribute('href') for d in details]
print(urls)

for d in urls:
    driver.get(d)
    comments = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, '.list-group-item P'))
    )
    for c in comments:
        print(c.text)

driver.quit()
