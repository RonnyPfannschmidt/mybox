import pytest
from mybox.backend import sql, maildir, memory


@pytest.fixture(
    params=[sql, maildir, memory],
    ids=['sql', 'maildir', 'memory'])
def backend(request):
    if request.param is sql:
        arg = 'memory:'
    elif request.param is maildir:
        arg = request.getfuncargvalue('tmpdir')
    else:
        arg = {}
    return request.param.Backend.create(arg)


def test_tree_emty(backend):
    assert backend.tree() == {}
