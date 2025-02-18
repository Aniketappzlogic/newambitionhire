import logging
import time
from datetime import datetime
import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Page_Recruiter.Assessments_page import Assessments
from Page_Recruiter.login import Loginrecruiter
from conftest import driver, env

logger = logging.getLogger()
logger.setLevel(logging.INFO)
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")


@pytest.mark.regression
@pytest.mark.assessments_page
def test_assessments_page(env, driver, authenticated_user):
    logging.info(f"environment -> {env}")
    login = authenticated_user
    recruiter_login = Loginrecruiter(driver)
    recruiter_login.username_btn.send_keys('inderjeetkmcs@gmail.com')
    recruiter_login.password_btn.send_keys('123')
    logging.info(f"Password entered")

    # recruiter_login.hidepassword_btn.click()
    # logging.info(f"hide passwrd btn clicked")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Login')]"))
    )
    recruiter_login.login_btn.click()
    logging.info(f"login btn clicked")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//h2[text()='Private Jobs'])"))
    )
    assessment_page = Assessments(driver)
    assessment_page.assessments_btn.click()
    logging.info(f"Assessments btn clicked")
    logger.info(f"assessment page btn clicked")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//body/div/div/div/div/div/div/div/div/div/div[1]/div[1]"))
    )

    inactivejobs = Assessments(driver)
    inactivejobs.inactive_btn.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//body/div/div/div/div/div/div/div/div/div/div[1]/div[1]"))
    )

    draftjobs = Assessments(driver)
    draftjobs.drafts_btn.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//body/div/div/div/div/div/div/div/div/div/div[1]/div[1]"))
    )

    # NavButton = Assessments(driver)  #BUG
    # NavButton.Nav_Button.click()

    searchtab = Assessments(driver)
    searchtab.search_tab.send_keys('Automated 1002')

    selectjob = Assessments(driver)
    selectjob.select_job.click()

    CreateNewAssessment =  Assessments(driver)
    CreateNewAssessment.Create_New_Assessment.click()
    time.sleep(4)

   ## //////////////////  CTQ  ///////////(COMMENT OUT ctq CODE IF CTQ IS NOT SELECTED FOR ASSESSMENT )

    AddCTQ = Assessments(driver)
    AddCTQ.Add_CTQ.click()

    CTQname = Assessments(driver)
    CTQname.CTQ_name.send_keys('CTQ')

    CTQduration = Assessments(driver)
    CTQduration.CTQ_duration.send_keys(10)

    CTQcutoff = Assessments(driver)
    CTQcutoff.CTQ_cutoff.click()

    CutoffValue = Assessments(driver)
    CutoffValue.Cutoff_value.click()

    CTQinstructions = Assessments(driver)
    CTQinstructions.CTQ_instructions.click()

    CTQques = Assessments(driver)
    CTQques.CTQ_questions.click()

