import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

options = webdriver.ChromeOptions()


driver = webdriver.Chrome(
    options=options, executable_path="D:\HERI\selenium\dataWebBI\chromedriver.exe")
driver.get(
    "https://www.bi.go.id/id/statistik/informasi-kurs/jisdor/Default.aspx")
driver.implicitly_wait(10)
# print(driver.page_source)
time.sleep(5)

elementTo = driver.find_element_by_xpath('//*[@id="TextBoxDateTo"]')
elementTo.send_keys("")
elementTo.send_keys(Keys.ENTER)

time.sleep(3)

elementSubmit = driver.find_element_by_xpath(
    '//*[@id="ctl00_ctl44_g_f51e6b6d_47c5_4ff4_8105_27cbd1a2f52d_ctl00_ButtonCari"]')
elementSubmit.click()


driver.implicitly_wait(10)
time.sleep(2)


datakursbi = pd.read_html(driver.page_source)
# print(datakursbi[0])

filename = "D:\HERI\selenium\dataWebBI\Jisdor_" + \
    (time.strftime("%Y%m%d")+".csv")

datakursbi[0].to_csv(filename, index=False, header=False, sep='|')

time.sleep(5)

driver.close()
