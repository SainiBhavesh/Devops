import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
# from helper import *
import time

src=""
dst=""

def save(final_data):
    json_object = json.dumps(final_data, indent=4, ensure_ascii=False)
    with open("final_data.json", "w", encoding='utf8') as outfile:
        outfile.write(json_object)
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.61 Safari/537.36'
def flightScrape(source,destination):
    global src
    src=source
    global dst
    dst=destination
    print(src)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument(f'user-agent={user_agent}')


# Functions created by me for reusability
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


# MAIN CODE

    # print('Enter your source-city')
    # source=input()

    # print('Enter your destination-city')
    # destination=input()


    final_data = []
    driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

    is_break = False

    start_url = f'https://www.makemytrip.com/flights/'

    driver.get(start_url)
    time.sleep(0.25)

# src=check_exists_by_xpath_text(driver, f'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/label/input').send_keys(source)

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/label/input').send_keys(source)
    time.sleep(1.0)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input').send_keys(Keys.ARROW_DOWN)
    time.sleep(1.0)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input').send_keys(Keys.ENTER)
    time.sleep(1.0)

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/label/input').send_keys(destination)
    time.sleep(1.0)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
    time.sleep(1.0)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/input').send_keys(Keys.ENTER)
    time.sleep(1.5)


    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/label/input').send_keys(Keys.ESCAPE)
    time.sleep(2.0)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/label/input').send_keys(Keys.ESCAPE)
    time.sleep(1.0)

    driver.find_element(By.XPATH,'//*[@id="SW"]/div[1]/div[1]/ul/li[4]/div[2]').click()
    time.sleep(4.0)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[2]/p/a').click()
    time.sleep(8.0)

    driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[3]/button').click()
    time.sleep(2.0)

# price1=check_exists_by_classname(driver,'timingOption')
    price1=check_exists_by_xpath_text(driver,'//*[@id="premEcon"]/div')
    # print(price1)
    return price1





        
