from selenium.webdriver.common.by import By
from utils.locators import Locator
from Pages_Candidate.base_page_candidate import BasePage
from utils.base_elements import BaseElement


class Login(BasePage):
    @property
    def login_btn(self):
        locator = Locator(by=By.XPATH, value="(//button[@class='font-Poppins border px-[68px] py-3 rounded-[80px] cursor-pointer'])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def name_btn(self):
        locator = Locator(by=By.XPATH,    value="(//input[@placeholder='Name'])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def phonenumber_btn(self):
        locator = Locator(by=By.XPATH, value="(//input[@placeholder='Phone No.'])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sendotp_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Send OTP')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def submitotp_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Submit')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def exploretext(self):
        locator = Locator(by=By.XPATH, value="(//p[text()='Explore Jobs'])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Sendingotp_text(self):
        locator = Locator(by=By.XPATH, value="(//input[@type='number'])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Resend_otp(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Resend')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def edit_number(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Edit ')]")
        return BaseElement(driver=self.driver, locator=locator)


