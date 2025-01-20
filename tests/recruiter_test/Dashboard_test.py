import logging
import time
from asyncio import wait_for
from datetime import datetime
from time import sleep

import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Page_Recruiter.login import Loginrecruiter
from conftest import driver, env
from Page_Recruiter.Dashboard_page import Dashboard, AllJobs, PrivateJobs, BasePage, PublicJobs, ActiveJobs, SearchJob, Searchbutton, InactiveJobs, ViewDetails

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


@pytest.mark.regression
@pytest.mark.dashboard_page
def test_dashboard_page(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    recruiter_login = Loginrecruiter(driver)
    recruiter_login.username_btn.send_keys('inderjeetkmcs@gmail.com')
    recruiter_login.password_btn.send_keys('123')
    recruiter_login.hidepassword_btn.click()
    recruiter_login.login_btn.click()
    time.sleep(30)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//h2[text()='Private Jobs'])"))
    )

    dashboard_page = Dashboard(driver)
    dashboard_page.dashboard_btn.click()

    all_job = AllJobs(driver)
    all_job.all_jobs_card.click()

    private_job=PrivateJobs(driver)
    private_job.private_jobs_card.click()

    public_job = PublicJobs(driver)
    public_job.public_jobs_card.click()

    activejob = ActiveJobs(driver)
    activejob.active_jobs_card.click()

    inactive_job = InactiveJobs(driver)
    inactive_job.inactive_jobs_card.click()

    search_jobs = SearchJob(driver)
    search_jobs.search_job.send_keys('testing 0901')

    # search_btn = Searchbutton(driver)
    # search_btn.search_btn.click()

    time.sleep(5)
    # viewdetail = ViewDetails(driver)
    # viewdetail.view_details.click()







