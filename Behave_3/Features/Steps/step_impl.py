import time

from behave import  *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helper.SeleniumHelper import Heading
from selenium.webdriver.common.action_chains import ActionChains
from Logs.logging import logger

loginUrl="https://demo.automationtesting.in/Register.html"

@given("a website with valid credentials")
def step_impl(context):
    Heading(context.driver).application(loginUrl)
    Heading(context.driver).verifytitle("Register")
    Heading(context.driver).verifyURL("https://demo.automationtesting.in/Register.html")
    Heading(context.driver).verifyText("//h1[text()='Automation Demo Site ']","Automation Demo Site")


@then("scrollby operation is performed")
def step_impl(context):
    logger.info("scrollby Operation started")
    time.sleep(2)
    try:
        ActionChains(context.driver).scroll_by_amount(0,2000).perform()
    except Exception as e:
        print("Exception is",e)
        logger.error("Error occured")

@then("moveby operation is performed")
def step_impl(context):
    logger.info("moveby operation started")
    time.sleep(2)
    try:
        ActionChains(context.driver).move_by_offset(0,2000).perform()
    except Exception as e:
        print("Exception is ",e)
        logger.error("Error occured")

@then("moveto element is performed")
def step_impl(context):
    logger.info("moveto element started")
    try:
        element = Heading(context.driver).movetoElement("//a[@href='https://www.youtube.com/channel/UCmQRa3pWM9zsB474URz8ESg']")
        ActionChains(context.driver).move_to_element(element).perform()
    except Exception as e:
        print("Exception is",e)
        logger.error("Error occured")
    finally:
        context.driver.close()

