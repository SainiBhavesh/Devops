import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from mmt import flightScrape
# from helper import *
import time

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.61 Safari/537.36'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option(
      'excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f'user-agent={user_agent}')


# Functions created by me for reusability

def save(final_data):
        json_object = json.dumps(final_data, indent=4, ensure_ascii=False)
        with open("final_data.json", "w", encoding='utf8') as outfile:
            outfile.write(json_object)

def check_exists_by_xpath_href(driver, xpath: str):
        try:
            value = driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            print(f'XPATH NOT FOUND ---- || {xpath}')
            return "null"
        return value.get_attribute('href')

def check_exists_by_xpath_text(driver, xpath):
        try:
            value = driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            print(f'XPATH NOT FOUND ---- || {xpath}')
            return "null"
        return value.text

def check_exists_by_xpath_src(driver, xpath):
        try:
            value = driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            print(f'XPATH NOT FOUND ---- || {xpath}')
            return "null"
        return value.get_attribute('src')

def check_exists_by_xpath_href(driver, xpath: str):
        try:
            value = driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            print(f'XPATH NOT FOUND ---- || {xpath}')
            return "null"
        return value.get_attribute('href')

def check_exists_by_classname(driver, xpath):
        try:
            value = driver.find_element(By.CLASS_NAME, xpath)
        except NoSuchElementException:
            return "null"
        return value

final_data = []

print('Enter your source-city')
source=input()
print('Enter your destination-city')
destination=input()

driver = webdriver.Chrome(service=Service(
ChromeDriverManager().install()), options=chrome_options)
is_break = False
start_url = f'http://127.0.0.1:5501/index.html'
driver.get(start_url)
time.sleep(1.5)

driver.find_element(By.XPATH,'//*[@id="top"]/header/div/div[1]/a/button').click()
time.sleep(2.0)

driver.find_element(By.XPATH, '//*[@id="lname"]').send_keys("John Doe")
time.sleep(1.5)

driver.find_element(By.XPATH, '//*[@id="lpassword"]').send_keys("12345")
time.sleep(2.5)

driver.back()
time.sleep(3.0)

book=check_exists_by_xpath_href(driver,'//*[@id="home"]/div/div/a[1]')
driver.get(book)
time.sleep(1.0)

driver.find_element(By.XPATH, '//*[@id="source"]').send_keys(source.capitalize)
time.sleep(1.5)

driver.find_element(By.XPATH, '//*[@id="destination"]').send_keys(destination.capitalize)
time.sleep(1.5)

driver.find_element(By.XPATH,'//*[@id="form"]/div/button[1]').click()
time.sleep(2.0)

price=flightScrape(source,destination)

driver.find_element(By.XPATH, '//*[@id="pricebox"]').send_keys(price)
time.sleep(1.5)

print(price)
