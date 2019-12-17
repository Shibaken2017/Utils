from selenium import webdriver
from datetime import datetime
import os
import time
from config import CONF, URLS
from selenium.webdriver.support.ui import Select

LOGIN_URL = "https://{}:{}@eservice.fujitsu.com/supportdesk/sdk/sdk?sv=0&lang=JA"


# url for basig authenticationa
# TODO:closeメソッド,headless-modeの追加


class Scraper:
    def __init__(self, driver_path: str = "chromedriver_79.exe"):
        self.driver = webdriver.Chrome(driver_path)
        print(type(self.driver))
        self.driver.implicitly_wait(30)
        self.__unixtime = datetime.now().timestamp()
        self.__save_dir = "screenshot_{}".format(self.__unixtime)
        os.mkdir(self.__save_dir)
        self.__count: int = 0

    def basic_authenticate(self, base_url: str, name: str, password: str):
        """log in by basic authentication"""
        self.driver.get(base_url.format(name, password))
        time.sleep(10)

    def login(self, url: str):
        """id,passwordを入力してログイン"""
        self.driver.get(url)
        self.driver.switch_to_alert()
        time.sleep(2)

    def check_page(self, url: str, name: str) -> None:
        self.driver.get(url)
        self.__save_screenshot(name)
    
    def check_middleware(self):
        """middlewareだけサイト構造違うのでメソッドを作成"""
        self.driver.get(URLS["middleware"])
        #　検索条件の追加
        self.driver.find_element_by_css_selector("a.btn").click()
        names = self.driver.find_elements_by_class_name("productname")
        select_name = Select(names[0])
        select_name.select_by_value("Systemwalker Centric Manager Standard Edition")

        systems = self.driver.find_elements_by_class_name("systemcode")
        select_system = Select(systems[0])
        select_system.select_by_value("515")

        generations = self.driver.find_elements_by_class_name("productverlev")
        select_generation=Select(generations[0])
        select_generation.select_by_value("V15.2.0")

        select_name = Select(names[1])
        select_name.select_by_value("Systemwalker Centric Manager Standard Edition")

        select_system = Select(systems[1])
        select_system.select_by_value("515")

        select_generation=Select(generations[1])
        select_generation.select_by_value("V13.6.0")

        self.driver.find_element_by_id("i_b_search").click()
        tables=self.driver.find_elements_by_css_selector("#list_area>div.stripe_2>table>tbody")
        print("tes###################")
        with open(self.__save_dir+"/output_middleware_{}.txt".format(self.__unixtime),"w",encoding="shift-jis")as writer:
            for ele in tables:
                writer.write(ele.text)
                writer.write("\n")
    





        






    def get_score(self, url: str, target_selector: str):
        # chromeのverが違うと動かないので要確認!
        print(url)
        self.driver.get(url)
        ele = self.driver.find_element_by_css_selector(target_selector)
        print("score:{}".format(ele.text))
        self.__save_screenshot()

    def __save_screenshot(self, name)->None:
        """save screenshot."""
        fname:str=os.path.join(self.__save_dir, name+"_"+str(self.__count) + ".png")
        print("screenshot:{}".format(fname))
        self.driver.save_screenshot(fname)
        self.__count += 1


if __name__ == "__main__":
    # test_url = "https://access.redhat.com/security/cve/CVE-2019-11043#cve-cvss-v3"
    # target_selector = "a.stat-card-left > span.stat-number"

    scraper = Scraper()

    scraper.basic_authenticate(LOGIN_URL, CONF["name"], CONF["password"])
    #scraper.check_page(URLS["oracle"],"oracle")
    #scraper.check_page(URLS["net_vault"],"net_vault")
    #scraper.check_page(URLS["vmware"],"vmware")
    scraper.check_middleware()
  
    # scraper.login("https://eservice.fujitsu.com/supportdesk/sdk/sdk?sv=0&lang=JA")
    # scraper.get_score(test_url, target_selector)


# driver = webdriver.Chrome("chromedriver.exe")
# driver.get("http://www.yahoo.co.jp")
