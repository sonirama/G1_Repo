import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchbrowser(context):
 context.driver = webdriver.Chrome()



@when('open the orange HRM page')
def openloginpage(context):
 context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
 time.sleep(4)


@then('verify that logon is present on the page')
def verifylogo(context):
    status = context.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").is_displayed()
    assert status is True


@then('close browser')
def  closebrowser(context):
    context.driver.close()


@when('Enter username "{user}" and password "{passd}"')
def enterusernamepasswd(context, user, passd):
    context.driver.find_element(By.XPATH, "//input[@name = 'username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys(passd)



@when('click on login button')
def clicklogin(context):
    context.driver.find_element(By.XPATH,"//button[@type= 'submit']").click()



@then('User must successfully login to Dashboard')
def homepagedisplay(context):
    try:
      text = context.driver.find_element(By.XPATH, "//header/div[1]/div[1]")
    except:
        context.driver.close()
        assert False,"Test failed"

    if text=="Dashboard":
        context.driver.close()
        assert True, "Test passed"






