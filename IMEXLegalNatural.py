from Utils import Utils
from selenium.webdriver.support.wait import WebDriverWait
import random
import time






                                    #RISK LEVL GREEN (SAD for Legal Entitity - IMPORT)

Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN = []
Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN.append({'tin1': '17031994', 'tin2': '17031994', 'tin3': '17031994', 'tin4': '17031994'})
Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN.append({'tin1': '02268813', 'tin2': '02268813', 'tin3': '02268813', 'tin4': '02268813'})
Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN.append({'tin1': '02610385', 'tin2': '02610385', 'tin3': '02610385', 'tin4': '02610385'})
Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN.append({'tin1': '02539726', 'tin2': '02539726', 'tin3': '02539726', 'tin4': '02539726'})
Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN.append({'tin1': '01237297', 'tin2': '01237297', 'tin3': '01237297', 'tin4': '01237297'})
Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN.append({'tin1': '00885389', 'tin2': '00885389', 'tin3': '00885389', 'tin4': '00885389'})
Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN.append({'tin1': 'AA3784582', 'tin2': 'AA3784582', 'tin3': 'AA3784582', 'tin4': 'AA3784582'})
Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN.append({'tin1': 'AA3784595', 'tin2': 'AA3784595', 'tin3': 'AA3784595', 'tin4': 'AA3784595'})
Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN.append({'tin1': 'AA3784579', 'tin2': 'AA3784579', 'tin3': 'AA3784579', 'tin4': 'AA3784579'})
Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN.append({'tin1': 'AA3784588', 'tin2': 'AA3784588', 'tin3': 'AA3784588', 'tin4': 'AA3784588'})


