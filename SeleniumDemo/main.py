from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path='venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://vnexpress.net/')

print(driver.title)
articles = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')

driver.set_page_load_timeout(360)
for article in articles:
    try:
        title = article.find_element(By.TAG_NAME, 'h3')
        des = article.find_element(By.CLASS_NAME, 'description')
        img = article.find_element(By.TAG_NAME, 'img')
        print(title.text)
        print(des.text)
        print(img.get_attribute('src'))
        print("==============")
        time.sleep(1)
    except :
        pass

driver.quit()
