import pytest
from mybox.backend import sql, maildir, memory


@pytest.fixture(params=[sql, maildir, memory])
def backend(request, tmpdir):
    if request.param is sql:
        arg = 'sqlite:///%s' % tmpdir
    elif request.param is maildir:
        arg = tmpdir
    else:
        arg = {}
    return request.param.Backend.create(arg)


def test_tree_emty(backend):
    assert backend.tree() == {}
