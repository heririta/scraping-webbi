import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    options=options, executable_path="D:\HERI\selenium\dataWebBI\chromedriver.exe")
driver.get("https://www.bi.go.id/id/statistik/indikator/IndONIA.aspx")
driver.implicitly_wait(10)
# print(driver.page_source)
time.sleep(5)

elementFrom = driver.find_element_by_xpath('//*[@id="dtBulanFrom"]')
elementFrom.send_keys("")
elementFrom.send_keys(Keys.ENTER)

time.sleep(3)

elementTo = driver.find_element_by_xpath('//*[@id="dtBulanTo"]')
elementTo.send_keys("")
elementTo.send_keys(Keys.ENTER)

time.sleep(3)

elementSubmit = driver.find_element_by_xpath(
    '//*[@id="ctl00_ctl44_g_3f02dde8_c13a_4d75_a020_c72d7e058154_ctl00_ButtonFilter"]')
elementSubmit.click()


driver.implicitly_wait(10)
time.sleep(2)
# print(driver.page_source)

datajibor = pd.read_html(driver.page_source)
# print(datajibor[0])
# print(datajibor[1])

filename = "D:\HERI\selenium\dataWebBI\Tbljibor1_" + \
    (time.strftime("%Y%m%d")+".csv")
filename2 = "D:\HERI\selenium\dataWebBI\Tbljibor2__" + \
    (time.strftime("%Y%m%d")+".csv")

datajibor[0].to_csv(filename, index=True, header=True, sep='|')
datajibor[1].to_csv(filename2, index=True, header=True, sep='|')


time.sleep(5)

driver.close()
