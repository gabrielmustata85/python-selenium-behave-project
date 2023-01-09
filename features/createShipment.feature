Feature: Create Shipment

  Scenario Outline:Create Shipment
    Given User starts the app
    And User enter the email
    And User enter the password
    When User clicks on the Login button
    Then The homepage should be displayed
    And User clicks on Shipments button
    And User clicks on Create a Shipment button
    And User clicks Carrier dropdown
    And User selects the "<carrier>"
    And User adds Reference one
    And User adds Business Name
    And User adds Contact
    And User adds Email
    And User adds the Phone Number
    And User adds AddressLine1
    And User adds AddressLine2
    And User adds County
    And User adds City
    And User adds Zip Code
    And User adds the Weight
    When User clicks on Create Shipment button
    Then The green notification message should be visible

    Examples:
      | carrier |  |
      |         |  |
      |         |  |
      |         |  |

