from utils.locators import Locator
from Page_Recruiter.base_page_recruiter import BasePage
from utils.base_elements import BaseElement
from selenium.webdriver.common.by import By

class Candidates(BasePage) :
    @property
    def candidates_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Candidates')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Sortby(self):
        locator = Locator(by=By.XPATH,
                          value="//p[@class='text-[#707070] font-medium whitespace-nowrap' and text()='Sort by:']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def last2week(self):
        locator = Locator(by=By.XPATH,
                          value="//li[contains(@class, 'list') and .//p[@class='text-sm font-medium' and text()='Last 2 weeks']]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Filters(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div[class='hidden sm:flex gap-3 items-center'] span[class='cursor-pointer whitespace-nowrap']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Stages_CTQ(self):
        locator = Locator(by=By.XPATH, value="//label[normalize-space()='CTQ()']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Stages_Functional(self):
        locator = Locator(by=By.XPATH, value="//label[normalize-space()='Functional()']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Stages_English(self):
        locator = Locator(by=By.XPATH, value="//label[normalize-space()='English()']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Stages_Psychometric(self):
        locator = Locator(by=By.XPATH, value="//label[normalize-space()='Psychometric()']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Stages_InReview(self):
        locator = Locator(by=By.XPATH, value="//label[normalize-space()='In-Review()']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Proctoring_status(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Proctoring status']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    #//label[normalize-space()='Passed()']
    def Passed(self):
        locator = Locator(by=By.XPATH, value="//label[normalize-space()='Passed()']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Failed(self):
        locator = Locator(by=By.XPATH, value="//label[normalize-space()='Failed()']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Last_active(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Last active']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Search_Candidate(self):
        locator = Locator(by=By.XPATH, value="//div[@class='hidden lg:block']//input[@placeholder='Search for Candidates']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Action_btn(self):
        locator = Locator(by=By.XPATH, value="//tbody/tr[1]/td[6]/div[1]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Download_Scorecard(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='Download Scorecard']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Candidate_Ceckbox(self):
        locator = Locator(by=By.XPATH,
                          value='//tbody/tr[1]/td[1]/div[1]/div[1]/div[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Candidate_Details(self):
        locator = Locator(by=By.XPATH,
                          value='//tbody/tr[1]/td[3]/div[1]/p[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Score_Card(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="span[class='text-sm font-medium leading-[21px] whitespace-nowrap text-center']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Detailed_Scorecard(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='Detailed score card']")
        return BaseElement(driver=self.driver, locator=locator)


