import logging
import time
from asyncio import wait_for
from datetime import datetime
from http.client import responses
from assertpy import assert_that, soft_assertions
import pytest
from selenium.webdriver.common.devtools.v85.network import Response
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver, env
from Page_Recruiter.login import Loginrecruiter

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")

#TC01
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.valid_Launch_Recruiter
def test_valid_Launch_Recruiter(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    recruiterpage = Loginrecruiter(driver)
    response =  recruiterpage.recruiter_page.get_text()
    assert_that("Welcome, Recruiter").is_equal_to(response)
    logging.info(f"Recruiter Page loaded : {response}")

#TC02
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.valid_login_recruiter
def test_valid_login_recruiter(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.username_btn.send_keys('inderjeetkmcs@gmail.com')
    recruiterlogin.password_btn.send_keys('123')
    recruiterlogin.login_btn.click()
    response = recruiterlogin.login_successful.get_text()
    #assert "Login successful" in response, f"Expected 'Login Successful', but got: {response}"
    assert_that("Login successful").is_equal_to(response)
    logging.info(f"LOGIN SUCCESSFUL : {response}")

#TC03
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.invalid_password_login_recruiter
def test_invalid_password_login_recruiter(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.username_btn.send_keys('inderjeetkmcs@gmail.com')
    recruiterlogin.password_btn.send_keys('xyz')
    recruiterlogin.login_btn.click()
    response = recruiterlogin.login_unsuccessful.get_text()
    assert_that("Invalid email ID or password").is_equal_to(response)
    logging.info(f"LOGIN UNSUCCESSFUL : {response}")

#TC04
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.invalid_email_login_recruiter
def test_invalid_email_login_recruiter(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.username_btn.send_keys('invalid@gmail.com')
    recruiterlogin.password_btn.send_keys('123')
    recruiterlogin.login_btn.click()
    response = recruiterlogin.error_occured.get_text()
    #assert "Some error occurred. Please try again later" in response, f"Expected 'Some error occurred. Please try again later', but got: {response}"
    assert_that("Some error occurred. Please try again later").is_equal_to(response)
    logging.info(f"LOGIN UNSUCCESSFUL : {response}")


#TC05
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.invalid_email_password_recruiter
def test_invalid_email_password_recruiter(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.username_btn.send_keys('invalid@gmail.com')
    recruiterlogin.password_btn.send_keys('invalid 123')
    recruiterlogin.login_btn.click()
    response = recruiterlogin.error_occured.get_text()
    #assert "Some error occurred. Please try again later" in response, f"Expected 'Some error occurred. Please try again later', but got: {response}"
    assert_that("Some error occurred. Please try again later").is_equal_to(response)
    logging.info(f"LOGIN UNSUCCESSFUL : {response}")

#TC06
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.empty_password_login_recruiter
def test_empty_password_login_recruiter(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.username_btn.send_keys('invalid@gmail.com')
    recruiterlogin.password_btn.send_keys('')
    recruiterlogin.login_btn.click()
    response = recruiterlogin.password_required.get_text()
    #assert "Password is required" in response, f"Expected 'Password is required', but got: {response}"
    assert_that("Password is required").is_equal_to(response)
    logging.info(f"Password Required : {response}")

#TC07
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.empty_email_login_recruiter
def test_empty_email_login_recruiter(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.username_btn.send_keys('')
    recruiterlogin.password_btn.send_keys('123')
    recruiterlogin.login_btn.click()
    response = recruiterlogin.email_required.get_text()
    assert_that("Email is required").is_equal_to(response)
    logging.info(f"Email Required : {response}")

#TC08
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.empty_emailandpassword_login_recruiter
def test_empty_emailandpassword_login_recruiter(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.username_btn.send_keys('')
    recruiterlogin.password_btn.send_keys('')
    recruiterlogin.login_btn.click()
    response_email = recruiterlogin.email_required.get_text()
    response_password = recruiterlogin.password_required.get_text()
    # Assertions for both email and password fields
    with soft_assertions():
      assert_that("Password is required").is_equal_to(response_password)
      assert_that("Email is required").is_equal_to(response_password)
    logging.info(f"Email Required : {response_email} , {response_password}")

#TC09
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.view_password_login_recruiter
def test_view_password_login_recruiter(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.username_btn.send_keys('')
    recruiterlogin.password_btn.send_keys('123')
    recruiterlogin.login_btn.click()
    recruiterlogin.hide_view_password_btn.click()
    logging.info(f"Hide/view password button clicked")

#TC10
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.login_trouble_signing
def test_login_trouble_signing(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    recruiterlogin.troublesigning_btn.click()
    response = recruiterlogin.forgotten_password_page.get_text()
    #assert "Please provide your functional email address, we’ll send you the reset link." in response, f"Expected 'Please provide your functional email address, we’ll send you the reset link.', but got: {response}"
    assert_that("Please provide your functional email address, we’ll send you the reset link.").is_equal_to(response)
    logging.info(f"Forgotten Password Page Loaded : {response}")



#TC11
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.login_contact_us
def test_login_contact_us(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    original_window = driver.current_window_handle

    recruiterlogin.contactus_btn.click()
    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    # Switch to the new tab
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break
    response = recruiterlogin.contactus_page.get_text()
    # assert 'Contact Us' in response, f"Contact Us', but got: {response}"
    assert_that("Contact Us").is_equal_to(response)
    logging.info(f"Contact Us Page Loaded : {response}")



#TC12
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.login_page_facebooklinks
def test_login_page_facebooklinks(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    original_window = driver.current_window_handle

    recruiterlogin.social_media_facebook_btn.click()
    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    # Switch to the new tab
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    current_url = driver.current_url
    expected_url = "https://www.facebook.com/people/Ambition-Hire/61552755518622/"
    assert_that(current_url).is_equal_to(expected_url)
    response = recruiterlogin.facebook_page.get_text()
    assert 'See more from Ambition Hire' in response, f"See more from Ambition Hire', but got: {response}"
    logging.info(f"Facebook Page Loaded : {response}")


#TC13
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.login_page_instagramlinks
def test_login_page_instagramlinks(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    original_window = driver.current_window_handle

    recruiterlogin.social_media_instagram_btn.click()
    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    # Switch to the new tab
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break
    response = recruiterlogin.instagram_page.get_text()
    # assert 'Sign up for Instagram' in response, f"Sign Up for Instagram', but got: {response}"
    assert_that('Sign up for Instagram').is_equal_to(response)
    logging.info(f"Instagram Page Loaded : {response}")


#TC14
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.login_page_linkedinlinks
def test_login_page_linkedinlinks(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    original_window = driver.current_window_handle

    recruiterlogin.social_media_linkedin_btn.click()
    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    # Switch to the new tab
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break
    response = recruiterlogin.linkedin_page.get_text()
    # assert 'Sign in' in response, f"Sign in', but got: {response}"
    assert_that("Sign in").is_equal_to(response)
    logging.info(f"LinkedIn Page Loaded : {response}")

#TC15
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.login_page_aboutus_page
def test_login_page_aboutus_page(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    original_window = driver.current_window_handle
    recruiterlogin.aboutuspage_btn.click()
    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    # Switch to the new tab
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break
    response = recruiterlogin.aboutus_page.get_text()
    assert_that("Get to know about us").is_equal_to(response)
    logging.info(f"About Us Page loaded : {response}")

#TC16
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.login_page_pricing_btn
def test_login_page_pricing_btn(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    original_window = driver.current_window_handle
    recruiterlogin.pricing_page_btn.click()
    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    # Switch to the new tab
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break
    response = recruiterlogin.pricing_page.get_text()
    assert_that("Unleash the Power of Ambition Hire for the Cost of a Burger!").is_equal_to(response)
    logging.info(f"Pricing Page loaded : {response}")

#TC17
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.login_page_demo_btn
def test_login_page_demo_btn(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    original_window = driver.current_window_handle
    recruiterlogin.demo_icon_btn.click()
    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    # Switch to the new tab
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break
    response = recruiterlogin.demo_page.get_text()
    assert_that("Take a Quick Demo").is_equal_to(response)
    logging.info(f"Demo Page loaded : {response}")

#TC18
@pytest.mark.regression
@pytest.mark.regression_recruiter_loginpage
@pytest.mark.login_globe_btn
def test_login_globe_btn(env, driver, recruiter_user):
    logging.info(f"environment -> {env}")
    login = recruiter_user
    recruiterlogin = Loginrecruiter(driver)
    original_window = driver.current_window_handle
    recruiterlogin.globe_icon_btn.click()
    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    # Switch to the new tab
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    current_url = driver.current_url
    expected_url = "https://www.ambitionhire.ai/"
    assert_that(current_url).is_equal_to(expected_url)
    logging.info(f"Current Url{current_url} : {expected_url}")

    response = recruiterlogin.ambitionhire_page.get_text()
    assert_that("Effortless Assessments with Unlimited Possibilities for Your Business").is_equal_to(response)
    logging.info(f"Ambition Hire Page loaded : {response}")

















