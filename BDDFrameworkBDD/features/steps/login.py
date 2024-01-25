from behave import *


@given(u'I navigate to login page')
def step_impl(context):
    print(1)

@when(u'I enter valid email address and valid password into the feilds')
def step_impl(context):
    print(2)

@when(u'I click on login button')
def step_impl(context):
    print(3)

@then(u'I should get logged in')
def step_impl(context):
    print(4)

@when(u'I enter invalid email address and valid password into the feilds')
def step_impl(context):
    print(5)


@then(u'I should get a proper warning message')
def step_impl(context):
    print(6)

@when(u'I enter valid email address and invalid password into the feilds')
def step_impl(context):
    print(7)


@when(u'I enter invalid email address and invalid password into the feilds')
def step_impl(context):
    print(8)


@when(u'I dont anything into email and password fields')
def step_impl(context):
    print(9)
