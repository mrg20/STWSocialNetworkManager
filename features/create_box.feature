Feature: Create new box
  As a user
  I want to create a box
  So I can use it


  Scenario: Create box
    Given I am logged in as
    | username | password |
    | usuari   | contra   |
    And I click to create button
    And I complete the form
    Then I create the box