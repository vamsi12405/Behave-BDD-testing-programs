from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

def before_all(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()