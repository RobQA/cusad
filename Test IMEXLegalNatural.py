from selenium import webdriver


from Roles import Roles
from IMEXLegalNatural import IMEXLegalNatural
from TestCase import TestCase
from TestGroup import TestGroup
from Utils import Utils


driver = webdriver.Chrome()
driver.implicitly_wait(1)
Utils.driver = driver


createRecallSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_recall_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
]

CR_REC = TestCase('CREATE_RECALL_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', createRecallSadIMForLegalSTEPS, '')

storedDeletedSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_delete_sad_im_for_legal, 'args': None},

]

ST_DEL = TestCase('STORED_DELETED_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', storedDeletedSadIMForLegalSTEPS, '')

storedGetRejectionSadIMForLegalSTEPS = [
    #{'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_getrejection_sad_im_for_legal, 'args': None},

]

ST_GR = TestCase('STORED_GET_REJECTION_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', storedGetRejectionSadIMForLegalSTEPS, '')

storedUpdateSadIMForLegalSTEPS = [
    #{'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},

]

ST_UP = TestCase('STORED_UPDATE_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', storedUpdateSadIMForLegalSTEPS, '')

storedSubmitSadIMForLegalSTEPS = [
    #{'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},

]
ST_SB = TestCase ('STORED_SUBMIT_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', storedSubmitSadIMForLegalSTEPS, '')


submittedRejectRegSadIMForLegalSTEPS = [
    #{'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.submitted_reject_registration_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]
SU_RR = TestCase ('STORED_SUBMITTED_REJECT_REGISTRATION_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', submittedRejectRegSadIMForLegalSTEPS, '')

submittedRegisterSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]
SU_REG = TestCase ('STORED_SUBMITTED_REGISTER_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', submittedRegisterSadIMForLegalSTEPS, '')

assessedRejectRegSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_REGISTRATION_REJECTOR]},
    {'func': IMEXLegalNatural.assessed_reject_registration_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
]

AS_RR = TestCase('ASSESSED_REJECT_REGISTRATION_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', assessedRejectRegSadIMForLegalSTEPS, '')


assessedReleaseRejectionSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_EXAMINER]},
    {'func': IMEXLegalNatural.assessed_release_rejection_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]

AS_RRJ = TestCase('ASSESSED_RELEASE_REJECTION_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', assessedReleaseRejectionSadIMForLegalSTEPS, '')


assessedCorrectionSaveSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},

]

AS_CR_SV = TestCase('ASSESSED_CORRECTION_SAVE_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', assessedCorrectionSaveSadIMForLegalSTEPS, '')

assessedCorrectableSubmitSadIMForLegalSTEPS = [
    #{'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},

]

AS_CR_SB = TestCase('ASSESSED_CORRECTABLE_SUBMIT_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', assessedCorrectableSubmitSadIMForLegalSTEPS, '')

assessedCorrectedRejectKDTSadIMForLegalSTEPS = [
    #{'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_corrected_reject_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
]


AS_CR_RJ = TestCase('ASSESSED_CORRECTED_REJECT_KDT_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', assessedCorrectedRejectKDTSadIMForLegalSTEPS, '')

assessedCorrectedRegisterKDTSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]

AS_CR_RG = TestCase('ASSESSED_CORRECTED_REGISTER_KDT_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', assessedCorrectedRegisterKDTSadIMForLegalSTEPS, '')

assessedAttachDocSubmitSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.assessed_attach_doc_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]

AS_AT_DC = TestCase('ASSESSED_ATTACH_DOC_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', assessedAttachDocSubmitSadIMForLegalSTEPS, '')

assessedRecallSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.assessed_attach_doc_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_recall_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]

AS_RE = TestCase('ASSESSED_RECALL_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', assessedRecallSadIMForLegalSTEPS, '')

assessedUpdateSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.assessed_attach_doc_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]

AS_UP = TestCase('ASSESSED_UPDATE_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', assessedUpdateSadIMForLegalSTEPS, '')


assessedReleaseSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.assessed_attach_doc_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_EXAMINER]},
    {'func': IMEXLegalNatural.assessed_release_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]

AS_RL = TestCase('ASSESSED_RELEASE_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', assessedReleaseSadIMForLegalSTEPS, '')

releasedAttachDocSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_EXAMINER]},
    {'func': IMEXLegalNatural.assessed_release_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.released_attach_doc_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]

RL_AT_DC = TestCase('RELEASED_ATTACH_DOC_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', releasedAttachDocSadIMForLegalSTEPS, '')

releasedUpdateSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_EXAMINER]},
    {'func': IMEXLegalNatural.assessed_release_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.released_attach_doc_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.released_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]

RL_UP = TestCase('RELEASED_UPDATE_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', releasedUpdateSadIMForLegalSTEPS, '')

releasedCorrectionSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_EXAMINER]},
    {'func': IMEXLegalNatural.assessed_release_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.released_attach_doc_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.released_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.released_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]

RL_CR = TestCase('RELEASED_CORRECTION_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', releasedCorrectionSadIMForLegalSTEPS, '')

releasedCorrectableSaveKDTSadIMForLegalSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_EXAMINER]},
    {'func': IMEXLegalNatural.assessed_release_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.released_attach_doc_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.released_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.released_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.released_correctable_save_kdt_sad_im_for_legal, 'args': None},

]

RL_KDT_SV = TestCase('RELEASED_CORRECTABLE_SAVE_KDT_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', releasedCorrectableSaveKDTSadIMForLegalSTEPS, '')

releasedCorrectableSubmitKDTSadIMForLegalSTEPS = [
    #{'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_EXAMINER]},
    {'func': IMEXLegalNatural.assessed_release_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.released_attach_doc_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.released_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.released_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.released_correctable_save_kdt_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.released_correctable_submit_kdt_sad_im_for_legal, 'args': None},


]

RL_KDT_SB = TestCase('RELEASED_CORRECTABLE_SUBMIT_KDT_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', releasedCorrectableSubmitKDTSadIMForLegalSTEPS, '')

releasedCorrectableRejectSubmitRegisterKdtRecallSadIMForLegalSTEPS = [
    #{'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.store_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_update_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.store_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.store_register_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.assessed_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_EXAMINER]},
    {'func': IMEXLegalNatural.assessed_release_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.released_attach_doc_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_SUPERVISOR]},
    {'func': IMEXLegalNatural.released_update_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.released_correction_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.released_correctable_save_kdt_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.released_correctable_submit_kdt_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.released_correctable_reject_submit_register_kdt_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_TARGETER]},
    {'func': IMEXLegalNatural.released_recall_sad_im_for_legal, 'args': None},
    {'func': IMEXLegalNatural.audit_sad_im_for_legal, 'args': None},
    {'func': Utils.logout, 'args': None},

]

RL_KDT_RJ = TestCase('RELEASED_CORRECTABLE_REJECT_SUBMIT_KDT_RECALL_SAD_IM_FOR_LEGAL_RISK_LVL_GREEN', releasedCorrectableRejectSubmitRegisterKdtRecallSadIMForLegalSTEPS, '')


createRegisterSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},

]

CR_RG = TestCase('CREATE_REGISTER_SAD_IM_FOR_LEGAL_RISK_LVL_RED', createRegisterSadIMForLegalRedLvlSTEPS, '')

selectedRejectRegistrationSadIMForLegalRedLvlSTEPS = [
    #{'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_REGISTRATION_REJECTOR]},
    {'func': IMEXLegalNatural.selected_reject_registration_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
]

SL_RJ_RG = TestCase('SELECTED_REJECT_REGISTRATION_SAD_IM_FOR_LEGAL_RISK_LVL_RED', selectedRejectRegistrationSadIMForLegalRedLvlSTEPS, '')

selectedRejectionSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_TARGETER]},
    {'func': IMEXLegalNatural.selected_rejection_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},

]

SL_RJ = TestCase('SELECTED_REJECTION_SAD_IM_FOR_LEGAL_RISK_LVL_RED', selectedRejectionSadIMForLegalRedLvlSTEPS, '')

selectedCorrectionSaveSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.selected_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},

]

SL_CR_SV = TestCase('SELECTED_CORRECTION_SAVE_SAD_IM_FOR_LEGAL_RISK_LVL_RED', selectedCorrectionSaveSadIMForLegalRedLvlSTEPS, '')

selectedCorrectableSubmitSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.selected_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.selected_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},

]

SL_CR_SB = TestCase('SELECTED_CORRECTABLE_SUBMIT_SAD_IM_FOR_LEGAL_RISK_LVL_RED', selectedCorrectableSubmitSadIMForLegalRedLvlSTEPS, '')

selectedCorrectedRejectKdtSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.selected_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.selected_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_corrected_reject_kdt_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},

]

SL_CR_RJ = TestCase('SELECTED_CORRECTED_REJECT_KDT_SAD_IM_FOR_LEGAL_RISK_LVL_RED', selectedCorrectedRejectKdtSadIMForLegalRedLvlSTEPS, '')

selectedCorrectedRegisterKdtSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.selected_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.selected_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_corrected_register_kdt_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},

]

SL_CR_RG = TestCase('SELECTED_CORRECTED_REGISTER_KDT_SAD_IM_FOR_LEGAL_RISK_LVL_RED', selectedCorrectedRegisterKdtSadIMForLegalRedLvlSTEPS, '')

selectedAttachDocSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.selected_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.selected_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_corrected_register_kdt_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.selected_attach_doc_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},

]

