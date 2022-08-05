#!/usr/bin env python


import pytest
from pytest_bdd import scenarios, given, when, then


scenarios('../features/archive_template.feature')


@given('there is an active template with ID 1')
def check_template_id_1_active():
    pass


@when('`stupa --id=1 archive` is invoked')
def archive_template_id_1():
    pass


@then('the template with ID 1 is archived')
def check_template_id_1_archived():
    pass
