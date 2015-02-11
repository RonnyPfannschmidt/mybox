import pytest
from mybox.backend import sql, maildir, memory


@pytest.fixture(
    params=[sql, maildir, memory],
    ids=['sql', 'maildir', 'memory'])
def backend(request):
    if request.param is sql:
        pytest.skip()
        arg = 'sqlite://'
    elif request.param is maildir:
        arg = request.getfuncargvalue('tmpdir').join('maildir')
    else:
        arg = {}
    return request.param.Backend.create(arg)


def test_tree_emty(backend):
    assert backend.tree() == {}


def test_add_folder(backend):
    backend.add_folder('inbox')

    assert backend.tree() != {}
