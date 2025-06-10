from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from parse import parse
from Helper.SeleniumHelper import Heading
from Logs.logging import logger

use_step_matcher("parse")
loginUrl="https://demo.automationtesting.in/Register.html"

@given("the web credentials")
def step_impl(context):
    Heading(context.driver).application(loginUrl)
    logger.info("Page Loaded")
    Heading(context.driver).verifyTitle("Register")
    Heading(context.driver).verifyURL("https://demo.automationtesting.in/Register.html")
    Heading(context.driver).verifyText("//h1[contains(text(),'Automation Demo Site')]","Automation Demo Site")
    Heading(context.driver).verifyElements("(//input[@type='radio'])[1]")
    Heading(context.driver).verifyElements("//select[@ng-model='country']")
    Heading(context.driver).verifyElements("//textarea[@ng-model='Adress']")

@then("'{action}' operation is performed")
def step_impl(context, action):
    logger.info(f"{action} Operation Begins")
    try:
        heading = Heading(context.driver)
        if action.lower() == "click":
            heading.clickOperation("(//input[@type='radio'])[1]")
        elif action.lower() == "double click":
            heading.doubleclickOperation("//select[@ng-model='country']")
        elif action.lower() == "context click":
            heading.contextclickOperation("//textarea[@ng-model='Adress']")
        else:
            logger.error(f"Unknown action: {action}")
    except Exception as e:
        logger.error(f"{action} could not be performed: {str(e)}")
        raise ValueError(f"Unknown action: {action}")
        raise
