
Feature: A new table

     Scenario: Initial state of created table
         Given the application is running
         Then table should have zero entries

    Scenario: The address book should be blank
        Given the application is running
         When a new table is created
         Then the table should be blank

	Scenario: State after adding two entries
	    Given the application is running
	    And I create a new table with two entries
	    | name | surname | email 		| phone |
	    | Anya | Kay     | anyakay@g.com| 1234  |
	    | Lily | Gen     | lilygen@y.com| 1333  |
	    Then '2' entries should bepresent
	    Then first row contain correct data
	    Then second row contain correct data