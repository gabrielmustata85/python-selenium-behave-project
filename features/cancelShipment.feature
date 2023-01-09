Feature: Cancel Shipment

    Scenario: Cancel Shipment
        Given User starts the app
        And User enter the email
        And User enter the password
        When User clicks on the Login button
        Then The homepage should be displayed
        And User clicks on Shipments button
        And User clicks on Manage Shipments button
        And User resets the filters
        When User clicks on Cancel button
        Then The shipment is canceled
    

    