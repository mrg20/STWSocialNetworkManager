Feature: Show a user box
  As a user
  I want to see my boxes
  So I know special information about them

  Scenario: Show box
    Given I am logged in as
    | username | password |
    | usuari   | contra   |
    And I have a registered box
    Then I want to see the information of it
