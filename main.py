import random
from datetime import datetime
import selenium as sel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import requests

options = Options()
#options.add_argument('--headless')


class GoogleHandler:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    def start(self):
        self.driver.maximize_window()
        self.driver.minimize_window()
        self.driver.maximize_window()
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.implicitly_wait(10)

        # Enter to the site
        self.driver.get('https://google.com')
        self.driver.implicitly_wait(8)
        self.acceptCookies()

    def acceptCookies(self):
        # Accept cookies
        self.driver.find_element('xpath', "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]").click()
        print('Opened page...')
        self.search()

    def search(self):
        input = self.driver.find_element('xpath', "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
        if input:
            input.send_keys('Mario Ruci')
            submit = self.driver.find_element('xpath', "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")
            submit.click()
            self.driver.implicitly_wait(5)
            website = self.driver.find_element('xpath', "//*[contains(text(), 'https://marioruci.com')]")
            if website:
                website.click()
                self.driver.implicitly_wait(15)
                self.driver.close()
                

if __name__ == '__main__':
    for i in range(5):
        google = GoogleHandler()
        google.start()
