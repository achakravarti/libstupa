#!/usr/bin env python


import pytest
from pytest_bdd import scenarios, given, when, then


scenarios('../features/archive_template.feature')


@given('there is an active template with ID 1')
def check_template_id_1_active():
    pass


@given('there is an archived template with ID 2')
def check_template_id_2_archived():
    pass


@given('there is no active template with ID 9999')
def check_template_id_9999_does_not_exist():
    pass


@when('stupa --id=1 archive is invoked')
def archive_template_id_1():
    pass


@when('stupa --id=2 archive is invoked')
def archive_template_id_2():
    pass


@when('stupa --id=9999 archive is invoked')
def archive_template_id_9999():
    pass


@then('the template with ID 1 is archived')
def check_template_id_1_archived():
    pass


@then('a not found error occurs')
def check_not_found_error():
    pass


@then('an invalid operation error occurs')
def check_invalid_operation_error():
    pass


@then('a missing flag error occurs')
def check_missing_flag_error():
    pass
