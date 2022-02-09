from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import datetime

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options,executable_path="D:\HERI\python\project\sample-app-selenium\chromedriver.exe")
# print(driver.title)

# time.sleep(5) : waktu tunggu
driver.implicitly_wait(10) #: waktu tunggu untuk driver menemukan element (global)

# https://cfs.ojk.go.id/cfs
# https://cfs.ojk.go.id/cfs/Report.aspx?BankTypeCode=UUS&amp;BankTypeName=Unit%20Usaha%20Syariah
# driver.get("https://cfs.ojk.go.id/cfs/Report.aspx?BankTypeCode=BUK&amp;BankTypeName=Conventional%20Bank")

driver.page_source
# time.sleep(5)

# print(datetime.datetime.now().time())
# element = driver.find_element_by_xpath('//*[@id="ctl00_PlaceHolderMain_g_b08cad05_9bd3_4661_83be_6f4f432cd22d_ctl00_ListViewInfo_ctrl0_HyperLinkInfo"]')

# presence of element located 
# visibility of element located 
#WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID,"CFSReportViewer_ct109")))
#element = driver.find_element_by_xpath('//*[@id="ext-gen1018"]/div[1]/p').text

# element = driver.find_element_by_xpath('//*[@id="DeltaBreadcrumbDropdown"]/ul/li/ul/li/ul/li/ul/li/ul/li/ul/li/a').get_attribute('href')
# element = driver.find_element(By.XPATH,'//*[@id="DeltaBreadcrumbDropdown"]/ul/li/ul/li/ul/li/ul/li/ul/li/ul/li/a').get_attribute('href')

# element = driver.find_element_by_xpath('//*[@id="ctl00_PlaceHolderSearchArea_g_b97e9dc2_f8c2_434c_bd07_78f57bc202f3_csr_sbox"]')
# element.clear()
# element.send_keys('test')
# time.sleep(5)
# print(element)

#element = driver.find_element_by_id('BankCode-inputEl')
#element = driver.find_element_by_link_text('Bisnis')

# time.sleep(5)
# 002-PT BANK RAKYAT INDONESIA (PERSERO), Tbk
# element = driver.find_element_by_xpath('//*[@id="tab-1013-btnInnerEl"]')
# element = driver.find_element_by_link_text('Bisnis')
# element.click()
# driver.execute_script("arguments[0].click()",element)
# print(element)


time.sleep(10)

# <div id="ReportPageTitle" style="height: 100%;">Laporan Publikasi Bank Umum Konvensional</div>

# <input type="button" id="R-inputEl" class="x-form-field x-form-radio x-form-cb" autocomplete="off" hidefocus="true" aria-invalid="false" data-errorqtip="">
# <label id="R-boxLabelEl" class="x-form-cb-label x-form-cb-label-after" for="R-inputEl">Triwulanan</label>
# element = driver.find_element_by_id('R-inputEl')

element = driver.find_element_by_xpath('//*[@id="R-inputEl"]')
element.click()
# driver.execute_script("arguments[0].click()",element)
time.sleep(5)

# element2 = driver.find_element_by_xpath('//*[@id="BankCode-inputEl"]')
# element.click()
#driver.execute_script("arguments[0].value='002-PT BANK RAKYAT INDONESIA (PERSERO), Tbk'",element2)

#<tr role="row" id="treeview-1012-record-PGWS-908-99999A" data-boundview="treeview-1012" data-recordid="PGWS-908-99999A" data-recordindex="8" class="x-grid-row x-grid-row-selected x-grid-tree-node-leaf x-grid-data-row x-grid-row-focused" tabindex="-1"><td role="gridcell" class="x-grid-cell x-grid-td x-grid-cell-treecolumn-1011 x-grid-cell-treecolumn x-grid-cell-first x-grid-cell-last x-unselectable x-grid-cell-treecolumn" id="ext-gen1138"><div unselectable="on" class="x-grid-cell-inner x-grid-cell-inner-treecolumn" style="text-align:left;"><img src="data:image/gif;base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" class=" x-tree-elbow-img x-tree-elbow-end"><input type="button" role="checkbox" aria-checked="true" class=" x-tree-checkbox x-tree-checkbox-checked"><img src="data:image/gif;base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" class=" x-tree-icon x-tree-icon-leaf "><span class="x-tree-node-text ">Susunan Pengurus Bank / Pimpinan KCBA di Indonesia / Pemilik                                        </span></div></td></tr>
time.sleep(5)
element3 = driver.find_element_by_xpath('//*[@id="ext-gen1094"]/div/input')
driver.execute_script("arguments[0].click()",element3)

time.sleep(5)

# element = driver.find_element_by_id('R-boxLabelEl')
# element.click()


driver.close()

