from utils.locators import Locator
from Page_Recruiter.base_page_recruiter import BasePage
from utils.base_elements import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dashboard(BasePage):
    @property
    def dashboard_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Dashboard')])[1]")
        return BaseElement(driver=self.driver, locator=locator)
# class Dashboard(BasePage):
#     @property
#     def dashboard_btn(self):
#         locator = (By.XPATH, "(//span[contains(text(),'Dashboard')])[1]")
#         return BaseElement(driver=self.driver, locator=locator)


class AllJobs(BasePage):
    @property
    def all_jobs_card(self):
        locator = Locator(by=By.XPATH, value= "(//h2[text()='All Jobs'])")
        return BaseElement(driver=self.driver, locator=locator)


class PrivateJobs(BasePage):
    @property
    def private_jobs_card(self):
        locator = Locator(by=By.XPATH, value= "(//h2[text()='Private Jobs'])")
        return BaseElement(driver=self.driver, locator=locator)


class PublicJobs(BasePage):
    @property
    def public_jobs_card(self):
        locator = Locator(by=By.XPATH, value= "(//h2[text()='Public Jobs'])")
        return BaseElement(driver=self.driver, locator=locator)

class ActiveJobs(BasePage):
    @property
    def active_jobs_card(self):
        locator = Locator(by=By.XPATH, value= "(//h2[text()='Active Jobs'])")
        return BaseElement(driver=self.driver, locator=locator)

class InactiveJobs(BasePage):
    @property
    def inactive_jobs_card(self):
        locator = Locator(by=By.XPATH, value= "(//h2[text()='Inactive Jobs'])")
        return BaseElement(driver=self.driver, locator=locator)

   #//div[text()='View Details']
class ViewDetails(BasePage):
    @property
    def view_details(self):
        locator = Locator(by=By.XPATH, value= "(//div[text()='View Details'] )")
        return BaseElement(driver=self.driver, locator=locator)

class SearchJob(BasePage):
    @property
    def search_job(self):
        locator = Locator(by=By.XPATH, value= "//input[@placeholder='Search by Job Title']")
        return BaseElement(driver=self.driver, locator=locator)

class Searchbutton(BasePage):
    @property
    def search_btn(self):
        locator = Locator(by=By.XPATH, value= "//button[@type='button' and contains(@style, 'background-color: rgb(213, 14, 14);')]")
        return BaseElement(driver=self.driver, locator=locator)