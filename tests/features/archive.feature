Feature: Archiving a template
  As a client user/program
  I want to archive an old template
  So that it no longer appears on my active list

  Scenario: Archiving an active template
    #Given there are 3 active template(s)
    #When stupa --id=1 archive is invoked
    #Then the template with ID 1 is archived
    #Then OK is printed

  Scenario: Archiving an active template with JSON output
    #Given there are 3 active template(s)
    #When stupa -j --id=1 archive is invoked
    #Then the template with ID 1 is archived
    #Then "status": "OK" is printed

  Scenario: Archiving a non-existent template
    #Given there are 0 active template(s)
    #When stupa --id=1 archive is invoked
    #Then ENA (Not Found) is printed
    #Then exit code 4 is returned

  Scenario: Archiving a non-existent template with JSON output
    #Given there are 0 active template(s)
    #When stupa -j --id=1 archive is invoked
    #Then "status": "ENA" is printed
    #Then "error": "Not Found" is printed
    #Then exit code 4 is returned

  Scenario: Archiving an archived template
    #Given there are 1 active template(s)
    #Given there are 2 archived template(s)
    #When stupa --id=2 archive is invoked
    #Then ENA (Invalid Operation) is printed
    #Then exit code 3 is returned

  Scenario: Archiving an archived template with JSON output
    #Given there are 1 active template(s)
    #Given there are 2 archived template(s)
    #When stupa -j --id=2 archive is invoked
    #Then "status": "EOP" is printed
    #Then "error": "Not Found" is printed
    #Then exit code 3 is returned

  Scenario: Archiving without specifying ID
    #Given there are 3 active template(s)
    #When stupa archive is invoked
    #Then ENA (Invalid Operation) is printed
    #Then exit code 3 is returned

  Scenario: Archiving without specifying ID with JSON output
    #Given there are 3 active template(s)
    #When stupa -j archive is invoked
    #Then "status": "EOP" is printed
    #Then "error": "Not Found" is printed
    #Then exit code 3 is returned
