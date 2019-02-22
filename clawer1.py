#!/usr/bin/python
# -*- coding: utf-8 -*-#
# Name:         ${NAME}
# Description:  This is the first prog. for crawler-2019-01-21
# Author:       ${USER}
# Date:         ${DATE}
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import re
import requests
import urllib.request
import os
import csv
from bs4 import BeautifulSoup

# Func. Description: Enter the home page and choose search conditions.
def homepage():

    # get homepage.
    browser.get("http://www.hkexnews.hk/index_c.htm")
    sleep(1)
    '''
    print("HKEX_Current_URL: ",browser.current_url)
    print("Get HKEX cookies: ",browser.get_cookies())
    print("HKEX Source page: ",browser.page_source)
    '''
    # Adjust screen
    browser.maximize_window()

    # Click btn for selecting report class

    # For method 1 [1928 items in 2018]
    # Btn for title class 1
    titleclassbutton1 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[1]/div/div/a')
    titleclassbutton1.click()

    titleclassbutton2 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]')
    titleclassbutton2.click()

    # Adjust screen for selecting items
    Drag1 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/div[1]')
    #[@class =“combobox-list-scroll-bar"]') # for ASUS//*[@id="rbAfter2006"]/div[2]/div/div/div/div[1]
    ActionChains(browser).drag_and_drop_by_offset(Drag1, 0, 60).perform()

    titleclassbutton3 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]/div/ul/li[6]')
    titleclassbutton3.click()

    Drag2 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]/div/ul/li[6]/div/div/div[1]')
    # [@class =“combobox-list-scroll-bar"]') # for ASUS
    Drag2.click()
    ActionChains(browser).drag_and_drop_by_offset(Drag2, 0, 100).perform()

    titleclassbutton4 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]/div/ul/li[6]/div/div/ul/li[11]')
    titleclassbutton4.click()

    # Select period
    # Select_from_date
    datefromSelect = browser.find_element_by_xpath('// *[ @ id = "searchDate-From"]')
    datefromSelect.click()
    # Year
    datefromY = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[1]/ul/li[12]/button')
    datefromY.click()
    # Month
    datefromM = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[2]/ul/li[1]/button')
    datefromM.click()
    # Day
    datefromD = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[3]/ul/li[1]/button')
    datefromD.click()
    datefromSelect.click()

    # Select to_date
    datetoSelect = browser.find_element_by_xpath('//*[@id = "searchDate-To"]')
    datetoSelect.click()
    # Year
    datetoY = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[1]/ul/li[12]/button')
    datetoY.click()
    # Month
    datetoM = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[2]/ul/li[12]/button')
    datetoM.click()
    # Day
    datetoD = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[3]/ul/li[31]/button')
    datetoD.click()
    datetoSelect.click()

    # For method 2 [1650 items in 2018]
    '''
    # Btn for title class 1
    titleclassbutton1 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[1]/div/div/a')
    titleclassbutton1.click()

    titleclassbutton2 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]')
    titleclassbutton2.click()
    
    # Adjust screen for selecting items
    Drag = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/div[1]')
    #[@class =“combobox-list-scroll-bar"]') # for ASUS
    ActionChains(browser).drag_and_drop_by_offset(Drag, 0, 100).perform()
    titleclassbutton3 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]/div/ul/li[9]')
    titleclassbutton3.click()
    titleclassbutton4 = browser.find_element_by_xpath('//*[@id="rbAfter2006"]/div[2]/div/div/div/ul/li[2]/div/ul/li[9]/div/div/ul/li[5]')
    titleclassbutton4.click()

    # Select period
    # Select_from_date
    datefromSelect = browser.find_element_by_xpath('// *[ @ id = "searchDate-From"]')
    datefromSelect.click()
    datefromY = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[1]/ul/li[2]/button')
    datefromY.click()
    datefromM = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[2]/ul/li[1]/button')
    datefromM.click()
    datefromD = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[3]/ul/li[1]/button')
    datefromD.click()
    datefromSelect.click()

    # Select to_date
    datetoSelect = browser.find_element_by_xpath('//*[@id = "searchDate-To"]')
    datetoSelect.click()
    datetoY = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[1]/ul/li[2]/button')
    datetoY.click()
    datetoM = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[2]/ul/li[12]/button')
    datetoM.click()
    datetoD = browser.find_element_by_xpath('//*[@id="date-picker"]/div[1]/b[3]/ul/li[31]/button')
    datetoD.click()
    datetoSelect.click()

    # Input keywords for searching
    input = browser.find_element_by_xpath('//*[@id="searchTitle"]')
    input.send_keys('盈利')
    '''
    #End for method2

    # Click search button.
    searchbtn = browser.find_element_by_xpath('// *[ @ id = "tab-panel-title-search"] / form / div / div[3] / a[3]')
    searchbtn.click()

