import pytest
from selenium import webdriver

SEED = '7456bec7-98df-46c0-82a4-acb02c81712f'


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
    def __str__(self):
        return __dict__


@pytest.fixture(scope='module', params=['prod'])
def environment(request):
    env = Environment()
    if request.param == 'prod':
        env.base_url = 'https://antycaptcha.amberteam.pl:5443/'
    elif request.param == 'test':
        env.base_url = ' http://127.0.0.1:5000/'
    else:
        assert False, "Unknown environment type."
    env.seed = SEED
    return env



