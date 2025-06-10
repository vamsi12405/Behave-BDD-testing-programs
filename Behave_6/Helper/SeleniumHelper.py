from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def verifyElements(self,xpath):
        assert self.driver.find_element(By.XPATH,xpath),"Element not found"

    def clickOperation(self,xpath):
        src=self.driver.find_element(By.XPATH,xpath)
        ActionChains(self.driver).click(src).perform()

    def contextclickOperation(self,xpath):
        src=self.driver.find_element(By.XPATH,xpath)
        ActionChains(self.driver).context_click(src).perform()

    def doubleclickOperation(self,xpath):
        src=self.driver.find_element(By.XPATH,xpath)
        ActionChains(self.driver).double_click(src).perform()