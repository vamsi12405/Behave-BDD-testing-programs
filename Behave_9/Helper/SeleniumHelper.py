from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

class Heading:
    def __init__(self,driver):
        self.driver=driver

    def application(self,url):
        self.driver.get(url)

    def verifyTitle(self,titleval):
        assert self.driver.title.__eq__(titleval),"User in wrong application(title)"

    def verifyURL(self,url_val):
        assert self.driver.current_url.__eq__(url_val),"User in wrong aplication(URL)"

    def verifyText(self,xpath,textval):
        txtval = self.driver.find_element(By.XPATH,xpath).text
        assert txtval == textval,"User in wrong application"

    def verifyElement(self,xpath):
        assert self.driver.find_element(By.XPATH,xpath),"Element not found"

    def clickElements(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()

    def switchtoIFrame(self,xpath):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,xpath))

    def inputElement(self,xpath,value):
        self.driver.find_element(By.XPATH,xpath).send_keys(value)