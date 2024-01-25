Feature: Regidter account functionality

  Scenario: Register with mandatory fields
    Given I navigate to register page
    When I enter mandatory fields
    And I click on continue button
    Then  Account is created

  Scenario: Register with all fields

    Given I navigate to register page
    When I enter all fields
    And I click on continue button
    Then Account is created

  Scenario: Register with a duplicates email address
    Given I navigate to register page
    When I enter details into all fields except email fields
    And I enter existing account email into email fields
    And I click on continue button
    Then Proper warning message informing about duplicate account should be displayed

  Scenario: Register without any details
    Given I navigate to register page
    When I dont enter anything into the fields
    And I click on continue button
    Then Proper Warning message for every manadatory fields should be displayed


