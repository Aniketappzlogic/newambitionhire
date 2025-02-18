from selenium.webdriver.common.by import By
from utils.locators import Locator
from Pages_Candidate.base_page_candidate import BasePage
from utils.base_elements import BaseElement


class ExploreJobs(BasePage):
    @property
    def searchjob_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Search for jobs, companies, profiles']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def applyjob_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Apply Now')])")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Keyword(self):
        locator = Locator(by=By.XPATH, value="//p[@class='font-500 line-clamp-1 text-base' and text()='TESTING -WEB']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def proceed_to_apply_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Proceed to Apply')])")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def refrence_soucre(self):
        locator = Locator(by=By.XPATH, value="//*[@placeholder='Reference Source']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def result_page_btn(self):
        locator = Locator(by=By.XPATH, value="((//p[contains(text(),'Explore Jobs')]))[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select_exam_language_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Language']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select_language_btn(self):
        locator = Locator(by=By.XPATH, value="//li[contains(text(),'English')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def socailmedialink_1(self):
        locator = Locator(by=By.XPATH, value="//a[contains(text(),'https://www.ambitionhire.ai/')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def socialmediatittle(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Ambition Hire')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def job_description_video(self):
        locator = Locator(by=By.CSS_SELECTOR, value="")
        return BaseElement(driver=self.driver, locator=locator)





