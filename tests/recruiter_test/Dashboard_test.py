import logging
import json
from datetime import datetime
import pytest
from assertpy import assert_that
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Page_Recruiter.login import Loginrecruiter
from conftest import driver, env
from Page_Recruiter.Dashboard_page import Dashboard

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")

#TC01
@pytest.mark.regression
@pytest.mark.view_dashboard_page
def test_view_dashboard_page(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    dashboard_page = Dashboard(driver)
    dashboard_page.dashboard_btn.click()
    logging.info(f"dashboard clicked")
    logging.info("DASHBOARD PAGE LOADED")

#TC02
@pytest.mark.regression
@pytest.mark.alljobs_count_dashboard_page
def test_allJobs_count_dashboard_page(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
     EC.visibility_of_element_located((By.XPATH,"//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
    alljobs_count = Dashboard(driver)
    alljobsnum = alljobs_count.all_jobs_count.get_text().strip()
    jobcount = ''.join(filter(str.isdigit, alljobsnum))
    logging.info(f"Text: {alljobsnum}")
    logging.info(f"Count: {jobcount}")
    assert_that(jobcount).is_not_empty().is_digit()
    assert_that(int(jobcount)).is_greater_than(0)

@pytest.mark.regression
@pytest.mark.privatejobs_count_dashboard_page
def test_privateJobs_count_dashboard_page(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
     EC.visibility_of_element_located((By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
           )
    privatejobs_count = Dashboard(driver)
    privatejobsnum = privatejobs_count.private_jobs_count.get_text().strip()
    jobcount = ''.join(filter(str.isdigit, privatejobsnum))
    logging.info(f"Text: {privatejobsnum}")
    logging.info(f"Count: {jobcount}")
    assert_that(jobcount).is_not_empty().is_digit()
    assert_that(int(jobcount)).is_greater_than(0)

@pytest.mark.regression
@pytest.mark.publicjobs_count_dashboard_page
def test_publicjobs_count_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        publicjobs_count = Dashboard(driver)
        publicjobsnum = publicjobs_count.public_jobs_count.get_text().strip()
        jobcount = ''.join(filter(str.isdigit, publicjobsnum))
        logging.info(f"Text: {publicjobsnum}")
        logging.info(f"Count: {jobcount}")
        assert_that(jobcount).is_not_empty().is_digit()
        assert_that(int(jobcount)).is_greater_than(0)

@pytest.mark.regression
@pytest.mark.activejobs_count_dashboard_page
def test_activejobs_count_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        publicjobs_count = Dashboard(driver)
        publicjobsnum = publicjobs_count.active_jobs_count.get_text().strip()
        jobcount = ''.join(filter(str.isdigit, publicjobsnum))
        logging.info(f"Text: {publicjobsnum}")
        logging.info(f"Count: {jobcount}")
        assert_that(jobcount).is_not_empty().is_digit()
        assert_that(int(jobcount)).is_greater_than(0)

@pytest.mark.regression
@pytest.mark.inactivejobs_count_dashboard_page
def test_inactivejobs_count_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        publicjobs_count = Dashboard(driver)
        publicjobsnum = publicjobs_count.active_jobs_count.get_text().strip()
        jobcount = ''.join(filter(str.isdigit, publicjobsnum))
        logging.info(f"Text: {publicjobsnum}")
        logging.info(f"Count: {jobcount}")
        assert_that(jobcount).is_not_empty().is_digit()
        assert_that(int(jobcount)).is_greater_than(0)


@pytest.mark.regression
@pytest.mark.alljobs_filter_dashboard_page
def test_alljobs_filter_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        alljobs_filter = Dashboard(driver)
        alljobs_filter.all_jobs_card.click()
        alljobsfilter = alljobs_filter.filtered_jobs.get_text()
        assert_that(alljobsfilter).contains("Multilingual Result Fix 1802")
        #logging.info(json.dumps({"alljobsfilter": alljobsfilter}))


@pytest.mark.regression
@pytest.mark.privatejobs_filter_dashboard_page
def test_privatejobs_filter_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        privatejobs_filter = Dashboard(driver)
        privatejobs_filter.private_jobs_card.click()
        privatejobsfilter = privatejobs_filter.filtered_jobs.get_text()
        assert_that(privatejobsfilter).contains("Store Manager - VMart")

@pytest.mark.regression
@pytest.mark.publicjobs_filter_dashboard_page
def test_publicjobs_filter_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        publicjobs_filter = Dashboard(driver)
        publicjobs_filter.public_jobs_card.click()
        publicjobsfilter = publicjobs_filter.filtered_jobs.get_text()
        assert_that(publicjobsfilter).contains("Test Job 0701")

@pytest.mark.regression
@pytest.mark.activejobs_filter_dashboard_page
def test_activejobs_filter_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        activejobs_filter = Dashboard(driver)
        activejobs_filter.active_jobs_card.click()
        activejobsfilter = activejobs_filter.filtered_jobs.get_text()
        assert_that(activejobsfilter).contains("KT JOB")


@pytest.mark.regression
@pytest.mark.inactivejobs_filter_dashboard_page
def test_inactivejobs_filter_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        inactivejobs_filter = Dashboard(driver)
        inactivejobs_filter.inactive_jobs_card.click()
        inactivejobsfilter = inactivejobs_filter.filtered_jobs.get_text()
        assert_that(inactivejobsfilter).contains("Data Scientist")


@pytest.mark.regression
@pytest.mark.searchjob_dashboard_page
def test_searchjob_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        searchjob = Dashboard(driver)
        searchjob.search_job.send_keys('ONE WAY 1202')
        searchresult = searchjob.filtered_jobs.get_text()
        assert_that(searchresult).contains('ONE WAY 1202')


@pytest.mark.regression
@pytest.mark.viewdetails_dashboard_page
def test_viewdetails_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        viewdetails = Dashboard(driver)
        viewdetailstext = viewdetails.view_details.get_text()
        logging.info(viewdetailstext)
        assert_that(viewdetailstext).contains("View Details")
        viewdetails.view_details.click()
        logging.info("Clicked on 'View Details' button.")

        closebtntext = viewdetails.close_details.get_text()
        logging.info(closebtntext)
        assert_that(closebtntext).contains('Close')
        viewdetails.close_details.click()
        logging.info("Clicked on 'Close' button.")


@pytest.mark.regression
@pytest.mark.jobdetails_dashboard_page
def test_viewdetails_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        jobdetails = Dashboard(driver)
        jobdetails.view_details.click()
        logging.info("view detail clicked")

        if jobdetails.nodata.is_element_visible():

              logging.info("No data available")

              nodata_text = jobdetails.nodata.get_text()

              logging.info(f"Text found: {nodata_text}")

        elif jobdetails.graph_detail.is_element_visible():

            logging.info('Graph is Displayed')
            assert_that(jobdetails.graph_detail.is_element_visible()).is_true()

        else:
            logging.error("Neither graph nor 'No data available' message found.")
            assert_that(False).is_true()
        #
        # jobdetails = Dashboard(driver)
        # jobdetails.view_details.click()
        # logging.info("view detail clicked")

        # if jobdetails.graph_detail.is_element_visible():
        #
        #     logging.info('Graph is Displayed')
        #     assert_that(jobdetails.graph_detail.is_element_visible()).is_true()
        #
        # elif jobdetails.nodata.is_element_visible():
        #
        #     logging.info("No data available")
        #
        #     nodata_text = jobdetails.nodata.get_text()
        #
        #     logging.info(f"Text found: {nodata_text}")
        #
        # else:
        #     logging.error("Neither graph nor 'No data available' message found.")
        #     assert_that(False).is_true()  # Force failure if neither element is found



@pytest.mark.regression
@pytest.mark.downloadreport_dashboard_page
def test_downloadreport_dashboard_page(env, driver, authenticated_user_recruiter):
        logging.info(f"environment -> {env}")
        login = authenticated_user_recruiter
        logging.info(f"logged in")
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]"))
        )
        downloadreport = Dashboard(driver)
        downloadreport.download_report.click()






























