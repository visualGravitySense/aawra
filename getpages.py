from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Getpages:
    def __init__(self, driver):
        self.driver = driver

    def get_followers(self):
        print('get followers')
        self.driver.get('https://www.instagram.com/python.learning')
        flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')))
        flw_btn.click()
        popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
