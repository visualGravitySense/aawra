from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import getpages

username = 'NAME'
password = 'PASS'
driver = 0
def main():
    global driver
    print('running script..')
    driver = webdriver.Chrome('/Users/dmitrigornakov/Desktop/chromedriver')
    l = login.Login(driver, username, password)
    l.signin()

    gp = getpages.Getpages(driver)
    gp.get_followers()
    time.sleep(60)

if __name__ == '__main__':
    main()
