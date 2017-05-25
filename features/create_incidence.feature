Feature: Create new incidence
  As a user
  I want to create an incidence
  So I can notify my problems

  Scenario: Create new incidence
    Given I am logged in as
    | username | password |
    | usuari   | contra   |
    And I click to create incidence
    And I fill all the camps
    | network  | explanation | city |
    | Facebook | Not working | DCU  |
    And I create the incidence