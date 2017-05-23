Feature: Delete box
  As a user
  I want to delete a box
  So I do not see the unused ones

  Scenario: Delete box
    Given I am logged in as
    | username | password |
    | usuari   | contra   |
    And I have a registered box
    And I want to see the information
    And I delete it
    Then I go to the homepage