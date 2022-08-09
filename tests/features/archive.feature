Feature: Archiving a template
  As a client user/program
  I want to archive an old template
  So that it no longer appears on my active list

  Scenario: Archiving an active template
    Given there is an active template with ID 1
    When stupa --id=1 archive is invoked
    Then the template with ID 1 is archived

  Scenario: Archiving a non-existent template
    Given there is no active template with ID 9999
    When stupa --id=9999 archive is invoked
    Then a not found error occurs

  Scenario: Archiving an archived template
    Given there is an archived template with ID 2
    When stupa --id=2 archive is invoked
    Then an invalid operation error occurs

  Scenario: Archiving without specifying ID
    Given there is an active template with ID 1
    When stupa archive is invoked
    Then a missing flag error occurs
