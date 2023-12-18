Feature: Login to the SauceDemo website

  Scenario: User logs in with valid credentials
    Given the user is on the login page
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the user should be logged in successfully
