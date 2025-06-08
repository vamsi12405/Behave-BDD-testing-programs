from xml.etree.ElementPath import xpath_tokenizer_re

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

class Heading:
    def __init__(self,driver):
        self.driver=driver

    def application(self,url):
        self.driver.get(url)

    def verifytitle(self,title_val):
        assert self.driver.title.__eq__(title_val),"User in wrong application(title)"

    def verifyURL(self,url_val):
        assert self.driver.current_url.__eq__(url_val),"User in wrong application(url)"

    def verifyText(self,xpath,textinput):
        txtval = self.driver.find_element(By.XPATH,xpath).text
        assert txtval == textinput

    def verifyElementTobeScrolled(self,xpath):
       assert self.driver.find_element(By.XPATH,xpath),"Element not present"

    def movetoElement(self,xpath):
        self.driver.find_element(By.XPATH,xpath)