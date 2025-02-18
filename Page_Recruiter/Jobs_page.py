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
    def search_tab(self):
        locator = Locator(by=By.XPATH, value='//input[@placeholder="Search for jobs"]')
        return BaseElement(driver=self.driver, locator=locator)
    #//span[text()="See Details"]
    @property
    def details_btn(self):
        locator = Locator(by=By.XPATH, value='//span[text()="See Details"]')
        return BaseElement(driver=self.driver, locator=locator)
    #//p[text()='Candidates']
    @property
    def candidates_btn(self):
        locator = Locator(by=By.XPATH, value="//p[text()='Candidates']")
        return BaseElement(driver=self.driver, locator=locator)
#//*[@id="input-450"]
    @property
    def candidates_checkbox(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#input-0')
        return BaseElement(driver=self.driver, locator=locator)
    #//input[@placeholder="Search for candidates"]
    @property
    def search_candidates(self):
        locator = Locator(by=By.XPATH, value='//input[@placeholder="Search for candidates"]')
        return BaseElement(driver=self.driver, locator=locator)
    #//p[text()="Settings"]
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

    #//p[text()="Proctoring"]
    @property
    def Proctoring_btn(self):
        locator = Locator(by=By.XPATH, value='//p[text()="Proctoring"]')
        return BaseElement(driver=self.driver, locator=locator)
    #//p[@class='uppercase' and text()='Cut-off & Aggregated Score']
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
    #//span[text()='Create a new Job']
    @property
    def Create_Job(self):
        locator = Locator(by=By.XPATH, value="//span[text()='Create a new Job']")
        return BaseElement(driver=self.driver, locator=locator)

    #//input[@placeholder="Job Title"]
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

#//input[@placeholder='Location(City)']
    @property
    def Location(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Location(City)']")
        return BaseElement(driver=self.driver, locator=locator)

    #//li[contains(text(), 'Haryana: Gurgaon')]
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
    def Next_btn(self):
        locator = Locator(by=By.XPATH, value="//span[text()='Next']")
        return BaseElement(driver=self.driver, locator=locator)

    #JOB SETTINGS

    @property
    def Email_Notification(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Whatsapp_Notification(self):
        locator = Locator(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Assessment_Completion_toggle(self):
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[7]/div[1]/label[1]/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    #div[class='flex gap-6 items-center max-w-[550px]'] div label[class='switch relative inline-block w-11 h-7'] span[class='slider absolute cursor-pointer top-0 left-0 right-0 bottom-0 bg-[#f3f4f5] rounded-[15px] before:h-[22px] before:w-[22px]']
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
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/customaccordion[1]/ul[1]/li[4]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Psychometric_Toggle(self):
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/customaccordion[1]/ul[1]/li[5]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Algorise_Toggle(self):
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/customaccordion[1]/ul[1]/li[6]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Excel_Toggle(self):
        locator = Locator(by=By.XPATH, value="//body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/customaccordion[1]/ul[1]/li[7]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]")
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
    def Next_btn_to_Proctoring(self):
        locator = Locator(by=By.XPATH, value="//span[normalize-space()='Next']")
        return BaseElement(driver=self.driver, locator=locator)

    #PROCTORING PAGE
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


