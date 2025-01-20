import logging
import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
# from pynput.keyboard import  Key,Controller

from Pages_Candidate.Userprofile import Userprofile
from conftest import driver, env
from Pages_Candidate.login import Login
import pyautogui

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime =     datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


@pytest.mark.userprofile
def test_userprofile(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(2)
    userinfo.profileicon_btn.click()
    time.sleep(1)


@pytest.mark.clickandsaveimage
def test_clickandsaveimage(env, authenticated_user, driver):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(2)
    userinfo.profileicon_btn.click()
    time.sleep(1)
    userinfo.selectingprofileicon_btn.click()
    time.sleep(5)
    userinfo.clickprofileimage_btn.click()
    time.sleep(5)
    userinfo.takephoto_btn.click()
    time.sleep(5)
    userinfo.savephoto_btn.click()
    userinfo.savechanges_btn.click()
    time.sleep(5)


@pytest.mark.clickdownoadandsaveimage
def test_clickdownoadandsaveimage(env, authenticated_user, driver):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    userinfo.explorepage_btn.click()
    time.sleep(5)
    userinfo.profileicon_btn.click()
    time.sleep(1)
    userinfo.selectingprofileicon_btn.click()
    time.sleep(5)
    userinfo.clickprofileimage_btn.click()
    time.sleep(5)
    userinfo.takephoto_btn.click()
    time.sleep(5)
    userinfo.downlaodimage_btn.click()
    driver.implicitly_wait(2)
    userinfo.savephoto_btn.click()
    userinfo.savechanges_btn.click()
    time.sleep(5)


@pytest.mark.uploadimagefromdevice
def test_uploadimagefromdevice(env, authenticated_user, driver):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(2)
    userinfo.profileicon_btn.click()
    time.sleep(5)
    userinfo.selectingprofileicon_btn.click()
    time.sleep(5)
    userinfo.uploadimagefromdesktop_btn.click()
    time.sleep(2)
    my_image_path = r'Downloads\imagetest'
    pyautogui.write(my_image_path)
    pyautogui.press("enter")
    time.sleep(5)
    userinfo.savechanges_btn.click()
    time.sleep(5)


@pytest.mark.changeaddress
def test_changeaddress(env, authenticated_user, driver):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(2)
    userinfo.profileicon_btn.click()
    time.sleep(5)
    userinfo.selectingprofileicon_btn.click()
    time.sleep(5)
    userinfo.edit_btn.click()
    userinfo.edit_address_btn.send_keys("123 MG Road, Bengaluru, Karnataka, India")
    userinfo.saveaddress_btn.click()
    time.sleep(3)


@pytest.mark.updatequalificationdetails
def test_updatequalificationdetails(env, authenticated_user, driver):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(2)
    userinfo.profileicon_btn.click()
    time.sleep(5)
    userinfo.selectingprofileicon_btn.click()
    time.sleep(5)
    userinfo.edit_btn_qualification.click()
    userinfo.qualification_btn.send_keys('High School')
    # userinfo.selectingprofileicon_btn.click()
    userinfo.select_course_btn.send_keys('Computer Science ')
    userinfo.select_educationplace_btn.send_keys('Indian Institute of Technology, Delhi ')
    userinfo.select_percentage_btn.send_keys('8.7')
    userinfo.select_passingyear_btn.send_keys('2022')
    userinfo.save_qualification_details_btn.click()


@pytest.mark.updateguardian_details
def test_updateguardian_details(env, authenticated_user, driver):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(2)
    userinfo.profileicon_btn.click()
    time.sleep(5)
    userinfo.selectingprofileicon_btn.click()
    time.sleep(5)
    userinfo.edit_btn_guardian.click()
    userinfo.add_guardian_btn.click()
    time.sleep(5)
    userinfo.add_guardian_name_btn.send_keys('Rahul Sharma ')
    userinfo.add_guardian_mobileno_btn.send_keys('9876543210')
    userinfo.add_guardian_relation_btn.send_keys('Father')
    userinfo.add_guardian_btn.click()
    userinfo.add_2ndguardian_name_btn.send_keys('reena sharma')
    userinfo.add_guardian_mobileno2_btn.send_keys('8768543217')
    userinfo.add_2ndguardian_relation_btn.send_keys('Mother')
    time.sleep(2)
    userinfo.save_guardian_details_btn.click()


@pytest.mark.deleteguardian_details
def test_deleteguardian_details(env, authenticated_user, driver):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(2)
    userinfo.profileicon_btn.click()
    time.sleep(5)
    userinfo.selectingprofileicon_btn.click()
    time.sleep(5)
    userinfo.edit_btn_guardian.click()
    userinfo.add_guardian_btn.click()
    time.sleep(5)
    userinfo.add_guardian_name_btn.send_keys('Rahul Sharma ')
    userinfo.add_guardian_mobileno_btn.send_keys('9876543210')
    userinfo.add_guardian_relation_btn.send_keys('Father')
    userinfo.delete_guardian_details_btn.click()
    time.sleep(2)
    userinfo.save_guardian_details_btn.click()


@pytest.mark.uploadcertificatefromdevice
def test_uploadcertificatefromdevice(env, authenticated_user, driver):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(2)
    userinfo.profileicon_btn.click()
    time.sleep(5)
    userinfo.selectingprofileicon_btn.click()
    time.sleep(5)
    userinfo.edit_certifiaction_btn.click()
    time.sleep(5)
    userinfo.add_certifiaction_btn.move_to_element()
    time.sleep(10)
    userinfo.add_certifiaction_name_btn.send_keys('AWS')
    # userinfo.add_certifiaction_number_btn.send_keys(' AWS-123456 ')
    # userinfo.choose_certificate_from_device_btn.click()
    # my_image_path = r'Downloads\sdet_test'
    # pyautogui.write(my_image_path)
    # pyautogui.press("enter")
    # time.sleep(5)


@pytest.mark.uploadresumefromdevice
def test_uploadresumefromdevice(env, authenticated_user, driver):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(2)
    userinfo.profileicon_btn.click()
    time.sleep(5)
    userinfo.selectingprofileicon_btn.click()
    time.sleep(5)
    userinfo.edit_resume_btn.click()
    time.sleep(5)
    userinfo.choose_Resume_from_device_btn.click()
    time.sleep(2)
    my_image_path = r'Downloads\Resumetest'
    pyautogui.write(my_image_path)
    pyautogui.press("enter")
    time.sleep(5)
    userinfo.save_resume_btn.click()
    time.sleep(5)


@pytest.mark.viewuploadedresume
def test_viewuploadedresume(env, authenticated_user, driver):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    userinfo = Userprofile(driver)
    Pagelogin = Login(driver)
    # Pagelogin.login_btn.click()
    # # driver.implicitly_wait(2)
    # time.sleep(3)
    # # Pagelogin.name_btn.send_keys('Mridul')
    Pagelogin.phonenumber_btn.send_keys('7503078450')
    Pagelogin.sendotp_btn.click()
    time.sleep(5)
    Pagelogin.Sendingotp_text.send_keys('000000')
    Pagelogin.submitotp_btn.click()
    time.sleep(2)
    userinfo.profileicon_btn.click()
    time.sleep(5)
    userinfo.selectingprofileicon_btn.click()
    time.sleep(5)
    userinfo.edit_resume_btn.click()
    time.sleep(5)
    userinfo.choose_Resume_from_device_btn.click()
    time.sleep(2)
    my_image_path = r'Downloads\Resumetest'
    pyautogui.write(my_image_path)
    pyautogui.press("enter")
    time.sleep(4)
    userinfo.save_resume_btn.click()
    time.sleep(4)
    userinfo.view_resume_btn.click()
    time.sleep(2)

