from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helper.SeleniumHelper import Heading
from Logs.logging import logger
from Values.value import title

loginUrl="https://www.amazon.in/"

@given("The Website with right credentials")
def step_impl(context):
    Heading(context.driver).application(loginUrl)
    Heading(context.driver).verifyTitle("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    Heading(context.driver).verifyURL("https://www.amazon.in/")
    Heading(context.driver).verifyText("//span[@class='nav-logo-locale']",".in")
    Heading(context.driver).verifyElements("//input[@placeholder='Search Amazon.in']")

@when("we click on desired items")
def step_impl(context):
    try:
        Heading(context.driver).sendInputandClick("//input[@placeholder='Search Amazon.in']","//input[@type='submit']")
    except Exception as e:
        print("error is",e)
    Heading(context.driver).printWindowHandles()

@then("we must execute window handles functionality")
def step_impl(context):
    try:
        Heading(context.driver).performWindowOperation(title[0],title[1],"//input[@id='add-to-cart-button']")
    except Exception as e:
        print("Error occured",e)