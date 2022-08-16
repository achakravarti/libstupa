from pytest_bdd import scenarios, when
from .conftest import *


scenarios('../features/list-archived.feature')


@when('stupa -j list-archived is invoked successfully')
def run_archived_json(output):
    cmd("src/stupa -j list-archived", output)
    assert output['RC'] == 0


@when('stupa list-archived is invoked successfully')
def run_archived(output):
    cmd("src/stupa list-archived", output)
    assert output['RC'] == 0
