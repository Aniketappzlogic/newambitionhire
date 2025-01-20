from selenium.webdriver.common.by import By
from utils.locators import Locator
from Page_Recruiter.base_page_recruiter import BasePage
from utils.base_elements import BaseElement


class Loginrecruiter(BasePage):
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
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Login')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def hidepassword_btn(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Login')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def troublesigning_btn(self):
        locator = Locator(by=By.XPATH, value="//p[@class='font-medium text-sm cursor-pointer text-ambition-fandango-color']")
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
    def hide_password_btn(self):
        locator = Locator(by=By.XPATH, value="//div[@class='absolute top-0 right-4 h-full flex items-center cursor-pointer']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def social_media_facebook_btn(self):
        locator = Locator(by=By.XPATH, value="(//a[@target='_blank'])[3]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def social_media_instagram_btn(self):
        locator = Locator(by=By.XPATH, value="(//a[@target='_blank'])[4]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def social_media_linkdien_btn(self):
        locator = Locator(by=By.XPATH, value="(//a[@target='_blank'])[5]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def aboutuspage_btn(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'About')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def pricing_page_btn(self):
        locator = Locator(by=By.XPATH, value="(//a[@target='_blank'])[7]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def globe_icon_btn(self):
        locator = Locator(by=By.XPATH, value="(//a[@target='_blank'])[1]")
        return BaseElement(driver=self.driver, locator=locator)














