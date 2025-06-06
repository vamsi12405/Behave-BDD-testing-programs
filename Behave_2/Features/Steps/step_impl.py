import time

from selenium.webdriver.common.by import By
from behave import when, then
from Seleniumhelper.Helper import Heading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logs.logging import logger

mainURL = "https://demo.automationtesting.in/Register.html"
anotherURL = "https://demo.automationtesting.in/Static.html"

@when("a website is given with valid web element location")
def step_impl(context):
    logger.info("First url page opened")
    Heading(context.driver).getURL(mainURL)
    Heading(context.driver).verifyTitle("Register")
    Heading(context.driver).verifyURL(mainURL)
    Heading(context.driver).verifyText("//h1[contains(text(),'Automation Demo Site')]", "Automation Demo Site")

@when("if we can navigate to another URL and verify")
def step_impl(context):
    logger.info("Second page url opened")
    Heading(context.driver).getURL(anotherURL)
    Heading(context.driver).verifyTitle("Drag and Drop")
    Heading(context.driver).verifyURL(anotherURL)
    Heading(context.driver).verifyText("//h1[contains(text(),'Automation Demo Site')]", "Automation Demo Site")
    for i in range(1, 4):
        xpath = f"(//div[@id='dragarea']//img)[{i}]"
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        assert Heading(context.driver).verifyElements(xpath), "Elements to be dragged not found"
    assert Heading(context.driver).verifyElements("//div[@id='droparea']"), "Drop area not found"

@then("we can perfrom drag drop operation")
def step_impl(context):
    logger.info("Operation started")
    count = 0
    try:
        # Use correct xpath for img elements
        for i in range(1, 4):
            Heading(context.driver).dragElements(f"(//div[@id='dragarea']//img)[{i}]", "//div[@id='droparea']")
            time.sleep(2)
        # After drag-and-drop, check if images are in drop area
        for i in range(1, 4):
            dropped_xpath = f"(//div[@id='droparea']//img)[{i}]"
            WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, dropped_xpath))
            )
            count += 1
        if count == 3:
            logger.info("drag drop successful")
        else:
            logger.error("Drag drop unsuccessful")
            print("not completed")
    finally:
        context.driver.close()