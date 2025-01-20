import logging
import time
from asyncio import wait_for
from datetime import datetime
import pytest
from conftest import driver, env
from Page_Recruiter.login import Loginrecruiter

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


@pytest.mark.regression
@pytest.mark.login_recruiter
def test_login_recruiter(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.username_btn.send_keys('inderjeetkmcs@gmail.com')
    recruiterlogin.password_btn.send_keys('123')
    recruiterlogin.hidepassword_btn.click()
    recruiterlogin.login_btn.click()
    time.sleep(10)


@pytest.mark.regression
@pytest.mark.login_trouble_signing
def test_login_trouble_signing(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.username_btn.send_keys('inderjeetkmcs@gmail.com')
    recruiterlogin.password_btn.send_keys('123')
    recruiterlogin.troublesigning_btn.click()
    driver.implicitly_wait(5)
    recruiterlogin.recoverpassword_email.send_keys('inderjeetkmcs@gmail.com')
    recruiterlogin.sendlink_btn.click()


@pytest.mark.regression
@pytest.mark.login_contact_us
def test_login_contact_us(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.contactus_btn.click()
    time.sleep(5)



@pytest.mark.regression
@pytest.mark.login_page_socialmedialinks
def test_login_page_socialmedialinks(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.social_media_facebook_btn.click()
    time.sleep(5)
    recruiterlogin.social_media_instagram_btn.click()
    time.sleep(5)
    recruiterlogin.social_media_linkdien_btn.click()
    time.sleep(5)


@pytest.mark.login_page_aboutus_page
def test_login_page_socialmedialinks(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.aboutuspage_btn.click()
    recruiterlogin.pricing_page_btn.click()


@pytest.mark.login_page_pricing_and_globe_btn
def test_login_page_pricing_and_globe_btn(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    # login = authenticated_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.pricing_page_btn.click()
    recruiterlogin.globe_icon_btn.click()











