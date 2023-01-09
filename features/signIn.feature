Feature: Sign in

  Scenario: Sign in as an Global administrator
    Given User starts the app
    And User enter the email
    And User enter the password
    When User clicks on the Login button
    Then The homepage should be displayed


  Scenario Outline: Sign in with other roles
    Given User starts the app
    And User enter role email "<email>"
    And User enter role password "<password>"
    When User clicks on the Login button
    Then The homepage should be displayed
    Examples:
      | roles             | email | password |
      | Global Admin      |       |          |
      | Customer Shipper  |       |          |
      | Customer Admin    |       |          |
      | Operation Manager |       |          |
      | Operation Admin   |       |          |


