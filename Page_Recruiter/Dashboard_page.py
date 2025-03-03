from utils.locators import Locator
from Page_Recruiter.base_page_recruiter import BasePage
from utils.base_elements import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dashboard(BasePage):
    @property
    def dashboard_btn(self):
        locator = Locator(by=By.XPATH, value="//span[text()='Dashboard']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def all_jobs_card(self):
        locator = Locator(by=By.XPATH, value= "//h2[contains(text(), 'All Jobs')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def filtered_jobs(self):
        locator = Locator(by=By.CSS_SELECTOR, value= ".flex.flex-col.gap-8.w-full")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def all_jobs_count(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def private_jobs_card(self):
        locator = Locator(by=By.XPATH, value= "//h2[contains(text(), 'Private Jobs')]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def private_jobs_count(self):
        locator = Locator(by=By.XPATH, value= "//body/div/div/div/div[3]/div[1]/div[2]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def public_jobs_card(self):
        locator = Locator(by=By.XPATH, value= "//h2[contains(text(), 'Public Jobs')]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def public_jobs_count(self):
        locator = Locator(by=By.XPATH, value= "//body[1]/div[1]/div[3]/div[2]/div[3]/div[1]/div[3]")
        return BaseElement(driver=self.driver, locator=locator)



    @property
    def active_jobs_card(self):
        locator = Locator(by=By.XPATH, value= "//h2[contains(text(), 'Active Jobs')]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def active_jobs_count(self):
        locator = Locator(by=By.XPATH, value= "//body[1]/div[1]/div[3]/div[2]/div[3]/div[1]/div[4]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def inactive_jobs_card(self):
        locator = Locator(by=By.XPATH, value= "//h2[contains(text(), 'Inactive Jobs')]")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def inactive_jobs_count(self):
        locator = Locator(by=By.XPATH, value= "//body[1]/div[1]/div[3]/div[2]/div[3]/div[1]/div[5]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_job(self):
        locator = Locator(by=By.XPATH, value= "//input[@placeholder='Search by Job Title']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_btn(self):
        locator = Locator(by=By.XPATH, value= "//button[@type='button' and contains(@style, 'background-color: rgb(213, 14, 14);')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def view_details(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div div div div:nth-child(1) div:nth-child(5) div:nth-child(1)")
        return BaseElement(driver=self.driver, locator=locator)



    @property
    def view_details_text(self):
        locator = Locator(by=By.XPATH, value="//p[@class='flex w-full justify-center items-center']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def close_details(self):
        locator = Locator(by=By.XPATH, value="//div[text()='Close']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def graph_detail(self):
        locator = Locator(by=By.XPATH, value="//canvas[@role='img']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def nodata(self):
        # Define the locator
        locator = Locator(by=By.XPATH,
                          value="//p[@class='flex w-full justify-center items-center' and text()='No Data for Stats Available']")
        return BaseElement(driver=self.driver, locator=locator)



    @property
    def download_report(self):
        locator = Locator(by=By.XPATH, value="//div[@class='rounded-md p-2 flex items-center justify-center cursor-pointer']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def recommendation_btn(self):
        locator = Locator(by=By.XPATH, value="//p[@class='text-sm' and text()='Recommendations']")
        return BaseElement(driver=self.driver, locator=locator)