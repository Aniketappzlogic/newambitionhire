import logging
import time
from datetime import datetime
from time import sleep

import pytest
from selenium.webdriver.common.by import By
# from pynput.keyboard import  Key,Controller
from Pages_Candidate.result_page import Result
from Pages_Candidate.Userprofile import Userprofile
from conftest import driver, env
from Pages_Candidate.login import Login
import pyautogui

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


@pytest.mark.view_result_tab
def test_view_results_tab(env, driver, authenticated_user):
    result = Result(driver)
    Pagelogin = Login(driver)
    time.sleep(3)
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)
    result.result_page.click()
    time.sleep(5)


# @pytest.mark.download_score_card feature removed
# def test_download_score_card(env, driver, authenticated_user):
#     result = Result(driver)
#     Pagelogin = Login(driver)
#     time.sleep(3)
#     Pagelogin.phonenumber_btn.send_keys('7503078450')
#     Pagelogin.sendotp_btn.click()
#     time.sleep(5)
#     Pagelogin.Sendingotp_text.send_keys('000000')
#     Pagelogin.submitotp_btn.click()
#     time.sleep(7)
#     result.result_page.click()
#     time.sleep(5)
#     result.results_checkbox.click()
#     time.sleep(3)
#     result.view_result.click()
#     time.sleep(10)
#     result.download_scorecard.click()
#     driver.implicitly_wait(5)


# @pytest.mark.view_incomplete_jobs feature removed
# def test_view_incomplete_jobs(env, driver, authenticated_user):
#     result = Result(driver)
#     Pagelogin = Login(driver)
#     time.sleep(3)
#     Pagelogin.phonenumber_btn.send_keys('7503078450')
#     Pagelogin.sendotp_btn.click()
#     time.sleep(5)
#     Pagelogin.Sendingotp_text.send_keys('000000')
#     Pagelogin.submitotp_btn.click()
#     time.sleep(7)
#     result.result_page.click()
#     time.sleep(5)
#     result.incompletejob_btn.click()
#     time.sleep(5)


@pytest.mark.view_results
def test_view_results(env, driver, authenticated_user):
    result = Result(driver)
    Pagelogin = Login(driver)
    time.sleep(3)
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)
    result.result_page.click()
    time.sleep(5)


@pytest.mark.search_result
def test_search_result(env, driver, authenticated_user):
    result = Result(driver)
    Pagelogin = Login(driver)
    time.sleep(3)
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)
    result.result_page.click()
    time.sleep(5)
    result.searchjobname.send_keys('EXCEL TEST ROUND 1')
    time.sleep(4)
    result.selectfulljob_btn.click()



@pytest.mark.download_scorecard
def test_download_scorecard(env, driver, authenticated_user):
    result = Result(driver)
    Pagelogin = Login(driver)
    time.sleep(3)
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)
    result.result_page.click()
    time.sleep(5)
    result.searchjobname.send_keys('EXCEL TEST ROUND 1')
    time.sleep(4)
    result.selectfulljob_btn.click()
    result.download_scorecard.click()
    time.sleep(2)

