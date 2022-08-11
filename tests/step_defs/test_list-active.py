from pytest_bdd import scenarios, when
from .conftest import *


scenarios('../features/list-active.feature')


@when('stupa -j list-active is invoked successfully')
def run_active_json(output):
    cmd("src/stupa -j list-active", output)
    assert output['RC'] == 0


@when('stupa list-active is invoked successfully')
def run_active(output):
    cmd("src/stupa list-active", output)
    assert output['RC'] == 0
