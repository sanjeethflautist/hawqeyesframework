
import pytest
from selenium.webdriver import Chrome



def pytest_addoption(parser):

    '''
    This function will automatically parse the arguments from pytest command lines
    Use request.config.getoption("--argmentname") for getting the arguments'
    '''

    parser.addoption(
        "--env", 
        action="store",
        default='UAT',
        help="Environment to run tests against. Supported environments are PDT,UAT and DEV"
    )
    parser.addoption(
        "--app",
        action="store",
        default='APPNAME',
        help="APPs to run tests against"
    )
    parser.addoption(
        "--profile",
        action="store",
        default='SUPERVISOR',
        help="profile to run the test against"
    )
    parser.addoption(
        "--synctimedelta",
        action="store",
        default=0,
        help="If we want to alter the default sync time for objects we can specify it from CMD. Example, if 20 is the default time out, if we specify --synctimedelta=-10, then this will get added to the default sync time. So sync time becomes 20+(-10) that is 10s"
    )



@pytest.fixture(scope="session",autouse=True)
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session",autouse=True)
def synctimedelta(request):
    return request.config.getoption("--synctimedelta")



@pytest.fixture(scope="function",autouse=False)
def browser():
  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()



