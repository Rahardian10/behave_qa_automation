Feature: Login Feature

Scenario: Success login with correct credential
    Given I am on the login
    When I enter valid credentials
    Then I should be logged in
