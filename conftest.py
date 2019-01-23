import pytest
from selenium import webdriver


@pytest.fixture(scope='module', params=['Chrome', 'Firefox', pytest.param('IE', marks=pytest.mark.skip),
                                        pytest.param('Edge', marks=pytest.mark.skip)])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    elif request.param == 'Firefox':
        driver = webdriver.Firefox()
    elif request.param == 'IE':
        driver = webdriver.Ie
    elif request.param == 'Edge':
        driver = webdriver.Edge
    elif request.param == 'Opera':
        driver = webdriver.Opera

    yield driver

    driver.quit()


# class for holding environment parameters
class Environment:
    pass


@pytest.fixture
def prod_environment():
    env = Environment()
    env.base_url = 'https://antycaptcha.amberteam.pl:5443/'

    yield env


@pytest.fixture
def local_environment():
    env = Environment()
    env.base_url = ' http://127.0.0.1:5000/'

    yield env
