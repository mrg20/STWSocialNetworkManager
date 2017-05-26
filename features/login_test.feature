Feature: Log in
  As a user
  I want to login
  So I can use the services

  Scenario: Log in
    Given This user exists
    | username | password |
    | usuari   | contra   |
    Then I log in
    | username | password |
    | usuari   | contra   |

  Scenario: Fail logging in
    Given I want to log in as
    | username | password |
    | usuari   | contras  |
    And The fields are invalid
    Then I go to register page