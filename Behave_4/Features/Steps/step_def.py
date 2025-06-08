from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Helper.SeleniumHelper import Heading
from Logs.logging import logger
from parse import parse

loginUrl="https://demo.automationtesting.in/Register.html"

use_step_matcher("parse")

@given("webpage with proper credentials")
def step_impl(context):
    Heading(context.driver).giveurl(loginUrl)
    logger.info("Page Opened")
    Heading(context.driver).verifyTitle("Register")
    Heading(context.driver).verifyURL("https://demo.automationtesting.in/Register.html")
    Heading(context.driver).verifyText("//h1[contains(text(),'Automation Demo Site')]","Automation Demo Site")
    logger.info("Page succesfully verified")

@then("'{numbered}' type of alert is verified amd addressed")
def step_impl(context,numbered):
    logger.info(f"{numbered} operation is being performed")
    Heading(context.driver).verifyelements("(//a[@href='SwitchTo.html'])[1]")
    Heading(context.driver).moveToElement("(//a[@href='SwitchTo.html'])[1]")
    Heading(context.driver).clickinput("//ul//li//a[@href='Alerts.html']")

    Heading(context.driver).verifyelements("//button[@class='btn btn-danger']")
    Heading(context.driver).clickinput("//button[@class='btn btn-danger']")

    Heading(context.driver).alert(context.driver)
    logger.info(f"{numbered} alert is succesful")

@then("'{numbered}' type of alert is verified and addressed")
def step_impl(context,numbered):
    logger.info(f"{numbered} operation is being performed")
    Heading(context.driver).verifyelements("//a[@href='#CancelTab']")
    Heading(context.driver).clickinput("//a[@href='#CancelTab']")
    Heading(context.driver).clickinput("//button[@class='btn btn-primary']")
    Heading(context.driver).alert(context.driver)
    logger.info(f"{numbered} alert is succesful")

@then("'{numbered}' type of alert is veritifed an addressed")
def step_impl(context,numbered):
    logger.info(f"{numbered} operation is being performed")
    Heading(context.driver).verifyelements("//a[@href='#Textbox']")
    Heading(context.driver).clickinput("//a[@href='#Textbox']")
    Heading(context.driver).clickinput("//button[@class='btn btn-info']")
    Heading(context.driver).alert3(context.driver)
    logger.info(f"{numbered} alert is succesful")

