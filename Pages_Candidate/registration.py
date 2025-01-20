from selenium.webdriver.common.by import By
from utils.locators import Locator
from Pages_Candidate.base_page_candidate import BasePage
from utils.base_elements import BaseElement


class Registration(BasePage):
    @property
    def registartion_name_btn(self):
        locator = Locator(by=By.XPATH, value="(//input[@placeholder='Name'])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Email']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def phoneno_btn(self):
        locator = Locator(by=By.XPATH, value="(//input[@placeholder='Phone No.'])[2]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def location_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Location(City)']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def condition_btn(self):
        locator = Locator(by=By.XPATH, value="//label[normalize-space()='I agree to all the']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sendotp_btn(self):
        locator = Locator(by=By.XPATH, value="(//button[@type='button'])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def submitotp_btn(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Submit')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def gmail_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@type='email']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def gmailnext_btn(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Next')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def gmail_enterpasswordbtn(self):
        locator = Locator(by=By.XPATH, value="(//input[@class='whsOnd zHQkBf'])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def gmail_passwordbtn(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Next')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Sendingotp_text(self):
        locator = Locator(by=By.XPATH, value="")
        return BaseElement(driver=self.driver, locator=locator)









