from selenium import webdriver
import time
#動作確認用,chrome-verを確認する
path_to_chromedriver="chromedriver"

# 起動(path_to_chromedriverにはchromedriverのバイナリファイルのパスを入力)
driver = webdriver.Chrome(executable_path=path_to_chromedriver) 
# https://www.google.co.jpを開く
driver.get("https://www.google.co.jp/") 
search_box=driver.find_element_by_name("q")
search_box.send_keys("タピオカ")
search_box.submit()
print(driver.title)
time.sleep(3)
driver.quit()