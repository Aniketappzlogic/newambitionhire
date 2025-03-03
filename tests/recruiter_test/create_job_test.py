import logging
import time
from asyncio import wait_for
from datetime import datetime
import pytest
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


@pytest.mark.regression
@pytest.mark.create_job
def test_create_jobs(env, driver, authenticated_user_recruiter):
    logging.info(f"environment -> {env}")
    login = authenticated_user_recruiter
    logging.info(f"Password entered")

    # recruiter_login.hidepassword_btn.click()
    # logging.info(f"hide passwrd btn clicked")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Login')]"))
    )
    #recruiter_login.login_btn.click()
    logging.info(f"login btn clicked")
    #time.sleep(5)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//h2[text()='Private Jobs'])"))
    )

    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs btn clicked")
    time.sleep(2)


    # activebtn = Jobs(driver)
    # activebtn.active_btn.click()
    # logging.info(f"active btn clicked")
    #
    # draftsbtn = Jobs(driver)
    # draftsbtn.drafts_btn.click()
    #
    # inactivebtn = Jobs(driver)
    # inactivebtn.inactive_btn.click()
    # logging.info(f"inactive btn clicked")
    #
    # sortby_btn = Jobs(driver)
    # sortby_btn.Sortby.click()
    #
    # last2week = Jobs(driver)
    # last2week.last2week.click()
    #
    # searchtab = Jobs(driver)
    # searchtab.search_tab.send_keys('3rd July Testing')
    #
    # detailsbtn = Jobs(driver)
    # detailsbtn.details_btn.click()
    #
    # candidatesbtn = Jobs(driver)
    # candidatesbtn.candidates_btn.click()
    # logging.info(f"candidate btn clicked")
    # #---------------------------------------------
    #
    #
    # # WebDriverWait(driver, 3).until(
    # #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-0"))
    # # )
    # # candidatecheckbox = Jobs(driver)
    # # candidatecheckbox.candidates_checkbox.click()
    # #-------------------------------------------------
    #
    # Settings = Jobs(driver)
    # Settings.Settings_btn.click()
    #
    # jobworkflow = Jobs(driver)
    # jobworkflow.Job_Workflow_btn.click()
    #
    # Proctoringbtn = Jobs(driver)
    # Proctoringbtn.Proctoring_btn.click()
    #
    # Cut_off = Jobs(driver)
    # Cut_off.Cutoff.click()
    #
    # Applicationform = Jobs(driver)
    # Applicationform.Application_Form.click()
    #
    # Languagebtn = Jobs(driver)
    # Languagebtn.Language_btn.click()
    # logging.info(f"Lang btn Created")
    #
    # Savebtn = Jobs(driver)
    # Savebtn.Save_btn.click()
    # logging.info(f"save btn clicked")
    #
    #
    # jobs_page = Jobs(driver)
    # jobs_page.jobs_btn.click()


