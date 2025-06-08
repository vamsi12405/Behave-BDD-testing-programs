import time
from xml.etree.ElementPath import xpath_tokenizer_re

from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Heading:
    def __init__(self,driver):
        self.driver = driver

    def giveurl(self,url):
        self.driver.get(url)

    def verifyTitle(self,titleval):
        assert self.driver.title.__eq__(titleval),"User in wrong application(wrong title)"

    def verifyURL(self,urlval):
        assert self.driver.current_url.__eq__(urlval),"User in wrong application(Wrong URL)"

    def verifyText(self,xpath,textvalue):
        txtval=self.driver.find_element(By.XPATH,xpath).text
        assert txtval == textvalue,"User in wrong application"

    def verifyelements(self,xpath):
        assert self.driver.find_element(By.XPATH,xpath),"Element not found"

    def moveToElement(self,xpath):
        element = self.driver.find_element(By.XPATH,xpath)
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()

    def clickinput(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()

    def alert(self,driver):
        content = self.driver.switch_to.alert
        print(content.text)
        content.accept()

    def alert3(self,driver):
        content = self.driver.switch_to.alert
        content.send_keys("I am new to Automation Testing")
        content.accept()
