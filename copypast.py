import time
from selenium.webdriver.support.wait import WebDriverWait
import random
from selenium.webdriver.common.keys import Keys
from Utils import Utils


class copypast:

    @staticmethod
    def copy():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationUpdateAssessedClass').click()
        time.sleep(1)
        element1 = driver.find_element_by_id('goodsShipments[0].mainContractTerms.dealNatureCode')
        element2 = driver.find_element_by_id('goodsShipments[0].mainContractTerms.dealFeatureCode')
        time.sleep(1)
        element1.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        element1.send_keys(Keys.CONTROL, 'c')
        time.sleep(1)
        element2.send_keys(Keys.CONTROL, 'v')

copySTEPS = [
    {'func': Utils.login, 'args': [Roles.CUSAD]},
    {'func': copypast.copy, 'args': None},

]

C = TestCase('copy', copySTEPS, ''),