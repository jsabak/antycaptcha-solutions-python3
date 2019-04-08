import pytest
from fixture.application import Application


@pytest.fixture(scope='session')
def fixture(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


__author__ = 'GiSDeCain'
