from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helper.SeleniumHelper import Heading
from Logs.logging import logger

loginUrl="https://demo.automationtesting.in/FileUpload.html"


loginUrl="https://demo.automationtesting.in/FileUpload.html"

@given("File element")
def step_impl(context):
    Heading(context.driver).application(loginUrl)
    logger.info("Page Opened")
    Heading(context.driver).verifyTitle("File input - Multi select")
    Heading(context.driver).verifyurl("https://demo.automationtesting.in/FileUpload.html")
    Heading(context.driver).verifyText("//h1[text()='Automation Demo Site ']","Automation Demo Site")
    Heading(context.driver).verifyElements("//input[@type='file']")

@then("we perform upload")
def step_impl(context):
    try:
        logger.info("File Operation started")
        filepath = r"C:\Users\vamsi\Desktop\Behave\Behave_5\file1.txt"
        Heading(context.driver).fileOperation(filepath, "//input[@type='file']")
    except Exception as e:
        logger.error("error is %s", e)
    finally:
        context.driver.close()

