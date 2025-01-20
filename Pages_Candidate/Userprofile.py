from selenium.webdriver.common.by import By
from utils.locators import Locator
from Pages_Candidate.base_page_candidate import BasePage
from utils.base_elements import BaseElement


class Userprofile(BasePage):
    @property
    def profileicon_btn(self):
        locator = Locator(by=By.XPATH, value="(//div[contains(@class, 'relative')])[6]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def selectingprofileicon_btn(self):
        locator = Locator(by=By.XPATH, value="//li[text()=' Profile ']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def clickprofileimage_btn(self):
        locator = Locator(by=By.XPATH, value="//div[@class='relative flex flex-col gap-2 cursor-pointer items-center']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def takephoto_btn(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Take Photo')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def savephoto_btn(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Done')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def savechanges_btn(self):
        locator = Locator(by=By.XPATH, value="//p[contains(text(),'SAVE CHANGES')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def downlaodimage_btn(self):
        locator = Locator(by=By.XPATH, value="//a[contains(text(),'Download')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def uploadimagefromdesktop_btn(self):
        locator = Locator(by=By.XPATH, value="//p[contains(text(),'OR UPLOAD FROM DEVICE')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def edit_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Edit')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def edit_address_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Address']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def saveaddress_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Save Changes')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def explorepage_btn(self):
        locator = Locator(by=By.XPATH, value="(//p[contains(text(), 'Explore Jobs')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def edit_btn_qualification(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Edit')])[3]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def qualification_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Highest Qualification']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select_qualification_btn(self):
        locator = Locator(by=By.XPATH, value="//li[contains(text(),'Other')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select_course_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Course']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select_educationplace_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='School/University/College Name']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select_percentage_btn(self):
        locator = Locator(by=By.XPATH, value=" //input[@placeholder='CGPA']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select_passingyear_btn(self):
        locator = Locator(by=By.XPATH, value=" //input[@placeholder='Passing Year']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def save_qualification_details_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Save Changes')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def edit_btn_guardian(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Edit')])[4]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_guardian_btn(self):
        locator = Locator(by=By.XPATH, value="(//div[@class='border border-outline-color border-dotted rounded-lg items-center justify-center cursor-pointer'])[1]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def add_guardian_name_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Full Name']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_2ndguardian_name_btn(self):
        locator = Locator(by=By.XPATH, value="(//input[@placeholder='Full Name'])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_guardian_mobileno_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Mobile Number']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_guardian_mobileno2_btn(self):
        locator = Locator(by=By.XPATH, value="(//input[@placeholder='Mobile Number'])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_guardian_relation_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Relation']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_2ndguardian_relation_btn(self):
        locator = Locator(by=By.XPATH, value="(//input[@placeholder='Relation'])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def save_guardian_details_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Save Changes')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def delete_guardian_details_btn(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div[class='flex items-center']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def edit_certifiaction_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Edit')])[5]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_certifiaction_btn(self):
        locator = Locator(by=By.XPATH, value="//p[@class='text-xs text-decorative-color']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_certifiaction_name_btn(self):
        locator = Locator(by=By.XPATH, value="//label[contains(text(),'Certificate Name')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_certifiaction_number_btn(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Certificate ID/Number']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def choose_certificate_from_device_btn(self):
        locator = Locator(by=By.XPATH, value="//label[@class='file-input cursor-pointer inline-block font-semibold underline']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def edit_resume_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Edit')])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def choose_Resume_from_device_btn(self):
        locator = Locator(by=By.XPATH,value="(//label[@class='file-input cursor-pointer inline-block font-semibold underline'])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def save_resume_btn(self):
        locator = Locator(by=By.XPATH, value="(//span[contains(text(),'Save Changes')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def view_resume_btn(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'View')]")
        return BaseElement(driver=self.driver, locator=locator)












