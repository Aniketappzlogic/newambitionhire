import logging
import re
import time
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from datetime import datetime, timedelta
from assertpy import assert_that
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Page_Recruiter.login import Loginrecruiter
from conftest import driver, env
from Page_Recruiter.Jobs_page import Jobs

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")

#TC01
@pytest.mark.regression
@pytest.mark.jobs_page
def test_view_jobs_page(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    logging.info("Jobs Page Loaded Successfully")

#TC02
@pytest.mark.regression
@pytest.mark.jobs_page_activejobs
def test_jobs_page_activejobs(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    jobs_page.active_btn.click()
    logging.info(f"active button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    ActiveJobsCount = jobs_page.active_jobs_count.get_text().strip()
    count = ''.join(filter(str.isdigit, ActiveJobsCount))
    logging.info(f"Text: {ActiveJobsCount}")
    logging.info(f"Count: {count}")
    assert_that(count).is_not_empty().is_digit()
    assert_that(int(count)).is_greater_than(0)

#TC03
@pytest.mark.regression
@pytest.mark.jobs_page_draftsjobs
def test_jobs_page_draftsjobs(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    jobs_page.drafts_btn.click()
    logging.info(f"jobs button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    DraftJobsCount = jobs_page.jobs_count.get_text().strip()
    count = ''.join(filter(str.isdigit, DraftJobsCount))
    logging.info(f"Text: {DraftJobsCount}")
    logging.info(f"Count: {count}")
    assert_that(count).is_not_empty().is_digit()
    assert_that(int(count)).is_greater_than(0)


#TC04
@pytest.mark.regression
@pytest.mark.jobs_page_inactivejobs
def test_jobs_page_inactivejobs(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    jobs_page.inactive_btn.click()
    logging.info(f"jobs button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    InactiveJobsCount = jobs_page.jobs_count.get_text().strip()
    count = ''.join(filter(str.isdigit, InactiveJobsCount))
    logging.info(f"Text: {InactiveJobsCount}")
    logging.info(f"Count: {count}")
    assert_that(count).is_not_empty().is_digit()
    assert_that(int(count)).is_greater_than(0)


@pytest.mark.regression
@pytest.mark.jobs_page_recentjobsfilter
def test_jobs_page_recentjobsfilter(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    JobCardText = jobs_page.top_jobs_card.get_text()
    # current_date = datetime.now().strftime("%B %d,%Y")
    logging.info((JobCardText))

    match = re.search(r"Created on\s*([A-Za-z]+ \d{1,2}, \d{4})", JobCardText)
    if match:
        job_creation_date_str = match.group(1)
        logging.info(f"Extracted Job Creation Date: {job_creation_date_str}")

        # Convert the extracted date string into a datetime object
        job_creation_date = datetime.strptime(job_creation_date_str, "%B %d, %Y")

        # Get the current date
        current_date = datetime.now()

        # Assert using assertpy that the job creation date is less than or equal to today's date
        assert_that(job_creation_date).is_less_than_or_equal_to(current_date)

    else:
        logging.error("No date found in JobCardText!")
        assert False, "Job creation date not found in JobCardText."



@pytest.mark.regression
@pytest.mark.jobs_page_lastweekjobsfilter
def test_jobs_page_lastweekjobsfilter(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.sortby.click()
    jobs_page.lastweek.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    elements =  jobs_page.job_creation_date.find_elements()

    current_date = datetime.now().date()  # Get the current date (ignoring time)
    last_week_start = current_date - timedelta(weeks=1)
    last_week_end = current_date - timedelta(days=0)  # Yesterday (ignoring time)

    logging.info(
        f"Last week date range: {last_week_start.strftime('%B %d, %Y')} to {last_week_end.strftime('%B %d, %Y')}")

    # Loop through each element and validate the job creation date
    for element in elements:
        JobCardText = element.text
        logging.info(f"Job card text: {JobCardText}")

        # Match the date in the format "Created on Month Day, Year"
        match = re.search(r"Created on\s*([A-Za-z]+ \d{1,2}, \d{4})", JobCardText)

        if match:
            job_creation_date_str = match.group(1)
            logging.info(f"Extracted Job Creation Date: {job_creation_date_str}")

            # Convert the extracted date string into a datetime object and focus only on the date
            job_creation_date = datetime.strptime(job_creation_date_str, "%B %d, %Y").date()  # Convert to date only

            # Assert that the job creation date is within the last week range (dates only, ignoring time)
            assert_that(job_creation_date).is_between(last_week_start, last_week_end)
        else:
            logging.error("No date found in JobCardText!")
            assert False, "Job creation date not found in JobCardText."



@pytest.mark.regression
@pytest.mark.jobs_page_last2weeksjobsfilter
def test_jobs_page_last2weeksjobsfilter(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.sortby.click()
    jobs_page.last2week.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    elements =  jobs_page.job_creation_date.find_elements()

    current_date = datetime.now().date()  # Get the current date (ignoring time)
    last_2_weeks_start = current_date - timedelta(weeks=2)
    last_2_weeks_end = current_date - timedelta(days=0)  # Yesterday (ignoring time)

    logging.info(
        f"Last 2 weeks date range: {last_2_weeks_start.strftime('%B %d, %Y')} to {last_2_weeks_end.strftime('%B %d, %Y')}")

    # Loop through each element and validate the job creation date
    for element in elements:
        JobCardText = element.text
        logging.info(f"Job card text: {JobCardText}")

        # Match the date in the format "Created on Month Day, Year"
        match = re.search(r"Created on\s*([A-Za-z]+ \d{1,2}, \d{4})", JobCardText)

        if match:
            job_creation_date_str = match.group(1)
            logging.info(f"Extracted Job Creation Date: {job_creation_date_str}")

            # Convert the extracted date string into a datetime object and focus only on the date
            job_creation_date = datetime.strptime(job_creation_date_str, "%B %d, %Y").date()  # Convert to date only

            # Assert that the job creation date is within the last 2 weeks range (dates only, ignoring time)
            assert_that(job_creation_date).is_between(last_2_weeks_start, last_2_weeks_end)
        else:
            logging.error("No date found in JobCardText!")
            assert False, "Job creation date not found in JobCardText."


@pytest.mark.regression
@pytest.mark.jobs_page_lastmonthjobsfilter
def test_jobs_page_lastmonthjobsfilter(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.sortby.click()
    jobs_page.last_month.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    elements =  jobs_page.job_creation_date.find_elements()

    current_date = datetime.now().date()  # Get the current date (ignoring time)
    last_month_start = current_date - timedelta(days=30)  # 30 days ago from the current date
    last_month_end = current_date  # Current date

    logging.info(
        f"Last month date range (from current date): {last_month_start.strftime('%B %d, %Y')} to {last_month_end.strftime('%B %d, %Y')}")

    # Loop through each element and validate the job creation date
    for element in elements:
        JobCardText = element.text
        logging.info(f"Job card text: {JobCardText}")

        # Match the date in the format "Created on Month Day, Year"
        match = re.search(r"Created on\s*([A-Za-z]+ \d{1,2}, \d{4})", JobCardText)

        if match:
            job_creation_date_str = match.group(1)
            logging.info(f"Extracted Job Creation Date: {job_creation_date_str}")

            # Convert the extracted date string into a datetime object and focus only on the date
            job_creation_date = datetime.strptime(job_creation_date_str, "%B %d, %Y").date()

            # Assert that the job creation date is within the last month range (from current date to 30 days ago)
            assert_that(job_creation_date).is_between(last_month_start, last_month_end)
        else:
            logging.error("No date found in JobCardText!")
            assert False, "Job creation date not found in JobCardText."


@pytest.mark.regression
@pytest.mark.jobs_page_last3monthsjobsfilter
def test_jobs_page_last3monthsjobsfilter(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.sortby.click()
    jobs_page.last_3_months.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    elements =  jobs_page.job_creation_date.find_elements()

    current_date = datetime.now().date()  # Get the current date (ignoring time)
    last_3_months_start = current_date - timedelta(days=90)  # 90 days ago from the current date
    last_3_months_end = current_date  # Current date

    logging.info(
        f"Last 3 months date range (from current date): {last_3_months_start.strftime('%B %d, %Y')} to {last_3_months_end.strftime('%B %d, %Y')}")

    # Loop through each element and validate the job creation date
    for element in elements:
        JobCardText = element.text
        logging.info(f"Job card text: {JobCardText}")

        # Match the date in the format "Created on Month Day, Year"
        match = re.search(r"Created on\s*([A-Za-z]+ \d{1,2}, \d{4})", JobCardText)

        if match:
            job_creation_date_str = match.group(1)
            logging.info(f"Extracted Job Creation Date: {job_creation_date_str}")

            # Convert the extracted date string into a datetime object and focus only on the date
            job_creation_date = datetime.strptime(job_creation_date_str, "%B %d, %Y").date()

            # Assert that the job creation date is within the last 3 months range (from current date to 90 days ago)
            assert_that(job_creation_date).is_between(last_3_months_start, last_3_months_end)
        else:
            logging.error("No date found in JobCardText!")
            assert False, "Job creation date not found in JobCardText."

@pytest.mark.regression
@pytest.mark.jobs_page_last6monthsjobsfilter
def test_jobs_page_last6monthsjobsfilter(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.sortby.click()
    jobs_page.last_6_months.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    elements =  jobs_page.job_creation_date.find_elements()

    current_date = datetime.now().date()  # Get the current date (ignoring time)
    last_6_months_start = current_date - timedelta(days=180)  # 180 days ago from the current date
    last_6_months_end = current_date  # Current date

    logging.info(
        f"Last 6 months date range (from current date): {last_6_months_start.strftime('%B %d, %Y')} to {last_6_months_end.strftime('%B %d, %Y')}")

    # Loop through each element and validate the job creation date
    for element in elements:
        JobCardText = element.text
        logging.info(f"Job card text: {JobCardText}")

        # Match the date in the format "Created on Month Day, Year"
        match = re.search(r"Created on\s*([A-Za-z]+ \d{1,2}, \d{4})", JobCardText)

        if match:
            job_creation_date_str = match.group(1)
            logging.info(f"Extracted Job Creation Date: {job_creation_date_str}")

            # Convert the extracted date string into a datetime object and focus only on the date
            job_creation_date = datetime.strptime(job_creation_date_str, "%B %d, %Y").date()

            # Assert that the job creation date is within the last 6 months range (from current date to 180 days ago)
            assert_that(job_creation_date).is_between(last_6_months_start, last_6_months_end)
        else:
            logging.error("No date found in JobCardText!")
            assert False, "Job creation date not found in JobCardText."


@pytest.mark.regression
@pytest.mark.jobs_page_lastyearjobsfilter
def test_jobs_page_lastyearfilter(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs button clicked")
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.sortby.click()
    jobs_page.last_year.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    elements =  jobs_page.job_creation_date.find_elements()

    current_date = datetime.now().date()  # Get the current date (ignoring time)
    last_year_start = current_date - timedelta(days=365)  # 365 days ago from the current date
    last_year_end = current_date  # Current date

    logging.info(
        f"Last year date range (from current date): {last_year_start.strftime('%B %d, %Y')} to {last_year_end.strftime('%B %d, %Y')}")

    # Loop through each element and validate the job creation date
    for element in elements:
        JobCardText = element.text
        logging.info(f"Job card text: {JobCardText}")

        # Match the date in the format "Created on Month Day, Year"
        match = re.search(r"Created on\s*([A-Za-z]+ \d{1,2}, \d{4})", JobCardText)

        if match:
            job_creation_date_str = match.group(1)
            logging.info(f"Extracted Job Creation Date: {job_creation_date_str}")

            # Convert the extracted date string into a datetime object and focus only on the date
            job_creation_date = datetime.strptime(job_creation_date_str, "%B %d, %Y").date()

            # Assert that the job creation date is within the last year range (from current date to 365 days ago)
            assert_that(job_creation_date).is_between(last_year_start, last_year_end)
        else:
            logging.error("No date found in JobCardText!")
            assert False, "Job creation date not found in JobCardText."


@pytest.mark.regression
@pytest.mark.jobs_page_search_functionality
def test_jobs_page_search_functionality(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    jobs_page.search_tab.click()
    logging.info(f"search tab clicked")
    jobs_page.search_tab.send_keys('TEST')
    searchedjobs =jobs_page.jobs_card.find_elements()

    for searchedjob in searchedjobs:
        SearchedJobText = searchedjob.text
        logging.info(f"Searched Job text: {SearchedJobText}")
        assert_that(SearchedJobText).contains('TEST')



@pytest.mark.regression
@pytest.mark.jobs_page_search_with_spaces
def test_jobs_page_search_with_spaces(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    jobs_page.search_tab.click()
    logging.info(f"search tab clicked")
    jobs_page.search_tab.send_keys('   TEST      ')
    searchedjobs =jobs_page.jobs_card.find_elements()

    for searchedjob in searchedjobs:
        SearchedJobText = searchedjob.text
        logging.info(f"Searched Job text: {SearchedJobText}")
        assert_that(SearchedJobText).contains('TEST')


@pytest.mark.regression
@pytest.mark.jobs_page_search_with_partial_text
def test_jobs_page_search_with_partial_text(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    jobs_page.search_tab.click()
    logging.info(f"search tab clicked")
    jobs_page.search_tab.send_keys('PSY')
    searchedjobs =jobs_page.jobs_card.find_elements()

    for searchedjob in searchedjobs:
        SearchedJobText = searchedjob.text
        logging.info(f"Searched Job text: {SearchedJobText}")
        assert_that(SearchedJobText).contains('PSY')


@pytest.mark.regression
@pytest.mark.jobs_page_clear_search
def test_jobs_page_clear_search(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    #login = authenticated_user_recruiter
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    jobs_page.search_tab.click()
    logging.info(f"search tab clicked")
    jobs_page.search_tab.send_keys('TEST')
    jobs_page.clear_search.click()
    assert_that(jobs_page.search_tab.get_attribute('value')).is_empty()


@pytest.mark.regression
@pytest.mark.jobs_page_see_details
def test_jobs_page_see_details(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.details_btn.click()
    assert_that(jobs_page.description.is_element_visible()).is_true()
    assert_that(jobs_page.details.is_element_visible()).is_true()


@pytest.mark.regression
@pytest.mark.jobs_page_see_details_candidates
def test_jobs_page_see_details_candidates(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.details_btn.click()
    assert_that(jobs_page.description.is_element_visible()).is_true()
    assert_that(jobs_page.details.is_element_visible()).is_true()
    jobs_page.candidates_btn.click()
    assert_that(jobs_page.candidates_count.is_element_visible()).is_true()
    count = jobs_page.candidates_count.get_text().strip()
    logging.info(count)

    candidatecount = int(''.join(filter(str.isdigit, count)))
    logging.info(candidatecount)
    assert_that(candidatecount).is_greater_than_or_equal_to(0)

    


@pytest.mark.regression
@pytest.mark.jobs_page_see_details_settings
def test_jobs_page_see_details_candidates(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.drafts_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.details_btn.click()
    jobs_page.Settings_btn.click()

    jobs_page.basic_in_seedeatils.click()
    assert_that(jobs_page.unpublish_after_in_seedeatils.is_element_visible()).is_true()

    jobs_page.job_workflow_in_seedeatils.click()
    assert_that(jobs_page.followcompanyworkflow.is_element_visible()).is_true()

    jobs_page.proctoring_in_seedeatils.click()
    assert_that(jobs_page.proctoring_option.is_element_visible()).is_true()

    jobs_page.cutoff_in_seedeatils.click()
    assert_that(jobs_page.weightage.is_element_visible()).is_true()

    jobs_page.applicationform_in_seedeatils.click()
    assert_that(jobs_page.fieldname.is_element_visible()).is_true()

    jobs_page.language_in_seedeatils.click()
    assert_that(jobs_page.language_heading.is_element_visible()).is_true()

    jobs_page.Save_btn.click()

@pytest.mark.regression
@pytest.mark.jobs_page_see_details_edit_job
def test_jobs_page_see_details_edit_job(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.details_btn.click()
    jobs_page.editjob.click()
    assert_that(jobs_page.editjob_popbox.is_element_visible()).is_true()


@pytest.mark.regression
@pytest.mark.jobs_page_unpublish_job
def test_jobs_page_unpublish_job(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.job_card_ellipsis.double_click()
    logging.info("ellipsis clicked")
    jobs_page.unpublishjob.click()
    assert_that(jobs_page.job_update_popup.is_element_visible()).is_true()
    text = jobs_page.job_update_popup.get_text()
    logging.info(text)
    assert_that(text).contains('Job updated successfully')


@pytest.mark.regression
@pytest.mark.jobs_page_markjob_private
def test_jobs_page_markjob_private(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.job_card_ellipsis.double_click()
    logging.info("ellipsis clicked")
    jobs_page.markjobprivate.click()
    assert_that(jobs_page.job_update_popup.is_element_visible()).is_true()
    text = jobs_page.job_update_popup.get_text()
    logging.info(text)
    assert_that(text).contains('Job updated successfully')


@pytest.mark.regression
@pytest.mark.jobs_page_markjob_public
def test_jobs_page_markjob_public(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.job_card_ellipsis.double_click()
    logging.info("ellipsis clicked")
    jobs_page.markjobpublic.click()
    assert_that(jobs_page.job_update_popup.is_element_visible()).is_true()
    text = jobs_page.job_update_popup.get_text()
    logging.info(text)
    assert_that(text).contains('Job updated successfully')


@pytest.mark.regression
@pytest.mark.jobs_page_duplicate_job
def test_jobs_page_duplicate_job(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.job_card_ellipsis.double_click()
    logging.info("ellipsis clicked")
    jobs_page.duplicatejob.click()
    assert_that(jobs_page.duplicatejob_popup.is_element_visible()).is_true()

@pytest.mark.regression
@pytest.mark.jobs_page_delete_job
def test_jobs_page_delete_job(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.job_card_ellipsis.double_click()
    logging.info("ellipsis clicked")
    jobs_page.deletejob.click()
    assert_that(jobs_page.deletejob_popup.is_element_visible()).is_true()

@pytest.mark.regression
@pytest.mark.jobs_page_publish_job
def test_jobs_page_publish_job(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    logging.info(f"logged in")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)"))
    )
    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.drafts_btn.click()
    assert_that(jobs_page.jobs_card.is_element_visible()).is_true()
    jobs_page.job_card_ellipsis.double_click()
    jobs_page.publishjob.click()
    assert_that(jobs_page.job_update_popup.is_element_visible()).is_true()
    text = jobs_page.job_update_popup.get_text()
    logging.info(text)
    assert_that(text).contains('Job updated successfully')

