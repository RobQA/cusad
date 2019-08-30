from selenium.webdriver.chrome.webdriver import WebDriver
import time


class Utils:
    driver = None

    @staticmethod
    def fill_form(dict):
        for key, value in dict.items():  # вернуть копию из списка словарей
            if value is None:
                Utils.driver.find_element_by_id(key).click()
            else:
                Utils.driver.find_element_by_id(key).send_keys(value)


    ########################################################################################

    @staticmethod
    def login(user):
        driver = Utils.driver
        driver.get(
            "https://uatapp3.fipsoft.com/cas//login?service=https%3A%2F%2Fuatapp3.fipsoft.com%2Fcusad%2Flogin%2Fcas")
        driver.find_element_by_id('username').send_keys(user['username'])
        driver.find_element_by_id('password').send_keys(user['password'])
        driver.find_element_by_name('submit').click()

    @staticmethod
    def login1(user):
        driver = Utils.driver
        driver.get(
            "https://uatapp3.fipsoft.com/cas//login?service=https%3A%2F%2Fuatapp3.fipsoft.com%2Fcusad%2Flogin%2Fcas")
        time.sleep(1)
        driver.find_element_by_id('username').send_keys(user['username'])
        time.sleep(1)
        driver.find_element_by_id('password').send_keys(user['password'])
        time.sleep(1)
        driver.find_element_by_name('submit').click()



    ########################################################################################

    @staticmethod
    def close_browser():
        Utils.driver.close()

    @staticmethod
    def check_select(selectId, optionNumber):
        driver = Utils.driver
        element = driver.find_element_by_id(selectId)
        all_options = element.find_elements_by_tag_name("option")
        all_options[optionNumber].click()

    ########################################################################################

    @staticmethod
    def set_date(elemId, date):
        driver = Utils.driver
        driver.execute_script("document.getElementById('" + elemId + "').value = '" + date + "'")

    ########################################################################################

    @staticmethod
    def check_box(elemId, check):
        driver = Utils.driver
        driver.execute_script("$(#" + elemId + ").prop('checked', false)")

    ########################################################################################

    @staticmethod
    def wait_for_ajax_complete(driver):
        return 0 == driver.execute_script("return $ && $.active")

    ########################################################################################

    @staticmethod
    def logout():
        driver = Utils.driver
        driver.find_element_by_class_name('scp-profile-dropdown-button').click()
        driver.find_element_by_class_name('glyphicon-log-out').click()

