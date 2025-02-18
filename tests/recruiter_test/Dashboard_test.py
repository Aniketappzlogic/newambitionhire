import logging
import time
from asyncio import wait_for
from datetime import datetime
from time import sleep
from Pages_Candidate.explore_jobs import ExploreJobs


import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Page_Recruiter.login import Loginrecruiter
from conftest import driver, env
from Page_Recruiter.Dashboard_page import Dashboard, AllJobs, PrivateJobs, BasePage, PublicJobs, ActiveJobs, SearchJob, \
    Searchbutton, InactiveJobs, ViewDetails, CloseDetails, DownloadReport

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


@pytest.mark.regression
@pytest.mark.dashboard_page
def test_dashboard_page(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    login = authenticated_user_recruiter
    logging.info(f"logged in")
    time.sleep(10)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//h2[text()='Private Jobs'])"))
    )
    #
    dashboard_page = Dashboard(driver)
    dashboard_page.dashboard_btn.click()
    logging.info(f"dashboard clicked")

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

    viewdetail = ViewDetails(driver)
    viewdetail.view_details.click()
    logging.info(f"view detail clicked")

    closedetails = CloseDetails(driver)
    closedetails.close_details.click()

    downloadreport = DownloadReport(driver)
    downloadreport.download_report.click()

    recommendation = DownloadReport(driver)
    recommendation.recommendation_btn().click()

    time.sleep(10)



# ---------------------------
@pytest.mark.xyzjob
def test_searchandapplyjob(env, driver, authenticated_user_candidate):
    logging.info(f"environment -> {env}")
    login = authenticated_user_candidate
    time.sleep(7)
    explore = ExploreJobs(driver)
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








