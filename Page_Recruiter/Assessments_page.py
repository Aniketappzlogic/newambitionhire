import time

from utils.locators import Locator
from Page_Recruiter.base_page_recruiter import BasePage
from utils.base_elements import BaseElement
from selenium.webdriver.common.by import By

class Assessments(BasePage) :
    @property
    def assessments_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Assessments')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def inactive_btn(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Inactive Jobs']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def drafts_btn(self):
        locator = Locator(by=By.XPATH, value="//p[normalize-space()='Drafts']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Nav_Button(self):
        locator = Locator(by=By.XPATH, value="//i[@class='mdi-chevron-right mdi v-icon notranslate v-theme--light v-icon--size-default']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_tab(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Search for jobs']")
        return BaseElement(driver=self.driver, locator=locator)

    #span[class='text-sm font-medium leading-[21px] whitespace-nowrap text-center']
    @property
    def select_job(self):
        locator = Locator(by=By.CSS_SELECTOR, value="span[class='text-sm font-medium leading-[21px] whitespace-nowrap text-center']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Create_New_Assessment(self):
        locator = Locator(by=By.CSS_SELECTOR, value="span[class='text-sm font-medium leading-[21px] whitespace-nowrap text-center']")
        return BaseElement(driver=self.driver, locator=locator)

#////////////////  CTQ ///////////////////////////////////
    @property
    def Add_CTQ(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='CTQ']")
        return BaseElement(driver=self.driver, locator=locator)

    #//input[@placeholder='Name']

    @property
    def CTQ_name(self):
        locator = Locator(by=By.XPATH,
                          value="//input[@placeholder='Name']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def CTQ_duration(self):
        locator = Locator(by=By.XPATH,
                          value="//input[@placeholder='Minute(s)']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def CTQ_cutoff(self):
        locator = Locator(by=By.XPATH,
                          value="//input[@placeholder='Cut-off']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Cutoff_value(self):
        locator = Locator(by=By.XPATH,
                          value="//li[normalize-space()='10%']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def CTQ_instructions(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='Instructions']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def CTQ_questions(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='Questions']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Add_Custom_questions(self):
        locator = Locator(by=By.XPATH,
                          value="//span[normalize-space()='Add Custom Question']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Custom_question_field(self):
        locator = Locator(by=By.XPATH,
                          value="//input[contains(@placeholder,'Enter custom question here')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def FreeText_Toggle(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="span[class='slider absolute cursor-pointer top-0 left-0 right-0 bottom-0 bg-[#f3f4f5] rounded-[15px] before:h-[22px] before:w-[22px]']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Save_button(self):
        locator = Locator(by=By.XPATH,
                          value="//span[normalize-space()='Save']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def questions(self):
        locator = Locator(by=By.XPATH,
                          value="//div//div//div[3]//div[1]//div[2]//button[1]//span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def questions2(self):
        locator = Locator(by=By.XPATH,
                          value="//body//div//div//div//div//div[2]//div[2]//button[1]//span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def CTQ_SaveChanges(self):
        locator = Locator(by=By.XPATH,
                          value="//span[normalize-space()='Save Changes']")
        return BaseElement(driver=self.driver, locator=locator)

    #//////////// FUNCTIONAL ///////////

    @property
    def Add_Functional(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='FUNCTIONAL']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Functional_name(self):
        locator = Locator(by=By.XPATH,
                          value="//input[@placeholder='Name']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Functional_cutoff(self):
        locator = Locator(by=By.XPATH,
                          value="//input[@placeholder='Cut-off']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Func_Cutoff_value(self):
        locator = Locator(by=By.XPATH,
                          value="//li[normalize-space()='10%']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Save_Next(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="span[class='text-sm font-medium leading-[21px] whitespace-nowrap text-center']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Func_Modules(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='Modules']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Func_Search_Modules(self):
        locator = Locator(by=By.XPATH,
                          value="//input[@placeholder='Search Modules']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Add_Module(self):
        locator = Locator(by=By.XPATH,
                          value="//div[5]//div[1]//div[4]//button[1]//span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Maths_Easy_Ques(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Ques_1(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Ques_2(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Ques_3(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Maths_Medium_Ques(self):
        locator = Locator(by=By.XPATH,
                          value="//body/div/div/div/div/div/div[3]/div[1]/div[1]/p[1]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Med_Ques_1(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Med_Ques_2(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Med_Ques_3(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Maths_Hard_Ques(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[4]/div[1]/div[1]/p[1]/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Hard_Ques_1(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Hard_Ques_2(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Hard_Ques_3(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/div[1]/div[1]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def Save_Changes_Func(self):
        locator = Locator(by=By.XPATH,
                          value="//span[normalize-space()='Save Changes']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Finish_Func(self):
        locator = Locator(by=By.XPATH,
                          value="//span[normalize-space()='Finish']")
        return BaseElement(driver=self.driver, locator=locator)

    #////////////////////////////  ENGLISH ASSESSMENT//////////////////////////////////

    @property
    def Add_English(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='ENGLISH']")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def English_name(self):
        locator = Locator(by=By.XPATH,
                          value="//input[@placeholder='Name']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def English_cutoff(self):
        locator = Locator(by=By.XPATH,
                          value="//input[@placeholder='Cut-off']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def English_Cutoff_value(self):
        locator = Locator(by=By.XPATH,
                          value="//li[normalize-space()='10%']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def English_Instructions(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='Instructions']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def English_Modules(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='Modules']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def English_Search_Modules(self):
        locator = Locator(by=By.XPATH,
                          value="//input[@placeholder='Search Modules']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Add_Eng_Module(self):
        locator = Locator(by=By.XPATH,
                          value="//span[normalize-space()='Add']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Easy_Ques(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Medium_Ques(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Hard_Ques(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Save_Module(self):
        locator = Locator(by=By.XPATH,
                          value="//span[normalize-space()='Save']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Para_Writing_Topic(self):
        locator = Locator(by=By.XPATH,
                          value="//input[@placeholder='Enter Topic']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Save_Para_Topic(self):
        locator = Locator(by=By.XPATH,
                          value="//span[normalize-space()='Save Changes']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Free_Speech_Custom_Ques(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="div[class='flex flex-col gap-2 text-sm font-medium'] div[class='flex items-center justify-center p-2 rounded-lg cursor-pointer']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Custom_Ques1(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def Custom_Ques2(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        return BaseElement(driver=self.driver, locator=locator)
    @property
    def Custom_Ques3(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value="body > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > input:nth-child(1)")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Save_All_Eng_Mods(self):
        locator = Locator(by=By.XPATH,
                          value="//span[normalize-space()='Save Changes']")
        return BaseElement(driver=self.driver, locator=locator)

    #/////////////////////// PSYCHOMETRIC ASSESSMENT /////////////////////

    @property
    def Psychometric(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='PSYCHOMETRIC']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Specific_Personality_Traits(self):
        locator = Locator(by=By.XPATH,
                          value="//body[1]/div[1]/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]/button[1]/span[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Psychometric_Instructions(self):
        locator = Locator(by=By.XPATH,
                          value="//p[normalize-space()='Instructions']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def Save_Psychometric(self):
        locator = Locator(by=By.XPATH,
                          value="//span[normalize-space()='Save Changes']")
        return BaseElement(driver=self.driver, locator=locator)
























































