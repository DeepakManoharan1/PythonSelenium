from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I got navigate to home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")


@when(u'Enter valid product id')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']//input[1]").send_keys("HP")


@when(u'click search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[@class='input-group-btn']//button[1]").click()


@then(u'product is displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    context.driver.quit()


@when(u'Enter Invalid product id')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']//input[1]").send_keys("Honda")


@then(u'Proper message is displayed')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria.";
    assert context.driver.find_element(By.XPATH,
                                       "//p[text()='There is no product that matches the search criteria.']").text.__eq__(
        expected_text)
    context.driver.quit()


@when(u'noyhing enter into search field')
def step_impl(context):
    print(8)
