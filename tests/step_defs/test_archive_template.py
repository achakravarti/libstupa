#!/usr/bin env python


from pytest import fixture
from pytest_bdd import scenarios, given, when, then
from subprocess import Popen, PIPE


scenarios('../features/archive_template.feature')


@fixture
def setupdb():
    p = Popen("src/stupa -s --id=1 load", stdout=PIPE, stderr=PIPE, shell=True)
    o, e = p.communicate()
    rc = p.returncode



@given('there is an active template with ID 1')
def check_template_id_1_active():
    p = Popen("src/stupa -H", stdout=PIPE, stderr=PIPE, shell=True)
    o, e = p.communicate()
    rc = p.returncode
    #print(o.decode('utf-8'))
    #print(rc)
    assert rc == 0


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


@when('stupa archive is invoked')
def archive():
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
