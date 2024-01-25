Feature: Login Functionality
  Scenario: Login with valid credentials
    Given I navigate to login page
    When I enter valid email address and valid password into the feilds
    And I click on login button
    Then I should get logged in

  Scenario: Login with invalid email and valid password
    Given  I navigate to login page
    When I enter invalid email address and valid password into the feilds
    And I click on login button
    Then I should get a proper warning message

  Scenario: Login with valid email and invalid password
    Given  I navigate to login page
    When I enter valid email address and invalid password into the feilds
    And I click on login button
    Then I should get a proper warning message

  Scenario: Login with invalid credentials
    Given I navigate to login page
    When I enter invalid email address and invalid password into the feilds
    And I click on login button
    Then I should get a proper warning message

  Scenario:  login without entering any credentials
    Given I navigate to login page
    When I dont anything into email and password fields
    And I click on login button
    Then I should get a proper warning message
