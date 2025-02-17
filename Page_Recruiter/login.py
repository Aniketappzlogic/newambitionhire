import time

from selenium.webdriver.common.by import By
from utils.locators import Locator
from Page_Recruiter.base_page_recruiter import BasePage
from utils.base_elements import BaseElement


class Loginrecruiter(BasePage):

    @property
    def recruiter_page(self):
        locator = Locator(by=By.XPATH, value="//h1[normalize-space()='Welcome, Recruiter']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def username_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Email']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Password']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_btn(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(), 'Login')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def hide_view_password_btn(self):
        locator = Locator(by=By.XPATH, value=".absolute.top-0.right-4.h-full.flex.items-center.cursor-pointer")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_successful(self):
        locator = Locator(by=By.XPATH, value="//p[@class='text-sm font-medium text-onbackground-color']")
        return BaseElement(driver=self.driver, locator=locator)

    #//p[normalize-space()='Invalid email ID or password']
    @property
    def login_unsuccessful(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Invalid email ID or password']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def error_occured(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Some error occurred. Please try again later.']")
        return BaseElement(driver=self.driver, locator=locator)

    #//p[normalize-space()='Password is required']

    @property
    def password_required(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Password is required']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_required(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Email is required']")
        return BaseElement(driver=self.driver, locator=locator)



    @property
    def troublesigning_btn(self):
        locator = Locator(by=By.XPATH, value="//p[@class='font-medium text-sm cursor-pointer text-ambition-fandango-color']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def forgotten_password_page(self):
        locator = Locator(by=By.XPATH, value="//p[@class='font-normal sm:font-medium text-base text-onbackground-color text-start sm:text-center w-full']")
        return BaseElement(driver=self.driver, locator=locator)



    @property
    def recoverpassword_email(self):
        locator = Locator(by=By.XPATH,value="//input[@placeholder='Email']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sendlink_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Email']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def contactus_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Contact Us.')])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def contactus_page(self):
        locator = Locator(by=By.XPATH, value="//h2[normalize-space()='Contact Us']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def hide_password_btn(self):
        locator = Locator(by=By.XPATH, value="//div[@class='absolute top-0 right-4 h-full flex items-center cursor-pointer']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def social_media_facebook_btn(self):
        locator = Locator(by=By.XPATH, value="(//a[@target='_blank'])[3]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def facebook_page(self):
        locator = Locator(by=By.CSS_SELECTOR, value=".x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xg8j3zb")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def social_media_instagram_btn(self):
        locator = Locator(by=By.XPATH, value="(//a[@target='_blank'])[4]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def instagram_page(self):
        locator = Locator(by=By.XPATH, value="//a[normalize-space()='Sign up for Instagram']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def social_media_linkedin_btn(self):
        locator = Locator(by=By.XPATH, value="(//a[@target='_blank'])[5]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def linkedin_page(self):
        locator = Locator(by=By.XPATH, value="//button[normalize-space()='Sign in']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def aboutuspage_btn(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'About')]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def aboutus_page(self):
        locator = Locator(by=By.XPATH, value="//h2[normalize-space()='Get to know about us']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def pricing_page_btn(self):
        locator = Locator(by=By.XPATH, value="(//a[@target='_blank'])[7]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def pricing_page(self):
        locator = Locator(by=By.XPATH, value="//h1[contains(text(),'Unleash the Power of Ambition Hire for the Cost of')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def demo_icon_btn(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Demo']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def demo_page(self):
        locator = Locator(by=By.XPATH, value="//h2[normalize-space()='Take a Quick Demo']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def globe_icon_btn(self):
        locator = Locator(by=By.XPATH, value="(//a[@target='_blank'])[1]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def ambitionhire_page(self):
        locator = Locator(by=By.XPATH, value="//h1[contains(text(),'Effortless Assessments with Unlimited Possibilitie')]")
        return BaseElement(driver=self.driver, locator=locator)















