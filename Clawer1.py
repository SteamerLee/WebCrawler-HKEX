#!/usr/bin/python
# This is the first prog. for crawler-2019-01-21
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()

# 类别选择：
#input:选择19750 //*[@id="tab-panel-title-search"]/form/input[7]
# 最终选择处：改data-value与文本 //*[@id="rbAfter2006"]/div[1]/div/div/a
# 19750's Xpath(内幕消息)改data-select-target-true  //*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]/div/ul/li[9]/div/div/ul/li[5]
# -2'Xpath(全局所有)改data-select-target-false    //*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[1]
try:
    browser.get("http://www.hkexnews.hk/index_c.htm")
    #input = browser.find_element_by_id('')
    #input.send_keys('')
    #input.send.keys(Keys.ENTER)

    print("HKEX_Current_URL: ",browser.current_url)
    print("Get HKEX cookies: ",browser.get_cookies())
    print("HKEX Source page: ",browser.page_source)
    browser.maximize_window()
    #click btn for selecting report class
    titleclassbutton1 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[1]/div/div/a')
    titleclassbutton1.click()
    sleep(0.5)
    titleclassbutton2 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]')
    titleclassbutton2.click()
    sleep(0.5)
    Drag = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]/div/div/div[1][@class ="combobox-list-scroll-bar"]')
    ActionChains(browser).drag_and_drop_by_offset(Drag, 0, 100).perform()
    sleep(0.5)
    '''
    js = 'document.getElementsByClassName("combobox-list-scroll-bar").scrollTop=110'
    browser.execute_script(js)
    '''
    #WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#rbAfter2006 > div.combobox-boundlist > div > div > div > ul > li:nth-child(2)#aria-expanded'), u'true'))
    #WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element_value((By.XPATH,'//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2][@aria-expanded]'), u'true'))
    titleclassbutton3 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]/div/div/ul/li[9]')
    titleclassbutton3.click()
    sleep(0.5)
    titleclassbutton4 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]/div/div/ul/li[9]/div/div/ul/li[5]')
    titleclassbutton4.click()

    #select period
    #select_from_date
    datefromSelect = browser.find_element_by_xpath('// *[ @ id = "searchDate-From"]')
    datefromSelect.click()
    datefromY = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[1]/ul/li[2]/button')
    datefromY.click()
    datefromM = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[2]/ul/li[1]/button')
    datefromM.click()
    datefromD = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[3]/ul/li[1]/button')
    datefromD.click()
    datefromSelect.click()

    #select to_date
    datetoSelect = browser.find_element_by_xpath('//*[@id = "searchDate-To"]')
    datetoSelect.click()
    datetoY = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[1]/ul/li[2]/button')
    datetoY.click()
    datetoM = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[2]/ul/li[12]/button')
    datetoM.click()
    datetoD = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[3]/ul/li[31]/button')
    datetoD.click()
    datetoSelect.click()

    input = browser.find_element_by_xpath('//*[@id="searchTitle"]')
    input.send_keys('盈利')


    searchbtn = browser.find_element_by_xpath('// *[ @ id = "tab-panel-title-search"] / form / div / div[3] / a[3]')
    searchbtn.click()


    print("Get New Source",browser.page_source)

    """"
    #   下一页
    button = browser.find_element_by_class_name('btn-blue')
    button.click()
    print("HKEX_CSearch_URL: ",browser.current_url)
    print("Get search HKEX cookies: ",browser.get_cookies())
    print("HKEX search Source page: ",browser.page_source)
    """


finally:
    pass
    #browser.close()

