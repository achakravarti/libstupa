from json import loads
from pytest import fixture
from pytest_bdd import parsers, scenarios, given, when, then
from subprocess import Popen, PIPE


@fixture
def output():
    return {
        'RC': -1,
        'STDOUT': b'',
        'STDERR': b''
    }


@fixture
def samples():
    return [{
            'name': 'Active1',
            'version': '1.0',
            'content': 'Test Content'
        }, {
            'name': 'Active2',
            'version': '1.1',
            'content': '''Test 2 {}'''
        }, {
            'name': 'Active2',
            'version': '2.1',
            'content': '''Test Content 3 {{%$#@!^";,"""}}'''
        }]


def cmd(cmd: str, output):
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    output['STDOUT'], output['STDERR'] = p.communicate()
    output['RC'] = p.returncode


def reset_db(output):
    cmd("src/stupa reset", output)
    assert output['RC'] == 0


def insert_sample(index, output, samples):
    n = samples[index]['name']
    v = samples[index]['version']
    c = samples[index]['content']
    cmd('''
        src/stupa           \
            --name={}       \
            --version={}    \
            --content={}    \
            create
    '''.format(n, v, c), output)
    assert output['RC'] == 0


def insert_archived_sample(index, output, samples):
    n = samples[index]['name']
    v = samples[index]['version']
    c = samples[index]['content']
    cmd('''
        src/stupa           \
            --name={}       \
            --version={}    \
            --content={}    \
            create
    '''.format(n, v, c), output)
    assert output['RC'] == 0
    cmd("src/stupa --id={} archive".format(index + 1), output)
    assert output['RC'] == 0


def insert_samples(count, output, samples):
    i = 0
    while count > 0 and i < count:
        insert_sample(i, output, samples)
        i = i + 1


def insert_archived_samples(count, output, samples):
    i = 0
    while count > 0 and i < count:
        insert_archived_sample(i, output, samples)
        i = i + 1


@given(parsers.parse('there are {count:d} active template(s)'))
def check_active_templates_count(count, output, samples):
    reset_db(output)
    insert_samples(count, output, samples)
    cmd("src/stupa -j count-active", output)
    assert output['RC'] == 0
    assert loads(output['STDOUT'])['count'] == count


@given(parsers.parse('there are {count:d} archived template(s)'))
def check_archived_templates_count(count, output, samples):
    reset_db(output)
    insert_archived_samples(count, output, samples)
    cmd("src/stupa -j count-archived", output)
    assert output['RC'] == 0
    assert loads(output['STDOUT'])['count'] == count


@then(parsers.parse('template count of {count:d} is reported in plain text'))
def check_template_listing_count_plain(count, output):
    assert f'{count} template(s) found' in output['STDOUT'].decode('utf-8')


@then(parsers.parse('template count of {count:d} is reported in JSON'))
def check_template_listing_count_json(count, output):
    assert loads(output['STDOUT'])['count'] == count


@then(parsers.parse('exit code {code:d} is returned'))
def check_exit_code(code, output):
    assert output['RC'] == code


@then(parsers.parse('status "{status}" is printed in plain text'))
def check_status_plain(status, output):
    assert status in output['STDOUT'].decode('utf-8')


@then(parsers.parse('status "{status}" is printed in JSON'))
def check_status_json(status, output):
    assert loads(output['STDOUT'])['status'] == status


@then(parsers.parse('error "{error}" is printed in plain text'))
def check_error_plain(error, output):
    assert error in output['STDOUT'].decode('utf-8')


@then(parsers.parse('error "{error}" is printed in JSON'))
def check_error_json(error, output):
    assert loads(output['STDOUT'])['error'] == error


@then(parsers.parse('summary of {count:d} template(s) is printed in plain text'))
def check_template_summary_count_plain(count, output):
    lines = output['STDOUT'].decode('utf-8').splitlines()
    icount = ncount = vcount = 0
    for x in lines:
        if x.startswith('id:'):
            icount = icount + 1
        if x.startswith('name:'):
            ncount = ncount + 1
        if x.startswith('version:'):
            vcount = vcount + 1
    assert icount == count
    assert ncount == count
    assert vcount == count


@then(parsers.parse('summary of {count:d} template(s) is printed in JSON'))
def check_template_summary_count_json(count, output):
    j = loads(output['STDOUT'])['templates']
    if count == 0:
        assert j is None
    else:
        assert len(j) == count
        i = 0
        while i < count:
            assert 'id' in j[i]
            assert 'name' in j[i]
            assert 'version' in j[i]
            i = i + 1


@then(parsers.parse(
    'template {t:d} property "{key}" matches with sample {s:d} in JSON'))
def check_key_match_json(t, s, key, samples, output):
    j = loads(output['STDOUT'])['templates']
    assert j[t][key] == samples[s][key]


@then(parsers.parse(
    'template {t:d} property "{key}" matches with sample {s:d} in plain text'))
def check_key_match_plain(t, s, key, samples, output):
    lines = output['STDOUT'].decode('utf-8').splitlines()
    i = -1
    for x in lines:
        if x.startswith(key + ':'):
            i = i + 1
            if i == t:
                assert x.split(key + ':')[1].strip() == samples[s][key]
    assert i > -1