# Get stock information from page
def getinfo(Info_list):
    # Get the sequence number of current page(1st_item,last_item,total number)
    recorditemnum = browser.find_element_by_xpath('//*[@id="ctl00_lblDisplay"]')
    print(recorditemnum.text)
    # '顯示第 1 至 20 紀錄 (共有 1650 紀錄)' ->(1)=1;(2)=20;(3)=1650;
    result = re.match('.*?(\d+).*?(\d+).*?(\d+)', recorditemnum.text)
    cpage_first_num = result.group(1)
    cpage_last_num = result.group(2)
    rec_total_num = result.group(3)

    # Locate inforamtion table
    parentnode = browser.find_element_by_xpath('//*[@id="ctl00_gvMain"]/tbody')
    sonnode = parentnode.find_elements_by_xpath('./*')
    # Delete non information nodes
    del sonnode[0]
    sonnode.pop()
    # Get the first item number in this page
    num_x = int(cpage_first_num)
    # loop for getting individual stock information
    for singlenode in sonnode:
        Info_list[0].append(str(num_x))
        itemnode = singlenode.find_elements_by_xpath('./*')
        # release time
        #timerec = itemnode[0].text
        # 28/12/2018 <br> 21:39
        datepattern = re.compile('.*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)',re.S)
        dateresult = re.match(datepattern, itemnode[0].text)
        day = dateresult.group(1)
        Info_list[6].append(day)
        Info_list[5].append(dateresult.group(2))
        Info_list[4].append(dateresult.group(3))
        Info_list[7].append(dateresult.group(4))
        Info_list[8].append(dateresult.group(5))
        #print("year: %s, month: %s, day: %s, hour: %s, minute: %s" %(year,month,day,hour,minute))

        # stock code-01775
        Info_list[1].append(itemnode[1].text)

        # stock name-腾讯控股
        Info_list[2].append(itemnode[2].text)

        # stock report category and download link
        # Category盈利预告
        # href: http://www3.hkexnews.hk/listedco/listconews/SEHK/2018/1228/LTN201812281356_C.pdf
        subitemnode = itemnode[3].find_elements_by_xpath('./*')
        Info_list[3].append(subitemnode[1].text)
        Info_list[9].append(subitemnode[1].get_attribute('href'))

        num_x = num_x+1
    return cpage_first_num, cpage_last_num, rec_total_num, Info_list

# Turn to next page
def nextpage():
    nextpagebtn = browser.find_element_by_xpath('//*[@id="ctl00_btnNext"]')
    nextpagebtn.click()
    sleep(1)

# Save stock information as csv format.
def savedata(Info_list):
    pdfnums = Info_list[0]
    pdfcodes = Info_list[1]
    pdfnames = Info_list[2]
    pdfctgs = Info_list[3]
    pdfyears = Info_list[4]
    pdfmonths = Info_list[5]
    pdfdays = Info_list[6]
    pdfhours = Info_list[7]
    pdfmins = Info_list[8]
    pdflinks = Info_list[9]
    # Eg: csv name: 2018data.csv
    csvname = pdfyears[1] + 'data' + '.csv'
    FILE_DIR = pdfyears[1]
    # Created dir..
    if not os.path.exists(FILE_DIR):
        os.makedirs(FILE_DIR)
    print("Dir Created successfully")
    # Write data
    with open(os.path.join(FILE_DIR,csvname),'w',encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Number','StockCode','StockName','Category','Year','Month','Day','Hour','Minute','PDFName','Link'])
        for itemindex in range(len(pdfnums)):
            filename = pdfyears[itemindex] + pdfnums[itemindex]
            writer.writerow([pdfnums[itemindex],pdfcodes[itemindex],pdfnames[itemindex],pdfctgs[itemindex],pdfyears[itemindex],pdfmonths[itemindex],pdfdays[itemindex],pdfhours[itemindex],pdfmins[itemindex],filename,pdflinks[itemindex]])
    print("Data has been written to csv!")

# Read data from csv
def readcsv():
    csvname = '2018data.csv'
    FILE_DIR = '2018'
    with open(os.path.join(FILE_DIR,csvname),'r',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        #Note: row[9] is PDFName, row[10] is link_list.
        for row in reader:
            print(row)

# Download report
def dlreport(Info_list):

    urls = Info_list[9]
    pdfnums = Info_list[0]
    pdfyears = Info_list[4]
    FILE_DIR = pdfyears[1]
    for pdfurl,pdfnum,pdfyear in zip(urls,pdfnums,pdfyears):
        #Eg: pdfname: 20181.pdf
        pdfname = pdfyear + pdfnum + '.pdf'
        pdfpage = requests.get(pdfurl,stream=True)
        with open(os.path.join(FILE_DIR,pdfname),'wb') as f:
            for chunk in pdfpage.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        print("Download Finished: ",pdfnum)


def main():
    # Create object
    global browser
    browser = webdriver.Chrome()
    # Initialization
    Info_list = []
    num_list = []
    stockcode_list = []
    stockname_list = []
    reportcatg_list = []
    year_list = []
    month_list = []
    day_list = []
    hour_list = []
    minute_list = []
    link_list = []
    Info_list = [num_list,stockcode_list,stockname_list,reportcatg_list,year_list,month_list,day_list,hour_list,minute_list,link_list]
    # Open home page
    homepage()
    sleep(1)
    # Extract data from page
    (cpage_first_num, cpage_last_num, rec_total_num, Info_list) = getinfo(Info_list)
    # Judge next page whether exist
    while int(cpage_last_num) < int(rec_total_num):
    #while int(cpage_last_num) < 20:
        nextpage()
        (cpage_first_num, cpage_last_num, rec_total_num, Info_list) = getinfo(Info_list)
        #print("Page %d is finished. Item %s to %s is recorded" %(((int(cpage_first_num)//20)+1), cpage_first_num, cpage_last_num))

    # Note: The order in list is from latest to old, which means that the first row in list is the latest(last) report of this year.
    print(Info_list[0])
    print(Info_list[1])
    print(Info_list[2])
    print(Info_list[3])
    print(Info_list[4])
    print(Info_list[5])
    print(Info_list[6])
    print(Info_list[7])
    print(Info_list[8])
    print(Info_list[9])

    # Save data into csv.
    savedata(Info_list)
    # Download pdf
    dlreport(Info_list)
    print('Everything is done!')



if __name__ == '__main__':
    try:
        # Parameter:
        # Selenium的点击Xpath, 包括公告种类，年份日期(From, To)，滚动条滑动距离等
        main()
    except:
        print("It seems happen error!")
