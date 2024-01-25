Feature: search functionality
  @completed
  Scenario: search for valid product
    Given I got navigate to home page
    When Enter valid product id
    And click search button
    Then product is displayed

  @completed
  Scenario: search for invalid product
    Given I got navigate to home page
    When Enter Invalid product id
    And click search button
    Then Proper message is displayed

  Scenario:search without entering product
    Given I got navigate to home page
    When noyhing enter into search field
    And click search button
    Then Proper message is displayed
