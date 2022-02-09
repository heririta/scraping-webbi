import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    options=options, executable_path="D:\HERI\selenium\dataWebBI\chromedriver.exe")
driver.get("https://www.bi.go.id/id/statistik/indikator/bi-7day-rr.aspx")
driver.implicitly_wait(10)
# print(driver.page_source)
time.sleep(5)

elementTo = driver.find_element_by_xpath('//*[@id="TextBoxDateEnd"]')
elementTo.send_keys("")
elementTo.send_keys(Keys.ENTER)


elementBi7dayrr = driver.find_element_by_xpath(
    '//*[@id="ctl00_ctl44_g_4dbaa7f5_3c71_4542_af75_185912ff0c39_ctl00_ButtonSearch"]')
elementBi7dayrr.click()

driver.implicitly_wait(10)
time.sleep(2)

dataBi7dayrr = pd.read_html(driver.page_source)
print(dataBi7dayrr[0])

filename = "D:\HERI\selenium\dataWebBI\TblBI7dayrr__" + \
    (time.strftime("%Y%m%d")+".csv")

dataBi7dayrr[0].to_csv(filename, index=False, header=True, sep='|')


time.sleep(5)

driver.close()
