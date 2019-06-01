from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

html = []

url = "http://m.bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do?searchIntClId=07"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)

driver.find_element_by_id("topWSI").click()
num = driver.find_element_by_id("search_length")
repeatVal = int(num.text)/5
print(repeatVal)
for i in range(repeatVal) :
    driver.find_element_by_class_name("ui-button-list-more").click()
    time.sleep(2)
# driver.quit()
