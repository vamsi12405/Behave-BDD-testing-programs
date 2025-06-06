from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

class heading:
    def __init__(self,driver):
        self.driver=driver;

    def url(self,url):
        self.driver.get(url)

    def verifyURL(self,urlpassed):
        assert self.driver.current_url.__eq__(urlpassed),"Invalid URL"

    def verifyTitle(self,giventitle):
        assert self.driver.title.__eq__(giventitle),"Invalid title"

    def verifyText(self,xpath,txtvalue):
        text_val=self.driver.find_element(By.XPATH,xpath)
        assert text_val.__eq__(txtvalue),"Wrong Application"

    def checkinput(self,xpath):
        assert self.driver.find_element(By.XPATH,xpath),"element not found"

    def enterInputText(self,xpath,value):
        self.driver.find_element(By.XPATH,xpath).send_keys(value)

    def enterSelectInput(self,xpath,index):
        Select(self.driver.find_element(By.XPATH,xpath)).select_by_visible_text(index)

    def enterClickInput(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()
