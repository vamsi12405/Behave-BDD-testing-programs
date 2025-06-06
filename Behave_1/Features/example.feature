Feature: Registration on Automation Demo Website
  Scenario: Registration with valid input data
    Given I open registration page
    And I verify the page
    When I enter registration details
    And I click the input values
    And I enter select Input
    Then action should  be successful
