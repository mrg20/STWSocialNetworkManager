Feature: Register user
  As a person
  I want to sign up
  So I can buy some products

  Scenario: Register user
    Given I go to the login page
    And I click into register
    And I register as "username" and "passwordo"
    And I go to the log in page