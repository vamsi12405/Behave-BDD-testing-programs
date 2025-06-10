import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helper.SeleniumHelper import Heading
from Logs.logging import logger

loginURL="https://www.geeksforgeeks.org/"

@given("website with proper credentials")
def step_impl(context):
    Heading(context.driver).application(loginURL)
    context.driver.implicitly_wait(20)
    logger.info("Page opened")
    Heading(context.driver).verifyTitle("GeeksforGeeks | Your All-in-One Learning Portal")
    Heading(context.driver).verifyURL("https://www.geeksforgeeks.org/")
    Heading(context.driver).verifyText("//div[@class='HomePageSearchContainer_homePageSearchContainer_heading__DhWmd']","Hello, What Do You Want To Learn?")

@then("we perform ActionChains operation")
def step_impl(context):
    time.sleep(3)
    try:
        Heading(context.driver).performOperation()
    except Exception as e:
        logger.error("Error Occured")
        print(e)