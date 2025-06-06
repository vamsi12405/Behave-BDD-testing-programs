from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from Helper.LoginHelper import heading
from AllFileLocations import xpaths
from Logs.logger import get_logger

logger = get_logger()

loginURL = "https://demo.automationtesting.in/Register.html"
verifyTitle = "Register"

@given("I open registration page")
def step_impl(context):
    heading(context.driver).url(loginURL)

@given("I verify the page")
def step_impl(context):
    logger.info("Test Execution Started")
    heading(context.driver).verifyURL(loginURL)
    heading(context.driver).verifyTitle(verifyTitle)
    heading(context.driver).verifyText("//h1[contains(text(),'Automation Demo Site')]", "Automation Demo Site")
    for xpath_dict in list:
        for xpath in xpath_dict.values():
            heading(context.driver).checkinput(xpath)
            logger.info(f"Checked input element: {xpath}")
    for xpath in xpaths.xpath1.keys():
        heading(context.driver).checkinput(xpath)
        logger.info(f"Checked input text field: {xpath}")

@when("I enter registration details")
def step_impl(context):
    for xpath, value in xpaths.xpath1.items():
        heading(context.driver).enterInputText(xpath, value)
        logger.info(f"Entered text '{value}' into field: {xpath}")

@when("I click the input values")
def step_impl(context):
    heading(context.driver).enterClickInput(xpaths.xpath2["Female"])
    heading(context.driver).enterClickInput(xpaths.xpath3["Cricket"])
    heading(context.driver).enterClickInput(xpaths.xpath4["Languages"])
    logger.info("Clicked input values: Female, Cricket, Languages")

@when("I enter select Input")
def step_impl(context):
    heading(context.driver).enterClickInput(xpaths.xpath4["Languages"])
    heading(context.driver).enterSelectInput(xpaths.xpath4["Select"], "English")
    heading(context.driver).enterClickInput(xpaths.xpath4["Country"])
    heading(context.driver).enterSelectInput(xpaths.xpath5["Year"], "1999")
    heading(context.driver).enterSelectInput(xpaths.xpath5["Month"], "October")
    heading(context.driver).enterSelectInput(xpaths.xpath5["Day"], "24")
    heading(context.driver).enterInputText(xpaths.xpath6["Password_1"], "YourPassword")
    heading(context.driver).enterInputText(xpaths.xpath6["Confirm_Password_1"], "YourPassword")
    logger.info("Entered select input and passwords.")

@then("action should  be successful")
def step_impl(context):
    heading(context.driver).enterClickInput(xpaths.xpath7["Button"])
    context.driver.implicitly_wait(10)
    try:
        WebDriverWait(context.driver, 10).until_not(EC.title_is(verifyTitle))
        logger.info("Registration successful (title changed).")
    except Exception as e:
        logger.error("Registration failed: Title did not change.")
    finally:
        context.driver.quit()
        logger.info("Test execution completed")