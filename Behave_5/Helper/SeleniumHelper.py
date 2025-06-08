from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

class Heading:
    def __init__(self,driver):
        self.driver=driver

    def application(self,url):
        self.driver.get(url)

    def verifyTitle(self,titleval):
        assert self.driver.title.__eq__(titleval),"User in wrong application(Title)"

    def verifyurl(self,giveurl):
        assert self.driver.current_url.__eq__(giveurl),"User in wrong application(URL)"

    def verifyText(self,xpath,textinput):
        txtval = self.driver.find_element(By.XPATH,xpath).text
        assert txtval == textinput,"User in wrong application(wrong text)"

    def verifyElements(self,xpath):
        assert self.driver.find_element(By.XPATH,xpath),"Element not found"

    def fileOperation(self,name,xpath):
        with open(f"{name}\\file1.txt","x") as f:
            self.driver.find_element(By.XPATH,xpath).send_keys(f)