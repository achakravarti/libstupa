#!/usr/bin env python


import pytest
from pytest_bdd import scenarios, given, when, then


scenarios('../features/archive_template.feature')


@given('there is an active template with ID 1')
def check_template_id_1_active():
    print('check_template_id_1_active')
    assert 1 == 1


@when('`stupa --id=1 archive` is invoked')
def archive_template_id_1():
    print('archive_template_id_1')
    assert 1 == 1


@then('the template with ID 1 is archived')
def check_template_id_1_archived():
    print('template with ID 1 is archived')
    assert 1 == 0
