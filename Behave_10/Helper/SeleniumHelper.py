import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Values.value import value1
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Heading:
    def __init__(self,driver):
        self.driver=driver;

    def application(self,url):
        self.driver.get(url)

    def verifyTitle(self,titleval):
        assert self.driver.title.__eq__(titleval),"User in wrong application(title)"

    def verifyURL(self,url_val):
        assert self.driver.current_url.__eq__(url_val),"User in wrong application(url)"

    def verifyText(self,xpath,textvalue):
        txtval = self.driver.find_element(By.XPATH,xpath).text
        assert txtval == textvalue,"User in wrong application"

    def verifyElements(self,xpath):
        self.driver.find_element(By.XPATH,xpath),"Element not found"

    def sendInputandClick(self,xpath1,xpath2):
       for i,j in value1.items():
           self.driver.find_element(By.XPATH,xpath1).send_keys(i)
           time.sleep(1)
           self.driver.find_element(By.XPATH,xpath2).click()
           time.sleep(1)
           element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.XPATH,j))
           time.sleep(2)
           element.click()
           time.sleep(2)

    def printWindowHandles(self):
        print(self.driver.window_handles)

    def performWindowOperation(self,titleofwindow,windowurl,addtocart1):
        for i in self.driver.window_handles:
            self.driver.switch_to.window(i)
            assert self.driver.title.__eq__(titleofwindow)
            self.driver.find_element(By.XPATH,addtocart1).click()
            assert self.driver.current_url(windowurl)
            self.driver.find_element(By.XPATH,addtocart1).click()
            self.driver.close()
        self.driver.close()

