import logging
import time
from datetime import datetime
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages_Candidate.Userprofile import Userprofile
from conftest import driver, env
from Pages_Candidate.login import Login
import pyautogui
from Pages_Candidate.explore_jobs import ExploreJobs

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


@pytest.mark.searchjob
def test_login(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    Pagelogin = Login(driver)
    explore = ExploreJobs(driver)
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)
    explore.searchjob_btn.send_keys("English Testing")
    time.sleep(5)


@pytest.mark.searchandapplyjob
def test_searchandapplyjob(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    Pagelogin = Login(driver)
    explore = ExploreJobs(driver)
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)
    explore.result_page_btn.click()
    explore.searchjob_btn.send_keys("TESTING -WEB")
    time.sleep(2)
    explore.applyjob_btn.click()
    time.sleep(10)
    explore.proceed_to_apply_btn.click()
    time.sleep(10)
    explore.refrence_soucre.send_keys('resource_source')
    time.sleep(5)
    explore.select_exam_language_btn.click()
    driver.implicitly_wait(5)
    explore.select_language_btn.click()
    time.sleep(5)


@pytest.mark.socialmedialinks
def test_socialmedialinks(authenticated_user, driver, env):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    Pagelogin = Login(driver)
    explore = ExploreJobs(driver)
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)
    explore.result_page_btn.click()
    explore.searchjob_btn.send_keys("TESTING -WEB")
    time.sleep(2)
    explore.applyjob_btn.click()
    time.sleep(10)
    # explore.socailmedialink_1.click()
    actions = ActionChains(driver)
    button = driver.find_element(By.XPATH, "//a[contains(text(),'https://www.ambitionhire.ai/')]")
    actions.click(button).perform()
    time.sleep(10)
    original_window = driver.current_window_handle
    driver.switch_to.window(original_window)
    time.sleep(5)
    buttonone = driver.find_element(By.XPATH, "//a[contains(text(),'LinkedIn Profile Link')]")
    actions.click(buttonone).perform()
    time.sleep(10)
    original_window = driver.current_window_handle
    driver.switch_to.window(original_window)
    time.sleep(2)


@pytest.mark.description_video
def test_description_video(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    Pagelogin = Login(driver)
    explore = ExploreJobs(driver)
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(7)
    explore.result_page_btn.click()
    explore.searchjob_btn.send_keys("TESTING -WEB")
    time.sleep(2)
    explore.applyjob_btn.click()
    time.sleep(10)
    iframe = driver.find_element(By.XPATH, "//iframe[@class='rounded-2xl']")
    driver.switch_to.frame(iframe)
    description_video =driver.find_element(By.XPATH,"//button[@title='Play']")
    description_video.click()
    time.sleep(10)
    driver.switch_to.default_content()
    time.sleep(5)



