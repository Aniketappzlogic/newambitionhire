from selenium.webdriver.common.by import By
from utils.locators import Locator
from Pages_Candidate.base_page_candidate import BasePage
from utils.base_elements import BaseElement

class Result(BasePage):
    @property
    def result_page(self):
        locator = Locator(by=By.XPATH, value="(//p[contains(text(),'Results')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def results_checkbox(self):
        locator = Locator(by=By.XPATH, value="//p[contains(text(),'Fraud analyst')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def view_result(self):
        locator = Locator(by=By.XPATH, value="(//div[contains(text(),'View Full Result')])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def download_scorecard(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Scorecard')])")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def incompletejob_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'View incomplete jobs')])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def searchjobname(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Search for jobs, companies, profiles']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def selectfulljob_btn(self):
        locator = Locator(by=By.XPATH, value="//div[contains(text(),'View Full Result')]")
        return BaseElement(driver=self.driver, locator=locator)



