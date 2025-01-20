from selenium.webdriver.common.by import By
from utils.locators import Locator
from Pages_Candidate.base_page_candidate import BasePage
from utils.base_elements import BaseElement

class TrainingModule(BasePage):
    @property
    def training_module_tab(self):
        locator = Locator(by=By.XPATH, value="(//p[contains(text(),'Training Module')])[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def select_training_module(self):
        locator = Locator(by=By.XPATH, value="//div[@class='flex flex-col p-3 gap-3 h-full']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def start_course(self):
        locator = Locator(by=By.XPATH, value="//span[contains(text(),'Start course')]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def playvideo(self):
        locator = Locator(by=By.XPATH, value="//*[@class='video-wrapper grid place-content-center']/video")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def openpdf(self):
        locator = Locator(by=By.XPATH, value="(//p[contains(text(),' Click to open the document ')])[1]")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def openpdf1(self):
        locator = Locator(by=By.XPATH, value="(//p[contains(text(),' Click to open the document ')])[2]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def exitthescreen(self):
        locator = Locator(by=By.XPATH, value="//div[@class='z-[99] fixed w-screen h-screen left-0 top-0 bg-modal-backdrop flex items-center justify-center backdrop']")
        return BaseElement(driver=self.driver, locator=locator)
