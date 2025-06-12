from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helper.SeleniumHelper import Heading
import logging

loginURL="https://demo.guru99.com/test/web-table-element.php"
elements=["Company","Group","Prev Close (Rs)","Current Price (Rs)","% Change"]
logger = logging.getLogger('behaveLogger')

@given("Webpage with proper credentials")
def step_impl(context):
    heading = Heading(context.driver)
    heading.application(loginURL)
    logger.info("Page opened")
    heading.verifyURL("https://demo.guru99.com/test/web-table-element.php")
    heading.verifyTitle("Web Table Elements")
    heading.verifyText("(//a[@href='https://demo.guru99.com/'])[2]","Demo Site")

    context.driver.implicitly_wait(10)
    heading.verifyElement("//table[@class='dataTable']")

@then("We fetch data from tables")
def step_impl(context):
    heading = Heading(context.driver)
    try:
        count = 0
        element_val = heading.fetchData("//table[@class='dataTable']//thead//tr")
        for destiny_element in element_val:
            if destiny_element.text == elements[count]:
                logger.info(f"{elements[count]} is present")
            else:
                logger.error(f"{elements[count]} is not present")
            count += 1
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")


