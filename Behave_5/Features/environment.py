from behave import *
from selenium import webdriver

def before_all(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()