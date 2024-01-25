from behave import *


@given(u'I navigate to register page')
def step_impl(context):
    print(1)


@when(u'I enter mandatory fields')
def step_impl(context):
    print(2)


@when(u'I click on continue button')
def step_impl(context):
    print(3)


@then(u'Account is created')
def step_impl(context):
    print(4)


@when(u'I enter all fields')
def step_impl(context):
    print(5)


@when(u'I enter details into all fields except email fields')
def step_impl(context):
    print(6)


@when(u'I enter existing account email into email fields')
def step_impl(context):
    print(7)


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    print(8)


@when(u'I dont enter anything into the fields')
def step_impl(context):
    print(9)


@then(u'Proper Warning message for every manadatory fields should be displayed')
def step_impl(context):
    print(10)
