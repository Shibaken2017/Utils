from selenium import webdriver
from datetime import datetime
import os


class Scraper:
	def __init__(self,driver_path:str="chromedriver.exe"):
		self.driver=webdriver.Chrome(driver_path)
		self.driver.implicitly_wait(30)
		unixtime=datetime.now().timestamp()
		self.__save_dir="screenshot_{}".format(unixtime)
		os.mkdir(self.__save_dir)

	def get_score(self,url:str,target_selector:str):
		
		#chromeのverが違うと動かないので要確認!
		print(url)
		self.driver.get(url)
		ele=self.driver.find_element_by_css_selector(target_selector)
		print(ele.text)


if __name__=="__main__":
	test_url="https://access.redhat.com/security/cve/CVE-2019-11043#cve-cvss-v3"
	target_selector="a.stat-card-left > span.stat-number"
	scraper=Scraper()
	scraper.get_score(test_url,target_selector)




 
#driver = webdriver.Chrome("chromedriver.exe")
#driver.get("http://www.yahoo.co.jp")