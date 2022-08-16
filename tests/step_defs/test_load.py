from pytest_bdd import scenarios, when
from .conftest import *


scenarios('../features/load.feature')


@when('stupa -j --id=2 load is invoked')
def run_load_json(output):
    cmd("src/stupa -j --id=2 load", output)


@when('stupa --id=2 load is invoked')
def run_load(output):
    cmd("src/stupa --id=2 load", output)