#/////////////// ADD CUSTOM QUESTIONS //////////////////////////

    #//// FREE TEXT QUES ////
    ques_to_send = [
        "What is your name?",
        "What is your current Location?",
        "Do you have a passport?",
        "Do you know Python?",
        ""
    ]

    for i in range (4):
        AddCustomQues = Assessments(driver)
        AddCustomQues.Add_Custom_questions.click()

        CustomQuesField = Assessments(driver)
        CustomQuesField.Custom_question_field.send_keys(ques_to_send[i])

        FreeTextToggle = Assessments(driver)
        FreeTextToggle.FreeText_Toggle.click()

        SaveButton = Assessments(driver)
        SaveButton.Save_button.click()

    for i in range (2):
        AddCustomQues = Assessments(driver)
        AddCustomQues.Add_Custom_questions.click()

        CustomQuesField = Assessments(driver)
        CustomQuesField.Custom_question_field.send_keys(ques_to_send[i])

        SaveButton = Assessments(driver)
        SaveButton.Save_button.click()

    CTQLibQues = Assessments(driver)
    CTQLibQues.questions.click()
    CTQLibQues.questions2.click()

    SaveChanges = Assessments(driver)
    SaveChanges.CTQ_SaveChanges.click()

  #//////////////////////////////  FUNCTIONAL ASSESSMENT  ////////////// (COMMENT OUT IF FUNCTIONAL IS NOT SELECTED FOR ASSESSMENT ) ////////////////////////

    searchtab = Assessments(driver)
    searchtab.search_tab.send_keys('Automated 1002')   #CHANGE THIS ACCORDING TO JOB NAME

    selectjob = Assessments(driver)
    selectjob.select_job.click()

    CreateNewAssessment = Assessments(driver)
    CreateNewAssessment.Create_New_Assessment.click()
    time.sleep(4)

    AddFunctional = Assessments(driver)
    AddFunctional.Add_Functional.click()

    FunctionalName = Assessments(driver)
    FunctionalName.Functional_name.send_keys('Functional')

    FunctionalCutoff = Assessments(driver)
    FunctionalCutoff.Functional_cutoff.click()
    logger.info(f"cutoff")


    FuncCutoffvalue = Assessments(driver)
    FuncCutoffvalue.Func_Cutoff_value.click()


    SaveandNext = Assessments(driver)
    SaveandNext.Save_Next.click()
    logger.info(f"Save and Next clicked")


    FuncModules =Assessments(driver)
    FuncModules.Func_Modules.click()
    logger.info(f"Modules clicked")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//body/div/div/div/div/div[5]/div[1]"))
    )


    SearchModules = Assessments(driver)
    SearchModules.Func_Search_Modules.send_keys('Mathematical Ability')

    AddModule = Assessments(driver)
    AddModule.Add_Module.click()

    EasyQues = Assessments(driver)
    EasyQues.Maths_Easy_Ques.click()

    Ques = Assessments(driver)
    Ques.Ques_1.click()
    Ques.Ques_2.click()
    Ques.Ques_3.click()
    EasyQues = Assessments(driver)
    EasyQues.Maths_Easy_Ques.click()

    MediumQues = Assessments(driver)
    MediumQues.Maths_Medium_Ques.click()

    MedQues = Assessments(driver)
    MedQues.Med_Ques_1.click()
    MedQues.Med_Ques_2.click()
    MedQues.Med_Ques_3.click()
    MediumQues = Assessments(driver)
    MediumQues.Maths_Medium_Ques.click()

    HardQues = Assessments(driver)
    HardQues.Maths_Hard_Ques.click()

    HQues = Assessments(driver)
    HQues.Hard_Ques_1.click()
    HQues.Hard_Ques_2.click()
    HQues.Hard_Ques_3.click()
    HardQues = Assessments(driver)
    HardQues.Maths_Hard_Ques.click()

    SaveChangesFunc = Assessments(driver)
    SaveChangesFunc.Save_Changes_Func.click()
    time.sleep(4)


    FinishFunc = Assessments(driver)
    FinishFunc.Finish_Func.click()

    #//////////////////////////////  ENGLISH  ///////////////////////////////////////////

    searchtab = Assessments(driver)
    searchtab.search_tab.send_keys('Automated 1002')  # CHANGE THIS ACCORDING TO JOB NAME

    selectjob = Assessments(driver)
    selectjob.select_job.click()

    CreateNewAssessment = Assessments(driver)
    CreateNewAssessment.Create_New_Assessment.click()
    time.sleep(4)

    AddEnglish = Assessments(driver)
    AddEnglish.Add_English.click()

    English_Assessment_Name = Assessments(driver)
    English_Assessment_Name.English_name.send_keys("English Assessment")

    EnglishCutOff = Assessments(driver)
    EnglishCutOff.English_cutoff.click()

    EnglishCutOffValue = Assessments(driver)
    EnglishCutOffValue.English_Cutoff_value.click()

    EnglishInstructions = Assessments(driver)
    EnglishInstructions.English_Instructions.click()

    EnglishModules = Assessments(driver)
    EnglishModules.English_Modules.click()

    #//////////////////  Adding Error Indetification Module /////////////////////

    EnglishSearchModules = Assessments(driver)
    EnglishSearchModules.English_Search_Modules.send_keys('Error Identification')

    ErrorIdentification = Assessments(driver)
    ErrorIdentification.Add_Eng_Module.click()

    for i in range (2):
       EIEasyQues = Assessments(driver)
       EIEasyQues.Easy_Ques.click()

    for i in range (2):
       EIMedQues = Assessments(driver)
       EIMedQues.Medium_Ques.click()

    for i in range (2):
       EIHardQues = Assessments(driver)
       EIHardQues.Hard_Ques.click()

    SaveEIModule = Assessments(driver)
    SaveEIModule.Save_Module.click()

    #//////////////////////////// Adding Passage Module /////////////////

    EnglishSearchModules = Assessments(driver)
    EnglishSearchModules.English_Search_Modules.clear()
    EnglishSearchModules.English_Search_Modules.send_keys('Passage')

    AddPassage = Assessments(driver)
    AddPassage.Add_Eng_Module.click()

    for i in range (2):
       PassageEasyQues = Assessments(driver)
       PassageEasyQues.Easy_Ques.click()

    for i in range (2):
       PassageMedQues = Assessments(driver)
       PassageMedQues.Medium_Ques.click()

    SavePassageModule = Assessments(driver)
    SavePassageModule.Save_Module.click()

    ##///////////////////////////////   ADDING GRAMMAR MODULE ///////////////////

    EnglishSearchModules = Assessments(driver)
    EnglishSearchModules.English_Search_Modules.clear()
    EnglishSearchModules.English_Search_Modules.send_keys('Grammar')

    AddPassage = Assessments(driver)
    AddPassage.Add_Eng_Module.click()

    for i in range(2):
        EasyQues = Assessments(driver)
        EasyQues.Easy_Ques.click()

    for i in range(2):
        MedQues = Assessments(driver)
        MedQues.Medium_Ques.click()

    for i in range (2):
       HardQues = Assessments(driver)
       HardQues.Hard_Ques.click()

    SavePassageModule = Assessments(driver)
    SavePassageModule.Save_Module.click()


    ##/////////////////// ADDING LISTEN AND TYPE MODULE ////////////////


    EnglishSearchModules = Assessments(driver)
    EnglishSearchModules.English_Search_Modules.clear()
    EnglishSearchModules.English_Search_Modules.send_keys('Listen & Type')

    AddPassage = Assessments(driver)
    AddPassage.Add_Eng_Module.click()

    for i in range(2):
        EasyQues = Assessments(driver)
        EasyQues.Easy_Ques.click()

    for i in range(2):
        MedQues = Assessments(driver)
        MedQues.Medium_Ques.click()

    for i in range (2):
       HardQues = Assessments(driver)
       HardQues.Hard_Ques.click()

    SavePassageModule = Assessments(driver)
    SavePassageModule.Save_Module.click()

    ##/////////////////// ADDING READ AND REPEAT MODULE ////////////////

    EnglishSearchModules = Assessments(driver)
    EnglishSearchModules.English_Search_Modules.clear()
    EnglishSearchModules.English_Search_Modules.send_keys('Read & Repeat')

    AddPassage = Assessments(driver)
    AddPassage.Add_Eng_Module.click()

    for i in range(2):
        EasyQues = Assessments(driver)
        EasyQues.Easy_Ques.click()

    for i in range(2):
        MedQues = Assessments(driver)
        MedQues.Medium_Ques.click()

    for i in range(2):
        HardQues = Assessments(driver)
        HardQues.Hard_Ques.click()

    SavePassageModule = Assessments(driver)
    SavePassageModule.Save_Module.click()

    ##/////////////////// ADDING LISTEN AND REPEAT MODULE ////////////////

    EnglishSearchModules = Assessments(driver)
    EnglishSearchModules.English_Search_Modules.clear()
    EnglishSearchModules.English_Search_Modules.send_keys('Listen & Repeat')

    AddPassage = Assessments(driver)
    AddPassage.Add_Eng_Module.click()

    for i in range(2):
        EasyQues = Assessments(driver)
        EasyQues.Easy_Ques.click()

    for i in range(2):
        MedQues = Assessments(driver)
        MedQues.Medium_Ques.click()

    for i in range(2):
        HardQues = Assessments(driver)
        HardQues.Hard_Ques.click()

    SavePassageModule = Assessments(driver)
    SavePassageModule.Save_Module.click()

    ##/////////////////// ADDING JUMBLED WORDS MODULE ////////////////

    EnglishSearchModules = Assessments(driver)
    EnglishSearchModules.English_Search_Modules.clear()
    EnglishSearchModules.English_Search_Modules.send_keys('Jumbled Words')

    AddPassage = Assessments(driver)
    AddPassage.Add_Eng_Module.click()

    for i in range(2):
        EasyQues = Assessments(driver)
        EasyQues.Easy_Ques.click()

    for i in range(2):
        MedQues = Assessments(driver)
        MedQues.Medium_Ques.click()

    for i in range(2):
        HardQues = Assessments(driver)
        HardQues.Hard_Ques.click()

    SavePassageModule = Assessments(driver)
    SavePassageModule.Save_Module.click()

    ##/////////////////// ADDING FILL IN MISSING PHRASES MODULE ////////////////

    EnglishSearchModules = Assessments(driver)
    EnglishSearchModules.English_Search_Modules.clear()
    EnglishSearchModules.English_Search_Modules.send_keys('Fill in the Missing Phrase')

    AddPassage = Assessments(driver)
    AddPassage.Add_Eng_Module.click()

    for i in range(2):
        PassageEasyQues = Assessments(driver)
        PassageEasyQues.Easy_Ques.click()

    for i in range(2):
        PassageMedQues = Assessments(driver)
        PassageMedQues.Medium_Ques.click()

    for i in range(2):
        EIHardQues = Assessments(driver)
        EIHardQues.Hard_Ques.click()

    SavePassageModule = Assessments(driver)
    SavePassageModule.Save_Module.click()

    ##/////////////////// ADDING PARAGRAPH WRITING MODULE ////////////////

    EnglishSearchModules = Assessments(driver)
    EnglishSearchModules.English_Search_Modules.clear()
    EnglishSearchModules.English_Search_Modules.send_keys('Paragraph Writing')

    AddPassage = Assessments(driver)
    AddPassage.Add_Eng_Module.click()

    Topic = Assessments(driver)
    Topic.Para_Writing_Topic.send_keys('Dog')

    AddTopic = Assessments(driver)
    AddTopic.Add_Eng_Module.click()

    SaveTopic = Assessments(driver)
    SaveTopic.Save_Para_Topic.click()

    ##/////////////////// ADDING FREE SPEECH MODULE ////////////////

    EnglishSearchModules = Assessments(driver)
    EnglishSearchModules.English_Search_Modules.clear()
    EnglishSearchModules.English_Search_Modules.send_keys('Free Speech')

    AddPassage = Assessments(driver)
    AddPassage.Add_Eng_Module.click()

    for i in range(2):
        EasyQues = Assessments(driver)
        EasyQues.Easy_Ques.click()

    for i in range(2):
        MedQues = Assessments(driver)
        MedQues.Medium_Ques.click()

    for i in range(2):
        HardQues = Assessments(driver)
        HardQues.Hard_Ques.click()

    for i in range(3):
        CustomQues = Assessments(driver)
        CustomQues.Free_Speech_Custom_Ques.click()

    CustomQues1Add = Assessments(driver)
    CustomQues1Add.Custom_Ques1.send_keys('Tell about yourself')

    CustomQues2Add = Assessments(driver)
    CustomQues2Add.Custom_Ques2.send_keys('How many years of experience do you have?')

    CustomQues3Add = Assessments(driver)
    CustomQues3Add.Custom_Ques3.send_keys('What are your strengths?')

    SaveFreeSpeechModule = Assessments(driver)
    SaveFreeSpeechModule.Save_Module.click()


    SaveAllEngModules = Assessments(driver)
    SaveAllEngModules.Save_All_Eng_Mods.click()

    ##////////////////////// ADDING PSYCHOMETRIC ASSESSMENT //////////////////////////

    searchtab = Assessments(driver)
    searchtab.search_tab.send_keys('Automated 1002')  # CHANGE THIS ACCORDING TO JOB NAME

    selectjob = Assessments(driver)
    selectjob.select_job.click()

    CreateNewAssessment = Assessments(driver)
    CreateNewAssessment.Create_New_Assessment.click()
    time.sleep(4)

    AddPsychometric = Assessments(driver)
    AddPsychometric.Psychometric.click()

    AddSPT = Assessments(driver)
    AddSPT.Specific_Personality_Traits.click()

    PsychometricInstructions =  Assessments(driver)
    PsychometricInstructions.Psychometric_Instructions.click()

    SavePsychometric = Assessments(driver)
    SavePsychometric.Save_Psychometric.click()

    #//////////////  MULTILINGUAL ////////////////







    time.sleep(6)