class IMEXLegalNatural:

    procedure_code = ['51', '70', '77', '78', '91', '93', '94', '96']
    rate = ['USD', 'EUR', 'RUS', 'AMD', 'TJS']
    trading_country = ['CF', 'RU', 'AM', 'GR', 'MG', 'MH', 'RW', 'HK']
    departure_country = ['CV', 'VW', 'GB', 'GD', 'GE', 'GS', 'FK', 'FM']
    createRecallSadImForLegalGeneralFormData = {
        "customsModeCode": procedure_code[random.randint(0, len(procedure_code)-1)],
        "regCustomsOffices[0].code": "05100010",
        "goodsShipments[0].specificationNumber": "11111",
        "goodsShipments[0].specificationListNumber": "11111",
        "declarationKindCode": "ЗПК",
        "goodsShipments[0].mainContractTerms.tradeCountryCode": trading_country[random.randint(0, len(trading_country)-1)],
        "goodsShipments[0].consigment.dispatchCountryCode": departure_country[random.randint(0, len(departure_country)-1)],
        "goodsShipments[0].mainContractTerms.totalInvoiceAmount": "1",
        'goodsShipments[0].mainContractTerms.contractCurrencyCode': rate[random.randint(0, len(rate)-1)],
        'goodsShipments[0].mainContractTerms.dealNatureCode': '545',
        'goodsShipments[0].mainContractTerms.dealFeatureCode': '56',
    }

    @staticmethod
    def createRecallSadImForLegalPartiesFormData(obj):
        return {
            'goodsShipments[0].consignor.organizationName': 'ValUe777',
            'goodsShipments[0].consignor.address.postalCode': 'ValUe777',
            'goodsShipments[0].consignor.address.countryCode': 'AM',
            'goodsShipments[0].consignor.address.region': 'ValUe777',
            'goodsShipments[0].consignor.address.city': 'ValUe777',
            'goodsShipments[0].consignor.address.streetHouse': 'ValUe777',
            'goodsShipments[0].consignee.raOrganizationFeatures.unn': obj['tin1'],
            'goodsShipments[0].finRespPerson.raOrganizationFeatures.unn': obj['tin2'],
            'goodsShipments[0].declarant.raOrganizationFeatures.unn': obj['tin3'],
            'filledPersons[0].unn': obj['tin4'],
            'null.goodsLocTransportAccordion': None,
            'addPhoneButton': None,
            'filledPersons[0].contact.phones[1].number': '+375345345'
    }

    delivery_terms = ['CIP', 'DAP', 'FGV', 'FAS', 'XXX', 'KKK', 'FOB', 'DAT']
    createRecallSadImForLegalTransportationFormData = {
        'goodsShipments[0].mainContractTerms.deliveryTerms.deliveryTermsStringCode': delivery_terms[random.randint(0, len(delivery_terms)-1)],
        'goodsShipments[0].mainContractTerms.deliveryTerms.deliveryPlace': 'ValUe777',
        'goodsShipments[0].consigment.departureArrivalTransport.transportModeCode': '31',
        'goodsShipments[0].consigment.borderTransport.transportModeCode': '31',
        'goodsShipments[0].goodsLocation[0].informationTypeCode': '21',
        'goodsShipments[0].goodsLocation[0].customsOfficeCode': '05100017',
        'goodsShipments[0].goodsLocation[0].goodsLocationPlace.numberCustomsZoneCode': 'MP00013',
        'goodsShipments[0].goodsLocation[0].locationName': 'ValUe777'
    }


    createRecallSadImForLegalGoodsFormData = {
        'goodFeatures': 'МПО',
        'goodsTNVEDCode': '85182930010',
        'intellectPropertySign': 'И',
        'goodsAddTNVEDCode': '0001',
        'additionalSign': 'С',
        'goodsClassificationCode': 'М',
        'originCountryCode': trading_country[random.randint(0, len(trading_country)-1)],
        'grossWeightQuantity': '1',
        'netWeightQuantity': '1',
        'netWeightQuantity2': '1',
        'customsProcedure.precedingCustomsModeCode': '00',
        'customsProcedure.goodsTransferFeatureCode': '000',
        'supplemGoodsQuantity.goodsQuantity': '1',
        'invoicedCost': '1',
        'customsCostCorrectMethodCode': '0',
        'goodsDsc': 'ValUe5ValUe5ValUe5ValUe5ValUe5ValUe5',
        'goodsDscRu': 'ValUe5ValUe5ValUe5ValUe5ValUe5ValUe5',
        #'container.containerKindCode': '1A',
        'cimIdDetails.cimMarkingFlagCode': 'ПВ',
        'saveItem': None,
    }

    createRecallSadImForLegalApportionmentFormData = {
        'goodsShipments[0].valuation.transportChargesTaxBase': '100',
        'goodsShipments[0].valuation.insuranceChargesTaxBase': '1000000',
        'goodsShipments[0].valuation.otherChargesTaxBase': '999999999',
        'goodsShipments[0].valuation.unionTransportChargesTaxBase': '9999999',
        'goodsShipments[0].valuation.deductionsTaxBase': '0,34',
        'goodsShipments[0].valuation.transportChargesCurrencyCode': 'AMD',
        'goodsShipments[0].valuation.insuranceChargesCurrencyCode': 'USD',
        'goodsShipments[0].valuation.otherChargesCurrencyCode': 'EUR',
        'goodsShipments[0].valuation.unionTransportChargesCurrencyCode': 'BYR',
        'goodsShipments[0].valuation.deductionsCurrencyCode': 'BRL'

    }

    createRecallSadImForLegalDocumentsFormData = {
        'fakePresentedDocuments[0].presentedDocumentModeCode': '460',
        'fakePresentedDocuments[0].providingIndicationMark': '0',
        'fakePresentedDocuments[0].prDocumentNumber': '777777',
        #'fakePresentedDocuments[0].goodsNumbers': '1'
    }

    createRecallSadImForLegalDocuments10017FormData = {
        'fakePresentedDocuments[1].presentedDocumentModeCode': '10017',
    }

    createRecallSadImForLegalDocuments10042FormData = {
        'fakePresentedDocuments[2].presentedDocumentModeCode': '10042',
    }

    createRecallSadImForLegalCustomsFeeFormData = {
        'otherPayment.providedForm.quantity': '999',
        'otherPayment.escortDistance': '99999',
        'otherPayment.transportControlFee': '99999999',
    }

    @staticmethod
    def create_recall_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get('https://uatapp3.fipsoft.com/cusad/sad/create?customsProcedure=IM&iff=I')
        Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalGeneralFormData)
        driver.find_element_by_partial_link_text('Стороны').click()
        time.sleep(1)
        rInt = random.randint(0, len(Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN) - 1)
        Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalPartiesFormData(Consignee_FinancialSettlement_DeclarationCompletion_DeclarationCompletion_TIN[rInt]))
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, 0 );")
        driver.find_element_by_partial_link_text('Перевозка').click()
        time.sleep(1)
        Utils.check_select('goodsShipments[0].consigment.containerIndicator', 2)
        Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalTransportationFormData)
        driver.execute_script("window.scrollTo( 0, 0 );")
        driver.find_element_by_partial_link_text('Товары').click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        time.sleep(1)
        Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalGoodsFormData)
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распределение').click()
        Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalApportionmentFormData)
        Utils.check_select('goodsShipments[0].valuation.transportChargesApportionmentType', 1)
        Utils.check_select('goodsShipments[0].valuation.insuranceChargesApportionmentType', 2)
        Utils.check_select('goodsShipments[0].valuation.otherChargesApportionmentType', 1)
        Utils.check_select('goodsShipments[0].valuation.unionTransportChargesApportionmentType', 2)
        Utils.check_select('goodsShipments[0].valuation.deductionsApportionmentType', 1)
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord").click()
        #driver.find_element_by_css_selector("#fakePresentedDocuments thead tr:first-child a").click()
        Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalDocumentsFormData)
        Utils.set_date('fakePresentedDocuments[0].prDocumentDate', '17/01/2018')
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord").click()
        Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalDocuments10017FormData)
        Utils.set_date('fakePresentedDocuments[1].temporaryStorageImportDate', '17/01/2020')
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord").click()
        Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalDocuments10042FormData)
        Utils.set_date('fakePresentedDocuments[2].temporaryStorageImportDate', '17/01/2020')
        Utils.driver.find_element_by_id('fakePresentedDocuments[2].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Иные платежи').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#toBePaidTable .tlpinput").click()
        Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalCustomsFeeFormData)
        Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationStore').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('cancel').click()
        time.sleep(1)
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        element = driver.find_element_by_css_selector("#searchRes .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.switch_to_window(driver.window_handles[0])   #Close tab browser
        driver.close()                                      #Close tab browser
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationSubmitStored').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        element = driver.find_element_by_css_selector("#searchRes .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.switch_to_window(driver.window_handles[0])  # Close tab browser
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_class_name('cancel').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationRegisterSubmitted').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        #driver.find_element_by_class_name('glyphicon-print').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Платежи').click()
        driver.find_element_by_class_name('glyphicon-print').click()
        driver.find_element_by_partial_link_text('Оплата').click()
        driver.switch_to_window(driver.window_handles[0])  # Close tab browser
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationPayFromOverpaymentClass').click()
        Utils.driver.find_element_by_id('overPayments[0].amountToUse').send_keys('9999999999999')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#obligationsTable .createdColor .glyphicon-pencil").click()
        driver.find_element_by_class_name('operationPayFromOverpaymentClass').click()
        Utils.driver.find_element_by_id('overPayments[0].amountToUse').send_keys('9999999999999')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        driver.find_element_by_css_selector("#obligationsTable tbody tr:first-child td:nth-child(8) a").click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationReleaseAssessedClass').click()
        driver.switch_to_window(driver.window_handles[0])  # Close tab browser
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        Utils.driver.find_element_by_id('operationReleaseAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationRecallReleasedClass').click()
        driver.switch_to_window(driver.window_handles[0])  # Close tab browser
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        Utils.driver.find_element_by_id('operationRecallReleased').click()
        time.sleep(2)
        Utils.driver.find_element_by_id('userNote').send_keys('dfdfadfa')
        Utils.driver.find_element_by_id('operationRecallReleased').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)








    ############################################################################################################################################################


    storeSadImForLegalGeneralFormData = {
        'customsModeCode': '40',
        'regCustomsOffices[0].code': '05100010',

    }

    storeSadImForLegalPartieslFormData = {
        'goodsShipments[0].consignee.raOrganizationFeatures.unn': '17031994',
        'goodsShipments[0].declarant.raOrganizationFeatures.unn': '17031994'
    }

    @staticmethod
    def store_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get('https://uatapp3.fipsoft.com/cusad/sad/create?customsProcedure=IM&iff=I')
        Utils.fill_form(IMEXLegalNatural.storeSadImForLegalGeneralFormData)
        driver.find_element_by_partial_link_text('Стороны').click()
        Utils.fill_form(IMEXLegalNatural.storeSadImForLegalPartieslFormData)
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, 0 );")
        Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationStore').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('cancel').click()


    ############################################################################################################################################################


    storedDeleteSadImForLegalFormData = {

    }

    @staticmethod
    def store_delete_sad_im_for_legal():
        driver = Utils.driver
        #driver.switch_to.window(driver.window_handles[5])
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('delete').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ############################################################################################################################################################


    storedGetRejectionSadImForLegalFormData = {

    }

    @staticmethod
    def store_getrejection_sad_im_for_legal():
        driver = Utils.driver
        #driver.switch_to.window(driver.window_handles[5])
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('operationGetRejection').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.find_element_by_class_name('btn').click()
        time.sleep(1)
        driver.find_element_by_class_name('cancel').click()
        driver.find_element_by_partial_link_text("Скачать").click()
        driver.find_element_by_partial_link_text("Аудит").click()
        element = driver.find_element_by_css_selector(".tableNoWrap .revisionsDiffLink")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.find_element_by_css_selector(".lcp-table-fixed .fieldMessage").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text("Аудит").click()
        time.sleep(1)
        driver.find_element_by_class_name('operationLink').click()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    ############################################################################################################################################################
    

    createUpdateSadImForLegalGeneralFormData = {
        "goodsShipments[0].specificationNumber": "1234",
        "goodsShipments[0].specificationListNumber": "12345",
        "declarationKindCode": "ВДТ",
        "goodsShipments[0].mainContractTerms.tradeCountryCode": "AE",
        "goodsShipments[0].consigment.dispatchCountryCode": "BG",
        "goodsShipments[0].mainContractTerms.totalInvoiceAmount": "1",
        'goodsShipments[0].mainContractTerms.contractCurrencyCode': 'AMD',
        'goodsShipments[0].mainContractTerms.dealNatureCode': '545',
        'goodsShipments[0].mainContractTerms.dealFeatureCode': '56',

    }

    createUpdateSadImForLegalPartiesFormData = {
        'goodsShipments[0].consignor.organizationName': '1',
        'goodsShipments[0].consignor.address.postalCode': '1',
        'goodsShipments[0].consignor.address.countryCode': 'AM',
        'goodsShipments[0].consignor.address.region': '3425',
        'goodsShipments[0].consignor.address.city': '235',
        'goodsShipments[0].consignor.address.streetHouse': '2134',
    }

    createUpdateSadImForLegalTransportationFormData = {
        'goodsShipments[0].mainContractTerms.deliveryTerms.deliveryTermsStringCode': 'CIF',
        'goodsShipments[0].mainContractTerms.deliveryTerms.deliveryPlace': '12341',
        'goodsShipments[0].consigment.departureArrivalTransport.transportModeCode': '31',
        'goodsShipments[0].consigment.borderTransport.transportModeCode': '31',
        'goodsShipments[0].goodsLocation[0].informationTypeCode': '21',
        'goodsShipments[0].goodsLocation[0].customsOfficeCode': '05100017',
        'goodsShipments[0].goodsLocation[0].goodsLocationPlace.numberCustomsZoneCode': 'MP00013',
        'goodsShipments[0].goodsLocation[0].locationName': '2345234'
    }

    createUpdateSadImForLegalGoodsFormData = {
        'goodFeatures': 'МПО',
        'goodsTNVEDCode': '85182930010',
        'intellectPropertySign': 'И',
        'goodsAddTNVEDCode': '0001',
        'additionalSign': 'С',
        'goodsClassificationCode': 'М',
        'originCountryCode': 'AM',
        'grossWeightQuantity': '1',
        'netWeightQuantity': '1',
        'netWeightQuantity2': '1',
        'customsProcedure.precedingCustomsModeCode': '00',
        'customsProcedure.goodsTransferFeatureCode': '000',
        'supplemGoodsQuantity.goodsQuantity': '1',
        'invoicedCost': '1',
        'customsCostCorrectMethodCode': '0',
        'goodsDsc': 'fasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfsadfasdfas',
        'goodsDscRu': 'dfASDadasdASDasdASDSDASDAadsfsdfsd',
        # 'container.containerKindCode': '1A',
        'cimIdDetails.cimMarkingFlagCode': 'ПВ',
        'saveItem': None,
    }

    createUpdateSadImForLegalApportionmentFormData = {
        'goodsShipments[0].valuation.transportChargesTaxBase': '100',
        'goodsShipments[0].valuation.insuranceChargesTaxBase': '1000000',
        'goodsShipments[0].valuation.otherChargesTaxBase': '999999999',
        'goodsShipments[0].valuation.unionTransportChargesTaxBase': '9999999',
        'goodsShipments[0].valuation.deductionsTaxBase': '0,34',
        'goodsShipments[0].valuation.transportChargesCurrencyCode': 'AMD',
        'goodsShipments[0].valuation.insuranceChargesCurrencyCode': 'USD',
        'goodsShipments[0].valuation.otherChargesCurrencyCode': 'EUR',
        'goodsShipments[0].valuation.unionTransportChargesCurrencyCode': 'BYR',
        'goodsShipments[0].valuation.deductionsCurrencyCode': 'BRL'

    }

    createUpdateSadImForLegalDocumentsFormData = {
        'fakePresentedDocuments[0].presentedDocumentModeCode': '460',
        'fakePresentedDocuments[0].providingIndicationMark': '0',
        'fakePresentedDocuments[0].prDocumentNumber': '123412',
        # 'fakePresentedDocuments[0].goodsNumbers': '1'
    }

    createUpdateSadImForLegalCustomsFeeFormData = {
        'otherPayment.providedForm.quantity': '999',
        'otherPayment.escortDistance': '99999',
        'otherPayment.transportControlFee': '99999999',
        'operationUpdateStored': None
    }

    @staticmethod
    def store_update_sad_im_for_legal():
        driver = Utils.driver
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        element = driver.find_element_by_css_selector("#searchRes .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        Utils.fill_form(IMEXLegalNatural.createUpdateSadImForLegalGeneralFormData)
        driver.find_element_by_partial_link_text('Стороны').click()
        Utils.fill_form(IMEXLegalNatural.createUpdateSadImForLegalPartiesFormData)
        Utils.driver.find_element_by_id('goodsShipments[0].finRespPerson.raOrganizationFeatures.unn').send_keys('17031994')
        time.sleep(1)
        driver.find_element_by_partial_link_text('Перевозка').click()
        time.sleep(1)
        Utils.check_select('goodsShipments[0].consigment.containerIndicator', 2)
        Utils.fill_form(IMEXLegalNatural.createUpdateSadImForLegalTransportationFormData)
        driver.execute_script("window.scrollTo( 0, 0 );")
        time.sleep(2)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Должен быть хотя бы один товар').click()
        #element = driver.find_element_by_css_selector(".documentTabs .itemsTab")
        #driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.createUpdateSadImForLegalGoodsFormData)
        time.sleep(2)
        driver.find_element_by_partial_link_text('Распределение').click()
        Utils.fill_form(IMEXLegalNatural.createUpdateSadImForLegalApportionmentFormData)
        Utils.check_select('goodsShipments[0].valuation.transportChargesApportionmentType', 1)
        Utils.check_select('goodsShipments[0].valuation.insuranceChargesApportionmentType', 2)
        Utils.check_select('goodsShipments[0].valuation.otherChargesApportionmentType', 1)
        Utils.check_select('goodsShipments[0].valuation.unionTransportChargesApportionmentType', 2)
        Utils.check_select('goodsShipments[0].valuation.deductionsApportionmentType', 1)
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord").click()
        # driver.find_element_by_css_selector("#fakePresentedDocuments thead tr:first-child a").click()
        Utils.fill_form(IMEXLegalNatural.createUpdateSadImForLegalDocumentsFormData)
        Utils.set_date('fakePresentedDocuments[0].prDocumentDate', '17/01/2018')
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Иные платежи').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#toBePaidTable .tlpinput").click()
        Utils.fill_form(IMEXLegalNatural.createUpdateSadImForLegalCustomsFeeFormData)
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()

    ############################################################################################################################################################

    @staticmethod
    def store_submit_sad_im_for_legal():
        driver = Utils.driver
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        Utils.driver.find_element_by_id('operationSubmitStored').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_partial_link_text('Загрузить').click()
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()

    ############################################################################################################################################################

    submittedRejectRegistrationSadImForLegalApportionmentFormData = {
        'userNote': '948A2975L35H5936',
        'tdcDocCode': '01021',
    }

    @staticmethod
    def submitted_reject_registration_sad_im_for_legal():
        driver = Utils.driver
        #driver.switch_to.window(driver.window_handles[10])
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_partial_link_text('Заметки').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('userNote').send_keys('523452')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationRejectSubmitted').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def store_register_sad_im_for_legal():
        driver = Utils.driver
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        element = driver.find_element_by_css_selector("#searchRes .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        Utils.driver.find_element_by_id('operationRegisterSubmitted').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)


    ########################################################################################################################################

    @staticmethod
    def assessed_reject_registration_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        #driver.find_element_by_class_name('glyphicon-eye-open').click()
        #time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        #driver.find_element_by_class_name('operationRejectRegistrationAssessedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationRejectRegistrationAssessed').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        Utils.driver.find_element_by_id('operationRejectRegistrationAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    assessedReleaseRejectionAttachTDCSadImForLegalDocumentsFormData = {
        'tdcAccessKey': '726A2357A39C3187',
        'tdcDocCode': '09015',
        'tdcDescription': 'r',
        'tdcDocumentNumber': 'r',
        'searchByMoreOptions': None
    }

    @staticmethod
    def assessed_release_rejection_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationRejectAssessedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_class_name('tdcCollapseAccordion').click()
        time.sleep(1)
        Utils.fill_form(IMEXLegalNatural.assessedReleaseRejectionAttachTDCSadImForLegalDocumentsFormData)
        Utils.driver.find_element_by_id('searchByMoreOptions').click()  ##########
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable #checkAllArchiveDocs").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('addTdcDocuments').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationRejectAssessed').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        Utils.driver.find_element_by_id('operationRejectAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)


    ########################################################################################################################################

    @staticmethod
    def assessed_correction_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationKdtAssessedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        Utils.driver.find_element_by_id('operationKdtAssessed').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        Utils.driver.find_element_by_id('operationKdtAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()

        ########################################################################################################################################

    assessedCorrectionSaveAttachTDCSadImForLegalDocumentsFormData = {
        'tdcAccessKey': '328C0632O78Z2837',
        'tdcDocCode': '01017',
        'tdcDescription': '123',
        'tdcDocumentNumber': '123',
        'searchByMoreOptions': None
    }

    assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData = {
        'goodFeatures': 'МПО',
        'goodsTNVEDCode': '85182930010',
        'intellectPropertySign': 'И',
        'goodsAddTNVEDCode': '0001',
        'additionalSign': 'С',
        'goodsClassificationCode': 'М',
        'originCountryCode': 'AM',
        'grossWeightQuantity': '1',
        'netWeightQuantity': '1',
        'netWeightQuantity2': '1',
        'customsProcedure.precedingCustomsModeCode': '00',
        'customsProcedure.goodsTransferFeatureCode': '000',
        'supplemGoodsQuantity.goodsQuantity': '1',
        'invoicedCost': '1',
        'customsCostCorrectMethodCode': '0',
        'customsCostCorrectMethod2Code': '0',
        'goodsDsc': 'fasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfsadfasdfas',
        'goodsDscRu': 'dfASDadasdASDasdASDSDASDAadsfsdfsd',
        # 'container.containerKindCode': '1A',
        'cimIdDetails.cimMarkingFlagCode': 'ПВ',
        'saveItem': None,
    }

    assessedCorrectionSaveAttach460DocSadImForLegalDocumentsFormData = {
        'fakePresentedDocuments[12].presentedDocumentModeCode': '460',
        'fakePresentedDocuments[12].providingIndicationMark': '0',
        'fakePresentedDocuments[12].prDocumentNumber': '123412',
        # 'fakePresentedDocuments[0].goodsNumbers': '1'
    }

    @staticmethod
    def assessed_correction_save_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Товары').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#goodsShipmentsGoods .glyphicon-pencil").click()
        Utils.driver.find_element_by_id('gdcItmChangeCode.basisCompilationCode').send_keys('1')
        Utils.driver.find_element_by_id('saveItem').click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(2)
        driver.find_element_by_class_name('tdcCollapseAccordion').click()
        time.sleep(2)
        Utils.driver.find_element_by_id('searchByMoreOptions').click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-eye-open").click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-download").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable #checkAllArchiveDocs").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('addTdcDocuments').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].goodsNumbers').send_keys('1')
        time.sleep(1)
        driver.find_element_by_class_name('tdcCollapseAccordion').click()
        time.sleep(1)
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSaveAttachTDCSadImForLegalDocumentsFormData)
        Utils.driver.find_element_by_id('searchByMoreOptions').click()  ##########
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable #checkAllArchiveDocs").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('addTdcDocuments').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .removeIterativeRecord").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[2].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[2].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[3].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[3].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[4].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[4].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[5].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[5].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[6].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[6].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[7].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[7].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[8].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[8].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[9].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[9].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[10].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[10].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[11].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[11].goodsNumbers').send_keys('1')
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord").click()
        Utils.fill_form(IMEXLegalNatural.assessedCorrectionSaveAttach460DocSadImForLegalDocumentsFormData)
        Utils.set_date('fakePresentedDocuments[12].prDocumentDate', '17/01/2018')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('headerTab').click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        Utils.driver.find_element_by_id('goodsShipments[0].mainContractTerms.totalInvoiceAmount').clear()
        Utils.driver.find_element_by_id('goodsShipments[0].mainContractTerms.totalInvoiceAmount').send_keys('16')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdateAssessedModification').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()


    ########################################################################################################################################

    @staticmethod
    def assessed_correctable_submit_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(2)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationSubmitAssessedModification').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        #driver.find_element_by_partial_link_text('Товары').click()
        time.sleep(1)
        #driver.find_element_by_css_selector("#goodsShipmentsGoods .glyphicon-pencil").click()
        #Utils.driver.find_element_by_id('gdcItmChangeCode.basisCompilationCode').send_keys('1')
        #Utils.driver.find_element_by_id('saveItem').click()
        time.sleep(1)
        #Utils.driver.find_element_by_id('operationSubmitAssessedModification').click()
        #element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        #driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def assessed_corrected_reject_kdt_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(2)
        Utils.driver.find_element_by_id('operationRejectAssessedModified').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.find_element_by_partial_link_text('Заметки').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        Utils.driver.find_element_by_id('addNote').click()
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()

    ########################################################################################################################################

    @staticmethod
    def assessed_corrected_register_kdt_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('operationApproveAssessedModified').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def assessed_attach_doc_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_class_name('tdcCollapseAccordion').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('searchByMoreOptions').click()
        time.sleep(1)
        driver.find_element_by_css_selector("ul.pagination").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-eye-open").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-download").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable #checkAllArchiveDocs").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('addTdcDocuments').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[13].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[13].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[14].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[14].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        Utils.driver.find_element_by_id('fakePresentedDocuments[15].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[15].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[16].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[16].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[17].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[17].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[18].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[18].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[19].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[19].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[20].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[20].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[21].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[21].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        time.sleep(1)
        Utils.driver.find_element_by_id('operationAttachDocumentAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)

    ########################################################################################################################################

    @staticmethod
    def assessed_recall_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.find_element_by_class_name('operationRecallAssessedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('itemsTab').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .removeIterativeRecord").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('userNote').send_keys('dfdfadfa')
        Utils.driver.find_element_by_id('operationRecallAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def assessed_update_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.find_element_by_class_name('operationUpdateAssessedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(2)
        Utils.driver.find_element_by_id('operationUpdateAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def assessed_release_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.find_element_by_class_name('operationReleaseAssessedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.find_element_by_class_name('fieldMessage').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-print').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Оплата').click()
        driver.switch_to_window(driver.window_handles[0])  # Close tab browser
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationPayFromOverpaymentClass').click()
        Utils.driver.find_element_by_id('overPayments[12].amountToUse').send_keys('9999999999999')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#obligationsTable .createdColor .glyphicon-pencil").click()
        driver.find_element_by_class_name('operationPayFromOverpaymentClass').click()
        Utils.driver.find_element_by_id('overPayments[12].amountToUse').send_keys('9999999999999')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        driver.find_element_by_css_selector("#obligationsTable tbody tr:first-child td:nth-child(8) a").click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.find_element_by_class_name('operationReleaseAssessedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(4)
        Utils.driver.find_element_by_id('operationReleaseAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def released_attach_doc_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_class_name('tdcCollapseAccordion').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('searchByMoreOptions').click()
        time.sleep(1)
        driver.find_element_by_css_selector("ul.pagination").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-eye-open").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-download").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable #checkAllArchiveDocs").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('addTdcDocuments').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[13].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[13].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[14].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[14].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        Utils.driver.find_element_by_id('fakePresentedDocuments[15].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[15].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[16].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[16].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[17].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[17].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[18].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[18].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[19].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[19].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[20].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[20].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[21].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[21].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .removeIterativeRecord").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationAttachDocumentReleased').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def released_update_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.find_element_by_class_name('operationUpdateReleasedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распределение').click()
        time.sleep(1)
        Utils.check_select('goodsShipments[0].valuation.apportionmentFlag', 1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .removeIterativeRecord").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Иные платежи').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#toBePaidTable .tlpinput").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('otherPayment.providedForm.quantity').clear()
        Utils.driver.find_element_by_id('otherPayment.escortDistance').clear()
        Utils.driver.find_element_by_id('otherPayment.transportControlFee').clear()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(3)
        Utils.driver.find_element_by_id('operationUpdateReleased').click()
        time.sleep(1)
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.find_element_by_class_name('operationUpdateReleasedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdateReleased').click()

    ########################################################################################################################################

    @staticmethod
    def released_correction_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.find_element_by_class_name('operationKdtReleasedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('operationKdtReleased').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('userNote').send_keys('trampampam')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationKdtReleased').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    releasedCorrectableSaveKDTAddGoodsSadImForLegalGoodsFormData = {
        'goodFeatures': 'МПО',
        'goodsTNVEDCode': '12060010000',
        'intellectPropertySign': 'И',
        'additionalSign': 'С',
        'goodsClassificationCode': 'М',
        'originCountryCode': 'AM',
        'grossWeightQuantity': '1',
        'netWeightQuantity': '1',
        'netWeightQuantity2': '1',
        'customsProcedure.precedingCustomsModeCode': '00',
        'customsProcedure.goodsTransferFeatureCode': '000',
        'supplemGoodsQuantity.goodsQuantity': '1',
        'invoicedCost': '9998756',
        'customsCostCorrectMethodCode': '0',
        'goodsDsc': 'fasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfsadfasdfas',
        'goodsDscRu': 'dfASDadasdASDasdASDSDASDAadsfsdfsd',
        # 'container.containerKindCode': '1A',
        'cimIdDetails.cimMarkingFlagCode': 'ПВ',
        'saveItem': None,
    }


    @staticmethod
    def released_correctable_save_kdt_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('itemsTab').click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .glyphicon-trash")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .glyphicon-trash")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .glyphicon-trash")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .glyphicon-trash")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .glyphicon-trash")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .glyphicon-trash")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        #Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalGoodsFormData)
        Utils.driver.find_element_by_id('customsCostCorrectMethod2Code').send_keys('0')
        Utils.fill_form(IMEXLegalNatural.releasedCorrectableSaveKDTAddGoodsSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        # Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalGoodsFormData)
        Utils.driver.find_element_by_id('customsCostCorrectMethod2Code').send_keys('0')
        Utils.fill_form(IMEXLegalNatural.releasedCorrectableSaveKDTAddGoodsSadImForLegalGoodsFormData)
        time.sleep(1)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        # Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalGoodsFormData)
        Utils.driver.find_element_by_id('customsCostCorrectMethod2Code').send_keys('0')
        Utils.fill_form(IMEXLegalNatural.releasedCorrectableSaveKDTAddGoodsSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        # Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalGoodsFormData)
        Utils.driver.find_element_by_id('customsCostCorrectMethod2Code').send_keys('0')
        Utils.fill_form(IMEXLegalNatural.releasedCorrectableSaveKDTAddGoodsSadImForLegalGoodsFormData)
        time.sleep(1)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        # Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalGoodsFormData)
        Utils.driver.find_element_by_id('customsCostCorrectMethod2Code').send_keys('0')
        Utils.fill_form(IMEXLegalNatural.releasedCorrectableSaveKDTAddGoodsSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        # Utils.fill_form(IMEXLegalNatural.createRecallSadImForLegalGoodsFormData)
        Utils.driver.find_element_by_id('customsCostCorrectMethod2Code').send_keys('0')
        Utils.fill_form(IMEXLegalNatural.releasedCorrectableSaveKDTAddGoodsSadImForLegalGoodsFormData)
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[9].goodsNumbers').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[9].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[10].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdateReleasedModification').click()
        time.sleep(1)
        driver.find_element_by_class_name('fieldMessage').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('goodsShipments[0].mainContractTerms.totalInvoiceAmount').clear()
        time.sleep(1)
        Utils.driver.find_element_by_id('goodsShipments[0].mainContractTerms.totalInvoiceAmount').send_keys('59992546')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdateReleasedModification').click()

    ########################################################################################################################################

    @staticmethod
    def released_correctable_submit_kdt_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_partial_link_text('Платежи').click()
        driver.find_element_by_class_name('glyphicon-print').click()
        driver.find_element_by_partial_link_text('Оплата').click()
        driver.switch_to_window(driver.window_handles[0])  # Close tab browser
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationPayFromOverpaymentClass').click()
        Utils.driver.find_element_by_id('overPayments[12].amountToUse').send_keys('9999999999999')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#obligationsTable tbody tr:first-child td:nth-child(8) a").click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_partial_link_text('Иные платежи').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#toBePaidTable .tlpinput").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdateReleasedModification').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to_window(driver.window_handles[0])  # Close tab browser
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('operationSubmitReleasedModification').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def released_correctable_reject_submit_register_kdt_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_partial_link_text('Товары').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        Utils.driver.find_element_by_id('operationRejectReleasedModified').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('operationSubmitReleasedModification').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(2)
        Utils.driver.find_element_by_id('operationApproveReleasedModified').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def released_recall_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.find_element_by_class_name('operationRecallReleasedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_class_name('cancel').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Заметки').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationRecallReleased').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def audit_sad_im_for_legal():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        driver.find_element_by_partial_link_text('Аудит').click()
        time.sleep(1)
        element = driver.find_element_by_css_selector(".tableNoWrap .revisionsDiffLink")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        driver.find_element_by_css_selector(".tableNoWrap tbody tr:first-child td:nth-child(4) a").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

    ########################################################################################################################################
    ########################################################################################################################################
                                            #RISK LEVL RED(SAD for Legal Entitity - IMPORT)
    ########################################################################################################################################
    ########################################################################################################################################

    createRegisterSadImForLegalGeneralFormData = {
        "customsModeCode": "40",
        "regCustomsOffices[0].code": "05100010",
        "goodsShipments[0].specificationNumber": "1234",
        "goodsShipments[0].specificationListNumber": "12345",
        "declarationKindCode": "ОКТ",
        "goodsShipments[0].mainContractTerms.tradeCountryCode": "AE",
        "goodsShipments[0].consigment.dispatchCountryCode": "BG",
        "goodsShipments[0].mainContractTerms.totalInvoiceAmount": "1",
        'goodsShipments[0].mainContractTerms.contractCurrencyCode': 'AMD',
        'goodsShipments[0].mainContractTerms.dealNatureCode': '545',
        'goodsShipments[0].mainContractTerms.dealFeatureCode': '56',
    }

    createRegisterSadImForLegalPartiesFormData = {
        'goodsShipments[0].consignor.organizationName': '1',
        'goodsShipments[0].consignor.address.postalCode': '1',
        'goodsShipments[0].consignor.address.countryCode': 'AM',
        'goodsShipments[0].consignor.address.region': '3425',
        'goodsShipments[0].consignor.address.city': '235',
        'goodsShipments[0].consignor.address.streetHouse': '2134',
        'goodsShipments[0].consignee.raOrganizationFeatures.unn': '17031994',
        'goodsShipments[0].finRespPerson.raOrganizationFeatures.unn': '17031994',
        'goodsShipments[0].declarant.raOrganizationFeatures.unn': '17031994',
        'null.goodsLocTransportAccordion': None,
        #'addPhoneButton': None,
        #'filledPersons[0].contact.phones[1].number': '+375345345'
    }

    createRegisterSadImForLegalTransportationFormData = {
        'goodsShipments[0].mainContractTerms.deliveryTerms.deliveryTermsStringCode': 'CIF',
        'goodsShipments[0].mainContractTerms.deliveryTerms.deliveryPlace': '12341',
        'goodsShipments[0].consigment.departureArrivalTransport.transportModeCode': '31',
        'goodsShipments[0].consigment.borderTransport.transportModeCode': '31',
        'goodsShipments[0].goodsLocation[0].informationTypeCode': '21',
        'goodsShipments[0].goodsLocation[0].customsOfficeCode': '05100017',
        'goodsShipments[0].goodsLocation[0].goodsLocationPlace.numberCustomsZoneCode': 'MP00013',
        'goodsShipments[0].goodsLocation[0].locationName': '2345234'
    }

    createRegisterSadImForLegalGoodsFormData = {
        'goodFeatures': 'МПО',
        'goodsTNVEDCode': '85182930010',
        'intellectPropertySign': 'И',
        'goodsAddTNVEDCode': '0001',
        'additionalSign': 'С',
        'goodsClassificationCode': 'М',
        'originCountryCode': 'AM',
        'grossWeightQuantity': '1',
        'netWeightQuantity': '1',
        'netWeightQuantity2': '1',
        'customsProcedure.precedingCustomsModeCode': '00',
        'customsProcedure.goodsTransferFeatureCode': '000',
        'supplemGoodsQuantity.goodsQuantity': '1',
        'invoicedCost': '1',
        'customsCostCorrectMethodCode': '0',
        'goodsDsc': 'fasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfsadfasdfas',
        'goodsDscRu': 'dfASDadasdASDasdASDSDASDAadsfsdfsd',
        # 'container.containerKindCode': '1A',
        'cimIdDetails.cimMarkingFlagCode': 'ПВ',
        'saveItem': None,
    }

    createRegisterSadImForLegalApportionmentFormData = {
        'goodsShipments[0].valuation.transportChargesTaxBase': '100',
        'goodsShipments[0].valuation.insuranceChargesTaxBase': '1000000',
        'goodsShipments[0].valuation.otherChargesTaxBase': '999999999',
        'goodsShipments[0].valuation.unionTransportChargesTaxBase': '9999999',
        'goodsShipments[0].valuation.deductionsTaxBase': '0,34',
        'goodsShipments[0].valuation.transportChargesCurrencyCode': 'AMD',
        'goodsShipments[0].valuation.insuranceChargesCurrencyCode': 'USD',
        'goodsShipments[0].valuation.otherChargesCurrencyCode': 'EUR',
        'goodsShipments[0].valuation.unionTransportChargesCurrencyCode': 'BYR',
        'goodsShipments[0].valuation.deductionsCurrencyCode': 'BRL'

    }

    createRegisterSadImForLegalDocumentsFormData = {
        'fakePresentedDocuments[0].presentedDocumentModeCode': '460',
        'fakePresentedDocuments[0].providingIndicationMark': '0',
        'fakePresentedDocuments[0].prDocumentNumber': '123412',
        # 'fakePresentedDocuments[0].goodsNumbers': '1'
    }

    createRegisterSadImForLegalCustomsFeeFormData = {
        'otherPayment.providedForm.quantity': '999',
        'otherPayment.escortDistance': '99999',
        'otherPayment.transportControlFee': '99999999',
    }

    @staticmethod
    def create_register_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get('https://uatapp3.fipsoft.com/cusad/sad/create?customsProcedure=IM&iff=I')
        Utils.fill_form(IMEXLegalNatural.createRegisterSadImForLegalGeneralFormData)
        driver.find_element_by_partial_link_text('Стороны').click()
        Utils.fill_form(IMEXLegalNatural.createRegisterSadImForLegalPartiesFormData)
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, 0 );")
        driver.find_element_by_partial_link_text('Перевозка').click()
        time.sleep(1)
        Utils.check_select('goodsShipments[0].consigment.containerIndicator', 2)
        Utils.fill_form(IMEXLegalNatural.createRegisterSadImForLegalTransportationFormData)
        driver.execute_script("window.scrollTo( 0, 0 );")
        driver.find_element_by_partial_link_text('Товары').click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.createRegisterSadImForLegalGoodsFormData)
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распределение').click()
        Utils.fill_form(IMEXLegalNatural.createRegisterSadImForLegalApportionmentFormData)
        Utils.check_select('goodsShipments[0].valuation.transportChargesApportionmentType', 1)
        Utils.check_select('goodsShipments[0].valuation.insuranceChargesApportionmentType', 2)
        Utils.check_select('goodsShipments[0].valuation.otherChargesApportionmentType', 1)
        Utils.check_select('goodsShipments[0].valuation.unionTransportChargesApportionmentType', 2)
        Utils.check_select('goodsShipments[0].valuation.deductionsApportionmentType', 1)
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord").click()
        # driver.find_element_by_css_selector("#fakePresentedDocuments thead tr:first-child a").click()
        Utils.fill_form(IMEXLegalNatural.createRegisterSadImForLegalDocumentsFormData)
        Utils.set_date('fakePresentedDocuments[0].prDocumentDate', '17/01/2018')
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Иные платежи').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#toBePaidTable .tlpinput").click()
        Utils.fill_form(IMEXLegalNatural.createRegisterSadImForLegalCustomsFeeFormData)
        time.sleep(1)
        #Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(3)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationStore').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.find_element_by_class_name('cancel').click()
        time.sleep(1)
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        element = driver.find_element_by_css_selector("#searchRes .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.switch_to_window(driver.window_handles[0])  # Close tab browser
        driver.close()  # Close tab browser
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationSubmitStored').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        element = driver.find_element_by_css_selector("#searchRes .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.switch_to_window(driver.window_handles[0])  # Close tab browser
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_class_name('cancel').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationRegisterSubmitted').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

    ########################################################################################################################################

    @staticmethod
    def selected_reject_registration_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        Utils.driver.find_element_by_id('operationRejectRegistrationSelected').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        Utils.driver.find_element_by_id('operationRejectRegistrationSelected').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def selected_rejection_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationRejectSelectedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationRejectSelected').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def selected_correction_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.find_element_by_class_name('operationKdtSelectedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        Utils.driver.find_element_by_id('operationKdtSelected').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        Utils.driver.find_element_by_id('operationKdtSelected').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()


    ########################################################################################################################################

    selectedCorrectionSaveAttachTDCSadImForLegalDocumentsFormData = {
        'tdcAccessKey': '328C0632O78Z2837',
        'tdcDocCode': '01017',
        'tdcDescription': '123',
        'tdcDocumentNumber': '123',
        'searchByMoreOptions': None
    }

    selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData = {
        'goodFeatures': 'МПО',
        'goodsTNVEDCode': '85182930010',
        'intellectPropertySign': 'И',
        'goodsAddTNVEDCode': '0001',
        'additionalSign': 'С',
        'goodsClassificationCode': 'М',
        'originCountryCode': 'AM',
        'grossWeightQuantity': '1',
        'netWeightQuantity': '1',
        'netWeightQuantity2': '1',
        'customsProcedure.precedingCustomsModeCode': '00',
        'customsProcedure.goodsTransferFeatureCode': '000',
        'supplemGoodsQuantity.goodsQuantity': '1',
        'invoicedCost': '1',
        'customsCostCorrectMethodCode': '0',
        'customsCostCorrectMethod2Code': '0',
        'goodsDsc': 'fasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfsadfasdfas',
        'goodsDscRu': 'dfASDadasdASDasdASDSDASDAadsfsdfsd',
        # 'container.containerKindCode': '1A',
        'cimIdDetails.cimMarkingFlagCode': 'ПВ',
        'saveItem': None,
    }

    selectedCorrectionSaveAttach460DocSadImForLegalDocumentsFormData = {
        'fakePresentedDocuments[12].presentedDocumentModeCode': '460',
        'fakePresentedDocuments[12].providingIndicationMark': '0',
        'fakePresentedDocuments[12].prDocumentNumber': '123412',
        # 'fakePresentedDocuments[0].goodsNumbers': '1'
    }

    @staticmethod
    def selected_correction_save_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Товары').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#goodsShipmentsGoods .glyphicon-pencil").click()
        Utils.driver.find_element_by_id('gdcItmChangeCode.basisCompilationCode').send_keys('1')
        Utils.driver.find_element_by_id('saveItem').click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        element = driver.find_element_by_css_selector("#goodsShipmentsGoods .addItemBtn")
        driver.execute_script("arguments[0].click();", element)
        Utils.check_select('goodsPackaging.pakageTypeCode', 2)
        Utils.set_date('deliveryTime', '29/08/2018')
        Utils.set_date('deliveryTimeEND', '31/08/2018')
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalGoodsFormData)
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(2)
        driver.find_element_by_class_name('tdcCollapseAccordion').click()
        time.sleep(2)
        Utils.driver.find_element_by_id('searchByMoreOptions').click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-eye-open").click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-download").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable #checkAllArchiveDocs").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('addTdcDocuments').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].goodsNumbers').send_keys('1')
        time.sleep(1)
        driver.find_element_by_class_name('tdcCollapseAccordion').click()
        time.sleep(1)
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttachTDCSadImForLegalDocumentsFormData)
        Utils.driver.find_element_by_id('searchByMoreOptions').click()  ##########
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable #checkAllArchiveDocs").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('addTdcDocuments').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .removeIterativeRecord").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[2].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[2].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[3].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[3].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[4].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[4].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[5].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[5].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[6].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[6].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[7].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[7].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[8].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[8].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[9].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[9].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[10].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[10].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[11].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[11].goodsNumbers').send_keys('1')
        time.sleep(1)
        driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord").click()
        Utils.fill_form(IMEXLegalNatural.selectedCorrectionSaveAttach460DocSadImForLegalDocumentsFormData)
        Utils.set_date('fakePresentedDocuments[12].prDocumentDate', '17/01/2018')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        time.sleep(1)
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('headerTab').click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        Utils.driver.find_element_by_id('goodsShipments[0].mainContractTerms.totalInvoiceAmount').clear()
        Utils.driver.find_element_by_id('goodsShipments[0].mainContractTerms.totalInvoiceAmount').send_keys('16')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdateModification').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()


    #########################################################################################################################################

    @staticmethod
    def selected_correctable_submit_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(2)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationSubmitModification').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

    ########################################################################################################################################

    @staticmethod
    def selected_corrected_reject_kdt_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(2)
        Utils.driver.find_element_by_id('operationRejectModified').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.find_element_by_partial_link_text('Заметки').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        Utils.driver.find_element_by_id('addNote').click()
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()

    ########################################################################################################################################

    @staticmethod
    def selected_corrected_register_kdt_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('operationApproveModified').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def selected_attach_doc_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_class_name('tdcCollapseAccordion').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('searchByMoreOptions').click()
        time.sleep(1)
        driver.find_element_by_css_selector("ul.pagination").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-eye-open").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-download").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable #checkAllArchiveDocs").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('addTdcDocuments').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[13].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[13].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[14].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[14].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        Utils.driver.find_element_by_id('fakePresentedDocuments[15].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[15].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[16].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[16].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[17].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[17].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[18].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[18].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[19].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[19].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[20].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[20].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[21].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[21].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        time.sleep(1)
        Utils.driver.find_element_by_id('operationAttachDocumentSelected').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)

    ########################################################################################################################################

    @staticmethod
    def selected_continue_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationContinueSelectedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(4)
        driver.find_element_by_css_selector("#documentErrorContainer .fieldMessage").click()
        time.sleep(1)
        driver.find_element_by_class_name('rmsLink').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationAddFeedbackClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_partial_link_text('Процедура').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#instructionsTable #selectAllFb").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('feedbackCode').send_keys('F010')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationSaveFeedback').click()
        time.sleep(1)
        driver.find_element_by_class_name('documentLink').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationContinueSelectedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(3)
        Utils.driver.find_element_by_id('operationContinueSelected').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def assessed_reject_registration_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationRejectRegistrationAssessed').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        Utils.driver.find_element_by_id('operationRejectRegistrationAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)

    ########################################################################################################################################

    @staticmethod
    def assessed_attach_doc_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_class_name('tdcCollapseAccordion').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('searchByMoreOptions').click()
        time.sleep(1)
        driver.find_element_by_css_selector("ul.pagination").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-eye-open").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-download").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable #checkAllArchiveDocs").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('addTdcDocuments').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[13].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[13].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[14].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[14].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        Utils.driver.find_element_by_id('fakePresentedDocuments[15].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[15].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[16].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[16].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[17].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[17].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[18].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[18].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[19].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[19].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[20].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[20].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[21].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[21].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        time.sleep(1)
        Utils.driver.find_element_by_id('operationAttachDocumentAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)

    ########################################################################################################################################


    assessedReleaseRejectionAttachTDCSadImForLegalDocumentsRedLvlFormData = {
        'tdcAccessKey': '726A2357A39C3187',
        'tdcDocCode': '09015',
        'tdcDescription': 'r',
        'tdcDocumentNumber': 'r',
        'searchByMoreOptions': None
    }

    @staticmethod
    def assessed_release_rejection_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationRejectAssessedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationRejectAssessed').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        Utils.driver.find_element_by_id('operationRejectAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)


    ########################################################################################################################################

    @staticmethod
    def assessed_correction_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationKdtAssessedClass').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationKdtAssessed').click()
        Utils.driver.find_element_by_id('userNote').send_keys('value')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationKdtAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()


    ########################################################################################################################################

    @staticmethod
    def assessed_correction_save_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(2)
        # driver.find_element_by_partial_link_text('Распечатать КДТ').click()
        # driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Товары').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdateAssessedModification').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать').click()
        driver.find_element_by_partial_link_text('Экспортировать XML').click()
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()


    ########################################################################################################################################

    @staticmethod
    def assessed_correctable_submit_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(2)
        Utils.driver.find_element_by_id('printButton').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('exportXmlButton').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Распечатать КДТ').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationSubmitAssessedModification').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

    ########################################################################################################################################

    @staticmethod
    def assessed_attach_doc_sad_im_for_legal_red_lvl():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)
        driver.find_element_by_class_name('tdcCollapseAccordion').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('searchByMoreOptions').click()
        time.sleep(1)
        driver.find_element_by_css_selector("ul.pagination").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-eye-open").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable .glyphicon-download").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_css_selector("#tdcSearchResultsTable #checkAllArchiveDocs").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('addTdcDocuments').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[12].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[13].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[13].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[14].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[14].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        Utils.driver.find_element_by_id('fakePresentedDocuments[15].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[15].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[16].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[16].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[17].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[17].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[18].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[18].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[19].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[19].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[20].providingIndicationMark').send_keys('2')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[20].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        Utils.driver.find_element_by_id('fakePresentedDocuments[21].providingIndicationMark').send_keys('1')
        time.sleep(1)
        Utils.driver.find_element_by_id('fakePresentedDocuments[21].attItemModal').click()
        time.sleep(1)
        driver.find_element_by_css_selector("#tblGrid #checkAllItem").click()
        driver.find_element_by_class_name('attModalSave').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#formContainer #checkButton").click()
        time.sleep(1)
        driver.execute_script("window.scrollTo( 0, document.body.scrollHeight );")
        time.sleep(1)
        Utils.driver.find_element_by_id('operationAttachDocumentAssessed').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        Utils.driver.find_element_by_id('presentedDocumentsTab').click()
        time.sleep(1)




































































