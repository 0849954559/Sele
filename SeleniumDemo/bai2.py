from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path='venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://www.conferenceseries.com/past-conference-reports.php')

print(driver.title)
articles = driver.find_elements(By.CSS_SELECTOR, 'list-group')

driver.set_page_load_timeout(360)
for article in articles:
    try:
        c1 = article.find_element(By.CLASS_NAME, 'col-md-6')
        c2 = article.find_element(By.CLASS_NAME, 'col-md-3')
        c3 = article.find_element(By.TAG_NAME, 'col-md-3')
        print(c1.text)
        print(c2.text)
        print(c3.text)
        print("==============")
        time.sleep(1)
    except :
        pass

driver.quit()
