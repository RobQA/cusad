from selenium import webdriver


from Roles import Roles
from TestCase import TestCase
from TestGroup import TestGroup
from Utils import Utils
from suspense53_31 import suspense53_31

driver = webdriver.Chrome()
driver.implicitly_wait(1)
Utils.driver = driver

suspense53_31STEPS = [
    {'func': Utils.login1, 'args': [Roles.CUSAD]},
    {'func': suspense53_31.suspens_im_53, 'args': None},
    {'func': suspense53_31.suspens_ex_31, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

CUSAD = TestCase('SUSPENSE_53_31', suspense53_31STEPS, '')

TestGroup('TEST_CROUP_EXTERNAL_ROLL', [CUSAD])