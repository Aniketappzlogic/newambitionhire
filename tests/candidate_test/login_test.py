import logging
import time
from datetime import datetime
import pytest
from conftest import driver, env
from Pages_Candidate.login import Login

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


@pytest.mark.login
def test_login(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    Pagelogin = Login(driver)
    time.sleep(3)
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)
    explore_text = Pagelogin.exploretext.get_text()
    print(explore_text)
    assert explore_text == 'Explore Jobs'


@pytest.mark.login_invalid_mobileno
def test_login_invalid_mobileno(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078487')
    Pagelogin.sendotp_btn.click()
    Pagelogin.Sendingotp_text.send_keys('000000')
    time.sleep(5)
    Pagelogin.submitotp_btn.click()
    time.sleep(7)


@pytest.mark.login_invalid_username
def test_login_invalid_username(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Rohan')
    Pagelogin.phonenumber_btn.send_keys('7503078487')
    Pagelogin.sendotp_btn.click()
    Pagelogin.Sendingotp_text.send_keys('000000')
    time.sleep(5)
    Pagelogin.submitotp_btn.click()
    time.sleep(7)


@pytest.mark.resendotp
def test_resendotp(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    Pagelogin = Login(driver)
    time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('')
    time.sleep(70)
    Pagelogin.Resend_otp.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)


@pytest.mark.editnumber
def test_editnumber(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    Pagelogin = Login(driver)
    time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.edit_number.click()
    time.sleep(5)
    Pagelogin.phonenumber_btn.clear()
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)

@pytest.mark.resendotp_three_times
def test_resendotp_three_times(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    Pagelogin = Login(driver)
    time.sleep(3)
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('')
    time.sleep(70)
    Pagelogin.Resend_otp.click()
    time.sleep(70)
    Pagelogin.Resend_otp.click()
    time.sleep(70)
    Pagelogin.Resend_otp.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)
