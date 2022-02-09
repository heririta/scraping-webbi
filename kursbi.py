import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

options = webdriver.ChromeOptions()


driver = webdriver.Chrome(
    options=options, executable_path="D:\HERI\selenium\dataWebBI\chromedriver.exe")
driver.get(
    "https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/Default.aspx")
driver.implicitly_wait(10)
print(driver.page_source)
time.sleep(5)


datakursbi = pd.read_html(driver.page_source)
print(datakursbi[0])
print(datakursbi[1])


filename = "D:\HERI\selenium\dataWebBI\TblRefKurs_" + \
    (time.strftime("%Y%m%d")+".csv")
filename2 = "D:\HERI\selenium\dataWebBI\TblKurs__" + \
    (time.strftime("%Y%m%d")+".csv")

datakursbi[0].to_csv(filename, index=False, header=True, sep='|')
datakursbi[1].to_csv(filename2, index=False, header=True, sep='|')


time.sleep(5)

driver.close()
