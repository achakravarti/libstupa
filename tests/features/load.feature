Feature: Loading a template
  As a client user/program
  I want to load the details of a single template
  So that I can view it


  Scenario: Load template details in JSON
    Given there are 3 active template(s)

    When stupa -j --id=2 load is invoked

    Then status "OK" is printed in JSON
    And JSON object "template" is printed
    And exit code 0 is returned


  Scenario: Load template details without JSON
    Given there are 3 active template(s)

    When stupa --id=2 load is invoked

    Then status "OK" is printed in plain text
    And template details are printed
    And exit code 0 is returned


  Scenario: Load non-existent template details in JSON
    Given there are 0 active template(s)

    When stupa -j --id=2 load is invoked

    Then status "ENA" is printed in JSON
    And error "Not Found" is printed in JSON
    And exit code 4 is returned


  Scenario: Load non-existent template details without JSON
    Given there are 0 active template(s)

    When stupa --id=2 load is invoked

    Then status "ENA" is printed in plain text
    And error "Not Found" is printed in plain text
    And exit code 4 is returned
