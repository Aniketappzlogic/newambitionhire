import logging
import re
import time
from datetime import datetime
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages_Candidate.login import Login
from conftest import driver, env
from Pages_Candidate.training_module import TrainingModule

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


@pytest.mark.view_training_module
def test_view_training_module(env, driver, authenticated_user):
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
    trainingmodule = TrainingModule(driver)
    trainingmodule.training_module_tab.click()
    time.sleep(4)
    trainingmodule.select_training_module.click()
    time.sleep(5)
    trainingmodule.start_course.click()
    time.sleep(5)


@pytest.mark.start_training_module
def test_start_training_module(env, driver, authenticated_user):
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
    trainingmodule = TrainingModule(driver)
    trainingmodule.training_module_tab.click()
    time.sleep(4)
    trainingmodule.select_training_module.click()
    time.sleep(5) #stop delete below code
    trainingmodule.start_course.click()
    time.sleep(2)
    trainingmodule.playvideo.click()
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(u'\ue007').perform()  # u'\ue007' corresponds to the Enter key
    # Wait for a few seconds to see the result
    time.sleep(3)  #####not working


@pytest.mark.view_pdftraining_module
def test_view_pdftraining_module(env, driver, authenticated_user):
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
    trainingmodule = TrainingModule(driver)
    trainingmodule.training_module_tab.click()
    time.sleep(4)
    trainingmodule.select_training_module.click()
    time.sleep(5)
    trainingmodule.start_course.click()
    time.sleep(5)
    iframe=driver.find_element(By.XPATH,"//iframe[@title='Office on the web Frame']")
    driver.switch_to.frame(iframe)
    pdf_view= driver.find_element(By.XPATH,"//svg[@xmlns='http://www.w3.org/2000/svg' and @xmlns:xlink='http://www.w3.org/1999/xlink']")
    pdf_view.click()




@pytest.mark.view_pdf
def test_view_pdf(env, driver, authenticated_user):
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
    trainingmodule = TrainingModule(driver)
    trainingmodule.training_module_tab.click()
    time.sleep(4)
    trainingmodule.select_training_module.click()
    time.sleep(5)
    trainingmodule.start_course.click()
    time.sleep(5)
    trainingmodule.openpdf.click()
    time.sleep(10)




@pytest.mark.view_pdf_2
def test_view_pdf_2(env, driver, authenticated_user):
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
    trainingmodule = TrainingModule(driver)
    trainingmodule.training_module_tab.click()
    time.sleep(4)
    trainingmodule.select_training_module.click()
    time.sleep(5)
    trainingmodule.start_course.click()
    time.sleep(5)
    trainingmodule.openpdf1.click()
    time.sleep(5)
