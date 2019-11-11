from selenium import webdriver
import time
import os
import shutil
from datetime import datetime
import sys
FORMAT="%Y%m%d_%H%M%S"

args=sys.argv
query=args[1]
print(query)
TMP=datetime.now().strftime(FORMAT)#fmt
no=0
#動作確認用,chrome-verを確認してダウンローど
path_to_chromedriver="chromedriver"
if os.path.exists(TMP):
	shutil.rmtree(TMP)

os.mkdir(TMP)#path



# 起動(path_to_chromedriverにはchromedriverのバイナリファイルのパスを入力)
driver = webdriver.Chrome(executable_path=path_to_chromedriver) 
# https://www.google.co.jpを開く
driver.get("https://www.google.co.jp/") 
driver.implicitly_wait(30)
driver.maximize_window()
driver.save_screenshot(TMP+"/"+str(no)+".png")
no+=1

search_box=driver.find_element_by_name("q")
search_box.clear()
search_box.send_keys(query)
driver.save_screenshot(TMP+"/"+str(no)+".png")
no+=1
search_box.submit()
driver.save_screenshot(TMP+"/"+str(no)+".png")
no+=1
print(driver.title)

driver.find_element_by_css_selector("div.rc a").click()
driver.save_screenshot(TMP+"/"+str(no)+".png")
no+=1
time.sleep(3)#secs

driver.quit()



