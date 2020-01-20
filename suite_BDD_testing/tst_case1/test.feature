
Feature: A new table

    Scenario: The address book should be blank

        Given the application is running
         When a new table is created
         Then the table should be blank