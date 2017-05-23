
Feature: Modify box
  As a user
  I want to modify a box
  So I can change its content

  Scenario: Modify box
    Given I am logged in as
    | username | password |
    | usuari   | contra   |
    And I have a registered box
    And I want to see the information
    And I want to modify it
    And I complete the form
    Then I save edited box