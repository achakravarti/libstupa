Feature: Listing active templates
  As a client user/program
  I want to list my active templates
  So that I can get a snapshot of them

  Scenario: Listing results in JSON when there are 0 active templates
    Given there are no active templates
    When stupa -js active is invoked successfully
    Then "status": "OK" is printed
    Then "count": 0 is printed
    Then null "templates" JSON array is printed

  Scenario: Listing results without JSON when there are 0 active templates
    Given there are no active templates
    When stupa -s active is invoked sucessfully
    Then OK: is printed
    Then 0 template(s) found is printed
    Then template listing is not printed

  Scenario: Listing results in JSON when there is 1 active template
    Given there is 1 active template
    When stupa -js active is invoked
    Then "status": "OK" is printed
    Then "count": 1 is printed
    Then "templates" JSON array with 1 item is printed

  Scenario: Listing results without JSON when there is 1 active template
    Given there is 1 active template
    When stupa -s active is invoked successfully
    Then OK: is printed
    Then 1 template(s) found is printed
    Then template listing with 1 item is printed

  Scenario: Listing results in JSON when there are 3 active templates
    Given there are 3 active template
    When stupa -js active is invoked
    Then "status": "OK" is printed
    Then "count": 3 is printed
    Then "templates" JSON array with 3 items is printed

  Scenario: Listing results without JSON when there are 3 active templates
    Given there are 3 active templates
    When stupa -s active is invoked successfully
    Then OK: is printed
    Then 3 template(s) found is printed
    Then template listing with 3 items is printed
