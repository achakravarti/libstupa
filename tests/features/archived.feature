Feature: Listing archived templates
  As a client user/program
  I want to list my archived templates
  So that I can get a snapshot of them

  Scenario: Listing results in JSON when there are 0 archived templates
    Given there are 0 archived template(s)
    When stupa -j archived is invoked successfully
    Then "status": "OK" is printed
    Then "count": 0 is printed
    Then JSON array with 0 "templates" is printed

  Scenario: Listing results without JSON when there are 0 archived templates
    Given there are 0 archived template(s)
    When stupa archived is invoked successfully
    Then OK: is printed
    Then 0 template(s) found is printed
    Then template listing with 0 item(s) is printed

  Scenario: Listing results in JSON when there is 1 archived template
    Given there are 1 archived template(s)
    When stupa -j archived is invoked successfully
    Then "status": "OK" is printed
    Then "count": 1 is printed
    Then JSON array with 1 "templates" is printed

  Scenario: Listing results without JSON when there is 1 archived template
    Given there are 1 archived template(s)
    When stupa archived is invoked successfully
    Then OK: is printed
    Then 1 template(s) found is printed
    Then template listing with 1 item(s) is printed

  Scenario: Listing results in JSON when there are 3 archived templates
    Given there are 3 archived template(s)
    When stupa -j archived is invoked successfully
    Then "status": "OK" is printed
    Then "count": 3 is printed
    Then JSON array with 3 "templates" is printed

  Scenario: Listing results without JSON when there are 3 archived templates
    Given there are 3 archived template(s)
    When stupa archived is invoked successfully
    Then OK: is printed
    Then 3 template(s) found is printed
    Then template listing with 3 item(s) is printed
