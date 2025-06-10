import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Heading:
    def __init__(self,driver):
        self.driver=driver

    def application(self,givenurl):
        self.driver.get(givenurl)

    def verifyTitle(self,titleval):
        assert self.driver.title.__eq__(titleval),"User in wrong application(title)"

    def verifyURL(self,url_val):
        assert self.driver.current_url.__eq__(url_val),"User in wrong aplication(URL)"

    def verifyText(self,xpath,textval):
        txtval = self.driver.find_element(By.XPATH,xpath).text
        assert txtval == textval,"User in wrong application"

    def performOperation(self):
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("f").key_down(Keys.CONTROL).perform()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("h").key_down(Keys.CONTROL).perform()
        self.driver.refresh()
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.ALT).send_keys("f").key_down(Keys.ALT).perform()

