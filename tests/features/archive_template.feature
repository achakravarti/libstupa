Feature: Archiving a template
  As a client user/program
  I want to archive an old template
  So that it no longer appears on my active list

  Scenario: Archiving an active template
    Given there is an active template with ID 1
    When `stupa --id=1 archive` is invoked
    Then the template with ID 1 is archived

  Scenario: Archiving a non-existent template

  Scenario: Archiving an archived template
