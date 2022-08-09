#!/usr/bin env python

from json import loads
from pytest_bdd import parsers, scenarios, given, when, then
from subprocess import Popen, PIPE


scenarios('../features/list_archived_templates.feature')

RC = -1
STDOUT = b''
STDERR = b''

SAMPLES = [
    {
        'name': 'Archived1',
        'version': '1.0',
        'content': 'Test Content'
    },
    {
        'name': 'Archived2',
        'version': '1.1',
        'content': '''Test 2 {}'''
    },
    {
        'name': 'Archived2',
        'version': '2.1',
        'content': '''Test Content 3 {{%$#@!^";,"""}}'''
    }
]


def cmd(cmd: str):
    global RC
    global STDOUT
    global STDERR
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    STDOUT, STDERR = p.communicate()
    RC = p.returncode


def reset_db():
    cmd("src/stupa reset")
    assert RC == 0


def insert_sample(index):
    n = SAMPLES[index]['name']
    v = SAMPLES[index]['version']
    c = SAMPLES[index]['content']
    cmd('''
        src/stupa           \
            --name={}       \
            --version={}    \
            --content={}    \
            create
    '''.format(n, v, c))
    assert RC == 0
    cmd("src/stupa --id={} archive".format(index + 1))
    assert RC == 0


def insert_samples(count):
    i = 0
    while count > 0 and i < count:
        insert_sample(i)
        i = i + 1


@given(parsers.parse('there are {count:d} archived template(s)'))
def check_archived_templates(count):
    reset_db()
    insert_samples(count)
    cmd("src/stupa -j count_archived")
    assert RC == 0
    assert loads(STDOUT)['count'] == count


@when('stupa -j archived is invoked successfully')
def run_archived_json():
    cmd("src/stupa -j archived")
    assert RC == 0


@when('stupa archived is invoked successfully')
def run_archived():
    cmd("src/stupa archived")
    assert RC == 0


@then('"status": "OK" is printed')
def check_status_OK_json():
    assert loads(STDOUT)['status'] == 'OK'


@then('OK: is printed')
def check_status_OK():
    assert 'OK: ' in STDOUT.decode('utf-8')


@then(parsers.parse('{count:d} template(s) found is printed'))
def check_count(count):
    assert f'{count} template(s) found' in STDOUT.decode('utf-8')


@then(parsers.parse('"count": {count:d} is printed'))
def check_count_json(count):
    assert loads(STDOUT)['count'] == count


@then(parsers.parse('JSON array with {count:d} "templates" is printed'))
def check_templates_array(count):
    if count == 0:
        assert loads(STDOUT)['templates'] is None
    else:
        assert len(loads(STDOUT)['templates']) == count


@then(parsers.parse('template listing with {count:d} item(s) is printed'))
def check_template_listing(count):
    assert STDOUT.decode('utf-8').count('id_=') == count
