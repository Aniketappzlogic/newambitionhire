from msilib.schema import Property

from piglet.parsers.semicolonseparated import value

from utils.locators import Locator
from Page_Recruiter.base_page_recruiter import BasePage
from utils.base_elements import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Jobs(BasePage):
    @property
    def jobs_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Jobs')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def jobs_card(self):
        locator = Locator(by=By.XPATH, value="//div[@class='p-4 border border-outline-color rounded-2xl flex flex-col max-w-[350px]']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def top_jobs_card(self):
        locator = Locator(by=By.XPATH, value="//body/div/div/div/div[3]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def job_card_ellipsis(self):
        locator = Locator(by=By.XPATH, value="//body//div//div//div//div[1]//div[1]//div[2]//div[1]")
        return BaseElement(driver=self.driver, locator=locator)



    @property
    def job_creation_date(self):
        locator = Locator(by=By.XPATH,
                          value="//div[contains(@class, 'flex justify-between') and .//span[text()='See Details']]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def drafts_btn(self):
        locator = Locator(by=By.XPATH, value="//p[@class='uppercase' and text()='Drafts']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def inactive_btn(self):
        locator = Locator(by=By.XPATH, value='//p[@class="uppercase" and text()="Inactive"]')
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def active_btn(self):
        locator = Locator(by=By.XPATH, value='//p[@class="uppercase" and text()="Active"]')
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def jobs_count(self):
        locator = Locator(by=By.CSS_SELECTOR, value= "p[class='font-medium text-[22px]']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sortby(self):
        locator = Locator(by=By.XPATH,
                          value="//p[@class='text-[#707070] font-medium whitespace-nowrap' and text()='Sort by:']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def lastweek(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='Last week']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def last2week(self):
        locator = Locator(by=By.XPATH,
                          value="//li[contains(@class, 'list') and .//p[@class='text-sm font-medium' and text()='Last 2 weeks']]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def last_month(self):
        locator = Locator(by=By.XPATH,
                          value="//li[contains(@class, 'list') and .//p[@class='text-sm font-medium' and text()='Last month']]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def last_3_months(self):
        locator = Locator(by=By.XPATH,
                          value="//li[contains(@class, 'list') and .//p[@class='text-sm font-medium' and text()='Last 3 months']]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def last_6_months(self):
        locator = Locator(by=By.XPATH,
                          value="//li[contains(@class, 'list') and .//p[@class='text-sm font-medium' and text()='Last 6 months']]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def last_year(self):
        locator = Locator(by=By.XPATH,
                          value="//li[contains(@class, 'list') and .//p[@class='text-sm font-medium' and text()='Last year']]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def unpublishjob(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Unpublish']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def job_update_popup(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div[class='flex items-center gap-3 rounded-[64px] p-4 shadow-[0px_4px_24px_0px_#0000001F] backdrop-blur-[2px] fixed bottom-20 z-[100] transition-[right] ease-[ease-in-out] right-8 duration-[0.3s]']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def markjobprivate(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Mark job as Private']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def markjobpublic(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Mark job as Public']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def duplicatejob(self):
        locator = Locator(by=By.XPATH, value="//p[@class='text-xs']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def duplicatejob_popup(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def deletejob(self):
        locator = Locator(by=By.CSS_SELECTOR, value=".text-xs.text-error-color.w-36")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def deletejob_popup(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def publishjob(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Publish']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def search_tab(self):
        locator = Locator(by=By.XPATH, value='//input[@placeholder="Search for jobs"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def clear_search(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.absolute.flex.items-center.right-24.cursor-pointer.h-full.top-0')
        return BaseElement(driver=self.driver, locator=locator)



    @property
    def details_btn(self):
        locator = Locator(by=By.XPATH, value='//span[text()="See Details"]')
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def description(self):
        locator = Locator(by=By.XPATH, value="//h1[normalize-space()='Description']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def details(self):
        locator = Locator(by=By.XPATH, value="//h1[normalize-space()='Details']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def basic_in_seedeatils(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Basic']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def unpublish_after_in_seedeatils(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Unpublish after']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def job_workflow_in_seedeatils(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Job Workflow']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def followcompanyworkflow(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Follow Company Workflow']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def proctoring_in_seedeatils(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Proctoring']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def proctoring_option(self):
        locator = Locator(by=By.XPATH, value="//h4[normalize-space()='Proctoring']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def cutoff_in_seedeatils(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Cut-off & Aggregated Score']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def weightage(self):
        locator = Locator(by=By.XPATH, value="//h4[normalize-space()='Set Assessment Weightage']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def applicationform_in_seedeatils(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Application Form']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def fieldname(self):
        locator = Locator(by=By.XPATH, value="//th[normalize-space()='Field Name']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def language_in_seedeatils(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Language']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def language_heading(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Language']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def editjob(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Edit Job']")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def editjob_popbox(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
        return BaseElement(driver=self.driver, locator=locator)






    @property
    def candidates_btn(self):
        locator = Locator(by=By.XPATH, value="//p[text()='Candidates']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def candidates_count(self):
        locator = Locator(by=By.CSS_SELECTOR, value="h3[class='text-[22px] font-medium whitespace-nowrap hidden lg:block']")
        return BaseElement(driver=self.driver, locator=locator)



    @property
    def candidates_checkbox(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#input-0')
        return BaseElement(driver=self.driver, locator=locator)
    #//input[@placeholder="Search for candidates"]
    @property
    def search_candidates(self):
        locator = Locator(by=By.XPATH, value='//input[@placeholder="Search for candidates"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Settings_btn(self):
        locator = Locator(by=By.XPATH, value='//p[text()="Settings"]')
        return BaseElement(driver=self.driver, locator=locator)
    #//p[text()="Basic"]
    @property
    def Basics_btn(self):
        locator = Locator(by=By.XPATH, value='//p[text()="Basic"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Job_Workflow_btn(self):
        locator = Locator(by=By.XPATH, value='//p[text()="Job Workflow"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Proctoring_btn(self):
        locator = Locator(by=By.XPATH, value='//p[text()="Proctoring"]')
        return BaseElement(driver=self.driver, locator=locator)
  
    @property
    def Cutoff(self):
        locator = Locator(by=By.XPATH,value="//p[@class='uppercase' and text()='Cut-off & Aggregated Score']")
        return BaseElement(driver=self.driver,locator=locator)
    @property
    def Application_Form(self):
        locator = Locator(by=By.XPATH, value= "//p[text()='Application Form']")
        return BaseElement(driver=self.driver, locator=locator)

    #//p[text()='Language']
    @property
    def Language_btn(self):
        locator = Locator(by=By.XPATH, value= "//p[text()='Language']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Save_btn(self):
        locator = Locator(by=By.XPATH, value="//span[text()='Save']")
        return BaseElement(driver=self.driver, locator=locator)


#CREATE NEW JOB
    @property
    def Create_Job(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Create a new Job']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Create_Job_page(self):
        locator = Locator(by=By.XPATH, value="//h3[normalize-space()='New Job Posting']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Saveasdraft(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Save as draft']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def TitleRequired(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Title is required']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def NotificationTitleRequired(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Notification Title is required']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def DepartmentRequired(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Department is required']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def IndustryRequired(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Industry is required']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def EmploymentTypeRequired(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Employment Type is required']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def WorkplaceTypeRequired(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Workplace Type is required']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def LocationRequired(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Location Search Text is required']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def MinSalaryRequired(self):
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[10]/div[1]/div[1]/div[1]/p[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def MaxSalaryRequired(self):
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[10]/div[3]/div[1]/div[1]/p[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Leave_job_posting(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Yes, leave']")
        return BaseElement(driver=self.driver, locator=locator)











    @property
    def Job_Title(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Job Title']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Notification_Title(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Notification Title']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Job_Description(self):
        locator = Locator(by=By.XPATH, value="//p[@data-placeholder='Job Description']")
        return BaseElement(driver=self.driver, locator=locator)
#driver.findElement(By.xpath("//input[@placeholder='Department']"))
    @property
    def Department(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Department']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Department_selector(self):
        locator = Locator(by=By.XPATH, value="//li[text()='Human Resources']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Industry(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Industry']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Industry_selector(self):
        locator = Locator(by=By.XPATH, value="//li[contains(text(), 'E-Commerce')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Employment_Type(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Employment Type']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Employmenttype_selector(self):
        locator = Locator(by=By.XPATH, value="//li[contains(text(), 'Full-Time')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Workplace_Type(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Workplace Type']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Workplace_Type_Selector(self):
        locator = Locator(by=By.XPATH, value="//li[contains(text(), 'Onsite')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Work_Experience(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Work Experience']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Workplace_Experience_Selector(self):
        locator = Locator(by=By.XPATH, value="//li[contains(text(), 'ASSOCIATE (1-3 year)')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Location(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Location(City)']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Location_selector(self):
        locator = Locator(by=By.XPATH, value="//li[contains(text(), 'Haryana: Gurgaon')]")
        return BaseElement(driver=self.driver, locator=locator)

    #//input[@placeholder='Min. Annual Salary']
    @property
    def Min_Salary(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Min. Annual Salary']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Max_Salary(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Max. Annual Salary']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Max_Salary_less_than_min_salary(self):
        locator = Locator(by=By.XPATH, value="//p[contains(text(),'Max salary must be greater than or equal to min sa')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Next_btn(self):
        locator = Locator(by=By.XPATH, value="//span[text()='Next']")
        return BaseElement(driver=self.driver, locator=locator)

    #JOB SETTINGS

    @property
    def Reapply_toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div[class='flex flex-col gap-4'] div[class='flex gap-6 items-center'] div label[class='switch relative inline-block w-11 h-7'] span[class='slider absolute cursor-pointer top-0 left-0 right-0 bottom-0 bg-[#f3f4f5] rounded-[15px] before:h-[22px] before:w-[22px]']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Reapplyfield(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Re-apply after(Days)']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Email_Notification(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def toggle_on(self):
        locator = Locator(by=By.CLASS_NAME, value="tick-mark")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Whatsapp_Notification(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Whatsapp_Notification(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Waterfall_toggle(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Mobile_Device_Assessment_toggle(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Backtracking_toggle(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Assessment_Completion_toggle(self):
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[7]/div[1]/label[1]/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def OneSitting_toggle(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="div[class='flex gap-6 items-center max-w-[550px]'] div label[class='switch relative inline-block w-11 h-7'] span[class='slider absolute cursor-pointer top-0 left-0 right-0 bottom-0 bg-[#f3f4f5] rounded-[15px] before:h-[22px] before:w-[22px]']")
        return BaseElement(driver=self.driver, locator=locator)

    #//span[normalize-space()='Next']



    @property
    def Next_butn(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Next']")
        return BaseElement(driver=self.driver, locator=locator)



    #JOB WORKFLOW PAGE

    @property
    def Company_Workflow(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div[class='workflow-title pt-2 text-base font-semibold text-black'] div[class='toggle-switch-text'] div label[class='switch relative inline-block w-11 h-7'] span[class='slider absolute cursor-pointer top-0 left-0 right-0 bottom-0 bg-[#f3f4f5] rounded-[15px] before:h-[22px] before:w-[22px]']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Assessment_toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div[class='workflow-title text-sm font-normal text-black'] div[class='toggle-switch-text'] div label[class='switch relative inline-block w-11 h-7'] span[class='slider absolute cursor-pointer top-0 left-0 right-0 bottom-0 bg-[#f3f4f5] rounded-[15px] before:h-[22px] before:w-[22px]']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def CTQ_Toggle(self):
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/customaccordion[1]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Functional_Toggle(self):
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/customaccordion[1]/ul[1]/li[2]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def English_Toggle(self):
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/customaccordion[1]/ul[1]/li[3]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Multilingual_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > customaccordion:nth-child(6) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Psychometric_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > customaccordion:nth-child(6) > ul:nth-child(1) > li:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Algorise_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > customaccordion:nth-child(6) > ul:nth-child(1) > li:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Excel_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > customaccordion:nth-child(6) > ul:nth-child(1) > li:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Typing_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > customaccordion:nth-child(6) > ul:nth-child(1) > li:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def OneWayInterview_Toggle(self):
        locator = Locator(by=By.XPATH, value="//body/div/div/div/div/div/div/div/customaccordion[@title='Assessments']/div/div/div/label/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Result_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div[class='py-4 text-sm font-normal flex flex-col gap-4'] div[class='toggle-switch-text'] div label[class='switch relative inline-block w-11 h-7'] span[class='slider absolute cursor-pointer top-0 left-0 right-0 bottom-0 bg-[#f3f4f5] rounded-[15px] before:h-[22px] before:w-[22px]']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Detailed_Result_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div[class='toggle-switch-text pl-6'] div span[class='slider absolute cursor-pointer top-0 left-0 right-0 bottom-0 bg-[#f3f4f5] rounded-[15px] rounded-[20px] before:h-4 before:w-4']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def In_Review_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Salary_Discussion_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(13) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Hire_or_Rejected_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(15) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Next_btn_to_Proctoring(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Next']")
        return BaseElement(driver=self.driver, locator=locator)

    #PROCTORING PAGE

    @property
    def Proctoring_Page(self):
        locator = Locator(by=By.CSS_SELECTOR, value="p[class='text-[22px] text-onbackground-color font-normal']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Proctoring_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def AntiCheat_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Next_to_Cutoff(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Next']")
        return BaseElement(driver=self.driver, locator=locator)


    #//span[normalize-space()='Next']
    @property
    def Next_to_Lang(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Next']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Hindi_Lang(self):
        locator = Locator(by=By.XPATH, value="//tbody/tr[2]/td[2]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Next_to_AppForm(self):
        locator = Locator(by=By.CSS_SELECTOR, value="button[class='font-Poppins px-4 py-2 flex items-center gap-2 justify-center rounded-[80px] border-2 cursor-pointer'] span[class='text-sm font-medium leading-[21px] whitespace-nowrap text-center']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Save_Draft(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body div div div div div div button:nth-child(2) span:nth-child(1)")
        return BaseElement(driver=self.driver, locator=locator)

    #h3_element = driver.find_element(By.XPATH, '//h3[@class="text-[22px] whitespace-nowrap"]')
    @property
    def Job_Saved_Popup(self):
        locator = Locator(by=By.XPATH,
                          value='//h3[@class="text-[22px] whitespace-nowrap"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def View_Job(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='View Job']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Options(self):
        locator = Locator(by=By.XPATH, value = '//body//div//div//div//div[1]//div[1]//div[2]//div[1]')
        return BaseElement(driver=self.driver, locator= locator)

    @property
    def Duplicate_Job(self):
        locator = Locator(by=By.XPATH, value='//li[contains(text(), "Duplicate Job")]')
        return BaseElement(driver=self.driver, locator=Locator)


