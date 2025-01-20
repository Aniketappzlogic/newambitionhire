import time

import pytest


class BasePage(object):

    base_url = None

    def __init__(self, driver):
        self.driver = driver

    def get(self, env):
        if env == 'dev':
            self.base_url = 'https://dev-recruiter.ambitionhire.ai/login'
        if env == 'services':
            self.base_url = 'https://services-recruiter.ambitionhire.ai/login'
        url = self.base_url
        print(url)
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("Url entered")
