Feature: Create a new address

  Scenario: Create a valid address
    Given User starts the app
    And User enter the email
    And User enter the password
    When User clicks on the Login button
    Then The homepage should be displayed

    And User clicks on Addresses
    And User clicks on Manage Addresses
    And User clicks on New Address
    And User adds Address Business Name
    And User adds Address Line1
    And User adds Address Line2
    And User adds Address County
    And User adds Address City
    And User adds First Name
    And User adds Last Name
    And User adds Phone Area Prefix
    And User adds Contact Phone Number
    And User adds Address Email
    And User adds Post Zip Code
    When User clicks on Create Address button
    Then The new address is created