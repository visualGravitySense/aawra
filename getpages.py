from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Getpages:
    def __init__(self, driver):
        self.driver = driver
            # 12 pages/laoded
    def get_num_flw(self):
        print('followers number')
        self.driver.get('https://www.instagram.com/python.learning')
        flw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
        sflw = b(flw.get_attribute('innerHTML'), 'html.parser')
        followers = sflw.findAll('span', {'class':'g47SY'})
        f = followers[1].getText().replace(',', '')
        print(f)
    def get_followers(self):
        print('get followers')
        flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')))
        flw_btn.click()
        popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