SL_AT_DC = TestCase('SELECTED_ATTACH_DOC_SAD_IM_FOR_LEGAL_RISK_LVL_RED', selectedAttachDocSadIMForLegalRedLvlSTEPS, '')

selectedContinueSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.selected_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.selected_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_corrected_register_kdt_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.selected_attach_doc_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_TARGETER]},
    {'func': IMEXLegalNatural.selected_continue_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},

]

SL_CT = TestCase('SELECTED_CONTINUE_SAD_IM_FOR_LEGAL_RISK_LVL_RED', selectedContinueSadIMForLegalRedLvlSTEPS, '')

assessedRejectRegSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.selected_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.selected_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_corrected_register_kdt_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_TARGETER]},
    {'func': IMEXLegalNatural.selected_continue_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.assessed_attach_doc_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_REGISTRATION_REJECTOR]},
    {'func': IMEXLegalNatural.assessed_reject_registration_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None}
]

AS_RR_RED = TestCase('ASSESSED_REJECT_REGISTRATION_SAD_IM_FOR_LEGAL_RISK_LVL_RED', assessedRejectRegSadIMForLegalRedLvlSTEPS, '')

assessedReleaseRejectionSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.selected_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.selected_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_corrected_register_kdt_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_TARGETER]},
    {'func': IMEXLegalNatural.selected_continue_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.assessed_attach_doc_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_EXAMINER]},
    {'func': IMEXLegalNatural.assessed_release_rejection_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},

]

AS_RRJ_RED = TestCase('ASSESSED_RELEASE_REJECTION_SAD_IM_FOR_LEGAL_RISK_LVL_RED', assessedReleaseRejectionSadIMForLegalRedLvlSTEPS, '')

assessedCorrectionSaveSubmitRejectSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.selected_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.selected_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_corrected_register_kdt_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_TARGETER]},
    {'func': IMEXLegalNatural.selected_continue_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.assessed_attach_doc_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_reject_kdt_sad_im_for_legal, 'args': None}, #FOR RED LVL
    {'func': Utils.logout, 'args': None},

]

AS_CR_SV_RED = TestCase('ASSESSED_CORRECTION_SAVE_SUBMIT_REJECT_SAD_IM_FOR_LEGAL_RISK_LVL_RED', assessedCorrectionSaveSubmitRejectSadIMForLegalRedLvlSTEPS, '')

assessedCorrectedRegisterKDTRecallAuditSadIMForLegalRedLvlSTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': IMEXLegalNatural.create_register_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.selected_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.selected_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.selected_corrected_register_kdt_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_TARGETER]},
    {'func': IMEXLegalNatural.selected_continue_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_ATTACHMENT]},
    {'func': IMEXLegalNatural.assessed_attach_doc_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_correction_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_DECLARANT]},
    {'func': IMEXLegalNatural.assessed_correction_save_sad_im_for_legal_red_lvl, 'args': None},
    {'func': IMEXLegalNatural.assessed_correctable_submit_sad_im_for_legal_red_lvl, 'args': None},
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_OFFICER]},
    {'func': IMEXLegalNatural.assessed_corrected_register_kdt_sad_im_for_legal, 'args': None}, #FOR RED LVL,
    {'func': Utils.logout, 'args': None},
    {'func': Utils.login, 'args': [Roles.CUSAD_TARGETER]},
    {'func': IMEXLegalNatural.assessed_recall_sad_im_for_legal, 'args': None}, #FOR RED LVL
    {'func': IMEXLegalNatural.audit_sad_im_for_legal, 'args': None}, #FOR RED LVL

]

AS_CR_RG_RED = TestCase('ASSESSED_CORRECTED_REGISTER_KDT_RECALL_AUDIT_SAD_IM_FOR_LEGAL_RISK_LVL_RED', assessedCorrectedRegisterKDTRecallAuditSadIMForLegalRedLvlSTEPS, '')




TestGroup('TEST', [CR_REC, ST_DEL, ST_GR, ST_UP, ST_SB, SU_RR, SU_REG, AS_RR, AS_RRJ, AS_CR_SV ,AS_CR_SB, AS_CR_RJ, AS_CR_RG, AS_AT_DC, AS_RE, AS_UP, AS_RL, RL_AT_DC, RL_UP, RL_CR, RL_KDT_SV, RL_KDT_SB,RL_KDT_RJ, CR_RG, SL_RJ_RG, SL_RJ, SL_CR_SV, SL_CR_SB, SL_CR_RJ, SL_CR_RG, SL_AT_DC, SL_CT, AS_RR_RED, AS_RRJ_RED, AS_CR_SV_RED, AS_CR_RG_RED])
#TestGroup('TEST', [RL_KDT_RJ])