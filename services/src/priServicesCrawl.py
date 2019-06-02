# -*- coding: utf-8 -*-

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import csv

html = []

url = "http://m.bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do?searchIntClId=07"
driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("lang=ko_KR")
driver.get(url)

driver.find_element_by_id("topWSI").click()
num = driver.find_element_by_id("search_length")
repeatVal = int(num.text)/5
print(repeatVal)

for i in range(repeatVal) :
    f = open('priServices.csv', 'w')
    for j in range(5) :
        innerURL = "//div[@class='service_group_list']/ul[1]/li[" + str(j+1) + "]"
        driver.find_element_by_xpath(innerURL).click()
        csvRow = ["", "", "", "", "", "", "", "", ""]
        for k in range(5) :
            result = driver.find_element_by_xpath("//div[@class='shareServiceCont']/ul/li[" + str(k+1) + "]/strong").text
            if result.encode('utf-8') == '사업목적' :
                servDgst = driver.find_element_by_xpath("//div[@class='shareServiceCont']/ul/li[" + str(k+1) + "]/div").text
                csvRow[4] = servDgst.encode('utf-8')

        jurMnofNm = driver.find_element_by_xpath("//form[@id='frm']/div[1]/div/table/tbody/tr[1]/td").text
        csvRow[2] = jurMnofNm.encode('utf-8')
        servDtlLink = driver.current_url
        csvRow[5] = servDtlLink
        servId = servDtlLink.split("&welInfSno=")[1]
        servId = servId.split("&")[0]
        csvRow[6] = servId
        servNm = driver.find_element_by_xpath("//h2[@class='title']").text
        csvRow[7] = servNm.encode('utf-8')
        svcfrstRegTs = driver.find_element_by_xpath("//form[@id='frm']/div[1]/div/table/tbody/tr[3]/td").text
        csvRow[8] = svcfrstRegTs.encode('utf-8')

        wr = csv.writer(f)
        wr.writerow(csvRow)

        time.sleep(2)
        driver.back()
        driver.find_element_by_id("topWSI").click()
    driver.find_element_by_class_name("ui-button-list-more").click()
    time.sleep(2)
    f.close()
driver.quit()
