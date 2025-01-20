import configparser
import os
from collections import namedtuple
import pytest
import logging
from datetime import datetime
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Pages_Candidate.login import Login
from config import Config
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

config = configparser.ConfigParser()
config.read('.env')
load_dotenv()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests on"
    )
    parser.addoption(
        "--myBrowser",
        action="store",
        help="myBrowser to run tests on"
    )


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def myBrowser(request):
    return request.config.getoption("--myBrowser")


@pytest.fixture(scope='session')
def test_config(env):
    cfg = Config(env)
    print(type(cfg))
    return cfg


@pytest.fixture(scope="session")
def driver(myBrowser):
    global driver
    logging.info(myBrowser)
    if myBrowser == 'chrome':
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--use-fake-ui-for-media-stream")
        # options.add_experimental_option("debuggerAddress","localhost:5678")
        # options.add_argument("--use-fake-device-for-media-stream")
        try:
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service= service, options=options)
            driver.maximize_window()
        except Exception as e:
            logging.info(f"Driver not found: {e}")
    elif myBrowser == 'edge':
        try:
            driver = webdriver.Edge()
        except Exception as e:
            logging.info(f"Driver not found: {e}")
    elif myBrowser == 'firefox':
        try:
            driver = webdriver.Firefox()
        except Exception as e:
            logging.info(f"Driver not found: {e}")
    else:
        raise ValueError(f"Unsupported browser: {myBrowser}")

    driver.implicitly_wait(15)
    yield driver
    driver.quit()


# import logging
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
#
# # Replace with the actual path to chromedriver.exe
# chrome_driver_path = r'C:\Users\AppzLogic\Desktop\Ambitionhire\driver\chromedriver.exe'
#
# @pytest.fixture(scope="session")
# def driver(myBrowser):
#     global driver
#     logging.info(myBrowser)
#     if myBrowser == 'chrome':
#         options = Options()
#         options.add_argument("--window-size=1920,1080")
#         options.add_argument("--use-fake-ui-for-media-stream")
#         # options.add_experimental_option("debuggerAddress","localhost:5678")
#         # options.add_argument("--use-fake-device-for-media-stream")
#         try:
#             service = ChromeService(executable_path=chrome_driver_path)
#             driver = webdriver.Chrome(service=service, options=options)
#             driver.maximize_window()
#         except Exception as e:
#             logging.info(f"Driver not found: {e}")
#     elif myBrowser == 'edge':
#         try:
#             driver = webdriver.Edge()
#         except Exception as e:
#             logging.info(f"Driver not found: {e}")
#     elif myBrowser == 'firefox':
#         try:
#             driver = webdriver.Firefox()
#         except Exception as e:
#             logging.info(f"Driver not found: {e}")
#     else:
#         raise ValueError(f"Unsupported browser: {myBrowser}")
#     driver.implicitly_wait(15)
#     yield driver
#     driver.quit()


@pytest.fixture(scope="module")
def authenticated_user(env, driver):
    """Fixture to handle login and return the initial dashboard state."""
    login = Login(driver)
    # Open the login page
    login.get(env)
    logger.info("Navigated to login page.")

