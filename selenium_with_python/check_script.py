from selenium import webdriver
#動作確認用
path_to_chromedriver="/usr/local/bin"

# 起動(path_to_chromedriverにはchromedriverのバイナリファイルのパスを入力)
driver = webdriver.Chrome(executable_path=path_to_chromedriver) 
# https://www.google.co.jpを開く
driver.get("https://www.google.co.jp/") 
