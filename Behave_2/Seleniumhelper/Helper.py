from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.common.action_chains import ActionChains

class Heading:
    def __init__(self,driver):
        self.driver=driver
    def getURL(self,url):
        self.driver.get(url)
    def verifyTitle(self,givenTitle):
        assert self.driver.title.__eq__(givenTitle),"User in wrong application(title)"
    def verifyURL(self,givenURL):
        assert self.driver.current_url.__eq__(givenURL),"User in wrong application(URL)"
    def verifyText(self,xpath,txtvalue):
        textval=self.driver.find_element(By.XPATH,xpath).text
        assert textval==txtvalue,"User in wrong appliaciton(wrong text)"
    def verifyElements(self,xpath):
        assert self.driver.find_element(By.XPATH,xpath),"element not found"
    def dragElements(self,xpath1,xpath2):
       src= self.driver.find_element(By.XPATH,xpath1)
       trg = self.driver.find_element(By.XPATH,xpath2)
       ActionChains(self.driver).drag_and_drop(src,trg).perform()
    def lastverify(self,xpath1,xpath2):
         elem1 = self.driver.find_element(By.XPATH,xpath1)
         elem2 = self.driver.find_element*(By.XPATH,xpath2)
         assert elem1 == elem2,"elements don't match"