import logging
import time
from asyncio import wait_for
from datetime import datetime
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Page_Recruiter.Candidates_page import Candidates
from Page_Recruiter.login import Loginrecruiter
from conftest import driver, env

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


@pytest.mark.regression
@pytest.mark.candidates_page
def test_candidates_page(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    recruiter_login = Loginrecruiter(driver)
    recruiter_login.username_btn.send_keys('inderjeetkmcs@gmail.com')
    recruiter_login.password_btn.send_keys('123')
    logging.info(f"Password entered")

    # recruiter_login.hidepassword_btn.click()
    # logging.info(f"hide passwrd btn clicked")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Login')]"))
    )
    recruiter_login.login_btn.click()
    logging.info(f"login btn clicked")
    #time.sleep(5)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//h2[text()='Private Jobs'])"))
    )
    candidate_page = Candidates(driver)
    candidate_page.candidates_btn.click()
    logging.info(f"candidates btn clicked")

    Sortby = Candidates(driver)
    Sortby.Sortby.click()

    Last_2week = Candidates(driver)
    Last_2week.last2week.click()

    time.sleep(3)

    Filters = Candidates(driver)
    Filters.Filters.click()

    StagesCTQ = Candidates(driver)
    StagesCTQ.Stages_CTQ.click()
    time.sleep(1)
    StagesCTQ.Stages_CTQ.click()
    logging.info(f"ctq btn clicked")

    StagesFunctional = Candidates(driver)
    StagesFunctional.Stages_Functional.click()
    time.sleep(1)
    StagesFunctional.Stages_Functional.click()
    logging.info(f"func btn clicked")

    StagesEnglish = Candidates(driver)
    StagesEnglish.Stages_English.click()
    time.sleep(1)
    StagesEnglish.Stages_English.click()
    logging.info(f"english btn clicked")

    StagesPsychometric = Candidates(driver)
    StagesPsychometric.Stages_Psychometric.click()
    time.sleep(1)
    StagesPsychometric.Stages_Psychometric.click()
    logging.info(f"candidates btn clicked")

    StagesInReview = Candidates(driver)
    StagesInReview.Stages_InReview.click()
    time.sleep(1)
    StagesInReview.Stages_InReview.click()
    logging.info(f"in-review btn clicked")

    ProctoringStatus = Candidates(driver)
    ProctoringStatus.Proctoring_status.click()

    Pass = Candidates(driver)
    Pass.Passed.click()
    time.sleep(1)
    Pass.Passed.click()

    Fail = Candidates(driver)
    Fail.Failed.click()
    time.sleep(1)
    Fail.Failed.click()

    Lastactive = Candidates(driver)
    Lastactive.Last_active.click()

    Filters = Candidates(driver)
    Filters.Filters.click()

    SearchCandidate = Candidates(driver)
    SearchCandidate.Search_Candidate.send_keys('Aniket')

    Action  = Candidates(driver)
    Action.Action_btn.click()

    DownloadScorecard = Candidates(driver)
    DownloadScorecard.Download_Scorecard.click()
    logging.info(f"in-review btn clicked")

    time.sleep(3)

    CandidatesDetail = Candidates(driver)
    CandidatesDetail.Candidate_Details.click()


    ScoreCard = Candidates(driver)
    ScoreCard.Score_Card.click()

    DetailedScorecard = Candidates(driver)
    DetailedScorecard.Detailed_Scorecard.click()

    time.sleep(5)