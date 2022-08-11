Feature: Listing archived templates
  As a client user/program
  I want to list my archived templates
  So that I can get a snapshot of them


  Scenario: Listing results in JSON when there are 0 archived templates
    Given there are 0 archived template(s)

    When stupa -j list-archived is invoked successfully

    Then status "OK" is printed in JSON
    And template count of 0 is reported in JSON
    And summary of 0 template(s) is printed in JSON
    And exit code 0 is returned


  Scenario: Listing results without JSON when there are 0 archived templates
    Given there are 0 archived template(s)

    When stupa list-archived is invoked successfully

    Then status "OK" is printed in plain text
    And template count of 0 is reported in plain text
    And summary of 0 template(s) is printed in plain text
    And exit code 0 is returned


  Scenario: Listing results in JSON when there is 1 archived template
    Given there are 1 archived template(s)

    When stupa -j list-archived is invoked successfully

    Then status "OK" is printed in JSON
    And template count of 1 is reported in JSON
    And summary of 1 template(s) is printed in JSON
    And template 0 property "name" matches with sample 0 in JSON
    And template 0 property "version" matches with sample 0 in JSON
    And exit code 0 is returned


  Scenario: Listing results without JSON when there is 1 archived template
    Given there are 1 archived template(s)

    When stupa list-archived is invoked successfully

    Then status "OK" is printed in plain text
    And template count of 1 is reported in plain text
    And summary of 1 template(s) is printed in plain text
    And exit code 0 is returned


  Scenario: Listing results in JSON when there are 3 archived templates
    Given there are 3 archived template(s)

    When stupa -j list-archived is invoked successfully

    Then status "OK" is printed in JSON
    And template count of 3 is reported in JSON
    And summary of 3 template(s) is printed in JSON
    And template 0 property "name" matches with sample 0 in JSON
    And template 0 property "version" matches with sample 0 in JSON
    And template 1 property "name" matches with sample 1 in JSON
    And template 1 property "version" matches with sample 1 in JSON
    And template 2 property "name" matches with sample 2 in JSON
    And template 2 property "version" matches with sample 2 in JSON
    And exit code 0 is returned


  Scenario: Listing results without JSON when there are 3 archived templates
    Given there are 3 archived template(s)

    When stupa list-archived is invoked successfully

    Then status "OK" is printed in plain text
    And template count of 3 is reported in plain text
    And summary of 3 template(s) is printed in plain text
    And exit code 0 is returned