#CREATE JOB
# def test_create_job(env, driver, authenticated_user):
#     logging.info(f"environment -> {env}")
#     login = authenticated_user
#     recruiter_login = Loginrecruiter(driver)
#     recruiter_login.username_btn.send_keys('inderjeetkmcs@gmail.com')
#     recruiter_login.password_btn.send_keys('123')
#     logging.info(f"Password entered")
#
#         # recruiter_login.hidepassword_btn.click()
#         # logging.info(f"hide passwrd btn clicked")
#
#     WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Login')]"))
#         )
#     recruiter_login.login_btn.click()
#     logging.info(f"login btn clicked")
#         # time.sleep(5)
#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "(//h2[text()='Private Jobs'])"))
#         )

    jobs_page = Jobs(driver)
    jobs_page.jobs_btn.click()
    logging.info(f"jobs btn clicked")
    time.sleep(2)

    createjob = Jobs(driver)
    createjob.Create_Job.click()
    logging.info(f"create job Clicked")

    jobtitle = Jobs(driver)
    jobtitle.Job_Title.send_keys('Fun bug III 0303')

    notificationtitle = Jobs(driver)
    notificationtitle.Notification_Title.send_keys("Automated")

    JobDescription = Jobs(driver)
    JobDescription.Job_Description.send_keys('automated')

    department = Jobs(driver)
    department.Department.click()
    department.Department_selector.click()

    industry = Jobs(driver)
    industry.Industry.click()
    industry.Industry_selector.click()

    Employmenttype = Jobs(driver)
    Employmenttype.Employment_Type.click()
    Employmenttype.Employmenttype_selector.click()

    WorkplaceType = Jobs(driver)
    WorkplaceType.Workplace_Type.click()
    WorkplaceType.Workplace_Type_Selector.click()

    WorkExperience = Jobs(driver)
    WorkExperience.Work_Experience.click()
    WorkExperience.Workplace_Experience_Selector.click()

    location = Jobs(driver)
    location.Location.send_keys('Gurgao')
    location.Location_selector.click()

    MinSalary = Jobs(driver)
    MinSalary.Min_Salary.send_keys('0')

    MaxSalary = Jobs(driver)
    MaxSalary.Max_Salary.send_keys('0')

    #NEXT SECTION
    Nextbtn = Jobs(driver)
    Nextbtn.Next_btn.click()

    #Basic Settings

    EmailNotification = Jobs(driver)
    EmailNotification.Email_Notification.click()

    WhatsappNotification = Jobs(driver)
    WhatsappNotification.Whatsapp_Notification.click()

    AssessmentCompletion = Jobs(driver)
    AssessmentCompletion.Assessment_Completion_toggle.click()

    OneSitting = Jobs(driver)
    OneSitting.OneSitting_toggle.click()

    Nextbutn = Jobs(driver)
    Nextbutn.Next_butn.click()


    #JOB SETTINGS - JOB WORKFLOW PAGE

    # AssessmentToggle = Jobs(driver)
    # AssessmentToggle.Assessment_toggle.click()

    # CTQToggle = Jobs(driver)
    # CTQToggle.CTQ_Toggle.click()

    FunctionalToggle = Jobs(driver)
    FunctionalToggle.Functional_Toggle.click()
    #
    # EnglishToggle = Jobs(driver)
    # EnglishToggle.English_Toggle.click()

    # MultilingualToggle = Jobs(driver)
    # MultilingualToggle.Multilingual_Toggle.click()

    # PsychometricToggle = Jobs(driver)
    # PsychometricToggle.Psychometric_Toggle.click()
    #
    # AlgoriseToggle = Jobs(driver)
    # AlgoriseToggle.Algorise_Toggle.click()
    #
    # ExcelToggle = Jobs(driver)
    # ExcelToggle.Excel_Toggle.click()
    #
    # OnewayInterview = Jobs(driver)
    # OnewayInterview.OneWayInterview_Toggle.click()

    ResultToggle = Jobs(driver)
    ResultToggle.Result_Toggle.click()

    Nexxt = Jobs(driver)
    Nexxt.Next_btn_to_Proctoring.click()
    time.sleep(2)

    #PROCTORING PAGE
    # ProctoringToggle = Jobs(driver)
    # ProctoringToggle.Proctoring_Toggle.click()       #COMMENT IT OUT IF you WANT PROCTORING TO BE DISABLED

    # AntiCheatToggle = Jobs(driver)
    # AntiCheatToggle.AntiCheat_Toggle.click()

    NextToCutoff = Jobs(driver)
    NextToCutoff.Next_to_Cutoff.click()
    time.sleep(2)


    #NEXT TO LANGUAGE
    NextToLang = Jobs(driver)
    NextToLang.Next_to_Lang.click()
    logging.info(f"next to lang Clicked")
    time.sleep(2)

    HindiLanguage = Jobs(driver)                   #COMMENT THIS IF YOU DON'T WANT TO ADD HINDI LANGUAGE
    HindiLanguage.Hindi_Lang.click()


    NextToAppForm = Jobs(driver)
    NextToAppForm.Next_to_AppForm.click()
    logging.info(f"app form Clicked")
    time.sleep(2)

    SaveDraft = Jobs(driver)
    SaveDraft.Save_Draft.click()
    logging.info(f"Job Created")

    # JobSavedPopUp = Jobs(driver)
    # popuptext = JobSavedPopUp.Job_Saved_Popup.get_text()
    # print(popuptext)
    #
    # try:
    #     assert popuptext == "Job Saved in Drafts Successfully!"
    #     print("Assertion passed: The text matches the expected value.")
    # except AssertionError:
    #     print(f"Assertion failed: Expected 'Job Saved in Drafts Successfully!', but got '{popuptext}'")




    # inactivebtn = Jobs(driver)
    # inactivebtn.inactive_btn.click()
    # logging.info(f"inactive btn clicked")
    #
    # searchtab = Jobs(driver)
    # searchtab.search_tab.send_keys('Automated Job')
    #
    # Options = Jobs(driver)
    # Options.Options.double_click()

    # DuplicateJob = Jobs(driver)
    # DuplicateJob.Duplicate_Job.click()



    time.sleep(5)

#Job Created and Saved as Draft













