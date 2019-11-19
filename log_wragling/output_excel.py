from typing import List,Set,Dict
from config import FILENAME_DICT
class Element:
	def __init__(self,name:str,server_name:str,target_sheet:str,score:int,summary:str):
		self.name:str=name
		self.target_sheet:str=target_sheet
		self.server_name_set:Set=set()
		self.server_name_set.add(server_name)
		self.summary=summary

	def add(self,serer_name:str):
		self.server_name_set.add(server_name)
	def  get_server_name(self):



def exe(fname:str):
	with open(fname,"r",encoding="utff-8")as reader:
		#skip first line ,header
		reader.read()
		for line in reader:
			tmp:List=line.replace("\n","").split("\t")


if __name__=="__main__":
