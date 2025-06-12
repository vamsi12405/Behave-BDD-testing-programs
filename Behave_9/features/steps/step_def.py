import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helper.SeleniumHelper import Heading
from Logs.logging import logger

loginURL="https://demo.automationtesting.in/Frames.html"

@given("The webpage with valid credentialis")
def step_impl(context):
    Heading(context.driver).application(loginURL)
    context.driver.implicitly_wait(20)
    logger.info("Page Opened")
    Heading(context.driver).verifyTitle("Frames")
    Heading(context.driver).verifyURL("https://demo.automationtesting.in/Frames.html")
    Heading(context.driver).verifyText("//h1[contains(text(),'Automation Demo Site')]","Automation Demo Site")
    Heading(context.driver).verifyElement("//a[@href='#Single']")
    Heading(context.driver).verifyElement("//a[@href='#Multiple']")

@then("we enter input into iframe")
def step_impl(context):
    try:
        logger.info("Operation is performed")
        Heading(context.driver).clickElements("//a[@href='#Single']")
        Heading(context.driver).switchtoIFrame("//iframe[@name='SingleFrame']")
        time.sleep(2)
        Heading(context.driver).inputElement("//input[@type='text']","Test_Single")

        context.driver.switch_to.default_content()

        Heading(context.driver).clickElements("//a[@href='#Multiple']")
        Heading(context.driver).switchtoIFrame("//iframe[@src='MultipleFrames.html']")
        Heading(context.driver).switchtoIFrame("//iframe[@name='SingleFrame']")
        time.sleep(2)
        Heading(context.driver).inputElement("//input[@type='text']","Test_Multiple")
    except Exception as e:
        logger.error(f"Error occured,{e}")