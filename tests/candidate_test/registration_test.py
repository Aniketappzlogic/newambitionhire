import email
import imaplib
import logging
import re
import time
from datetime import datetime
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver, env
from Pages_Candidate.registration import Registration

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")



@pytest.mark.registration
def test_registration(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    registration = Registration(driver)
    driver.implicitly_wait(5)
    registration.registartion_name_btn.send_keys('MRIDUL')
    driver.implicitly_wait(2)
    registration.email_btn.send_keys('mridulsaxena@gmail.com')
    registration.phoneno_btn.send_keys('7503078450')
    registration.location_btn.send_keys('Uttar Pradesh: Noida')
    driver.implicitly_wait(10)
    registration.condition_btn.click()
    time.sleep(2)
    registration.sendotp_btn.click()
    time.sleep(5)
    registration.Sendingotp_text('667890')
    time.sleep(10)
    registration.submitotp_btn.click()
    time.sleep(2)

