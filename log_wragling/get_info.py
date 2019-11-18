from typing  import List,Set,Dict
import requests
import time
##getting data from api and write it on an output_file
#ERRATA_BASE_URL="https://access.redhat.com/errata/"
BASE_URL="https://access.redhat.com/hydra/rest/securitydata/cve.json?ids="

from config import ERRATA_BASE_URL,CVE_BASE_URL
import os


def exe(fname_list:str,output_fname):
	with open(output_fname,"w",encoding="utf-8")as writer:
		writer.write("log_name\tname\tscore\tcve_url\n")
	for fname in fname_list:
		output=get_name_from_log(fname)
		write_file(output_fname,output,fname)

def write_file(output_fname,dict_list,fname):
	with open(output_fname,"a",encoding="utf-8")as writer:
		for ele in dict_list:
			writer.write("{}\t{}\t{}\t{}\n".format(fname,ele["name"],ele["score"],ele["cve_url"]))

def get_name_from_log(fname:str):
	name_set:Set=set()
	count=0
	output_list:List=[]
	tmp_list=[]
	with open(fname,"r",encoding="utf-8")as reader:
		for line in reader:
			line=line.replace("\n","")

			#after a blank line ,there is a new set of info
			count=0 if len(line)==0 else count+1
			if count==2 and len(line.replace("=","")):
				name=line.replace("|","").replace(" ","")
				if name in name_set:
					continue
				name_set.add(name)
				tmp_list.append(name)
				if len(tmp_list)>50:
					print(tmp_list)
					output_list.extend(get_info_from_api(tmp_list))
					tmp_list=[]

	if len(tmp_list):
		output_list.extend(get_info_from_api(tmp_list))
	print(output_list)
	return output_list

def get_info_from_api(name_list:List):
	#sleep for not sending too many requests in short period time!!
	time.sleep(1)
	req_url=BASE_URL+",".join(name_list)
	print(req_url)
	res=requests.get(req_url).json()
	print(res)
	output_list=[]
	for ele in res:
		output_list.append(summarize_info(ele))
	return output_list

def summarize_info(response_ele:Dict):
	if "cvss3_score" in response_ele.keys():
		score=response_ele["cvss3_score"]
	elif "cvss_score" in response_ele.keys():
		score=response_ele["cvss_score"]
	else:
		raise Exception("key error at getting a score")
	#パッチを探す
#	url=response_ele["resource_url"]
#	print(url)
#	res=requests.get(url).json()
	#print(res)
#	advisory=None
#	if  "affected_release" in res.keys():
#		res_list=res["affected_release"]
#		#adivisory=None	
#		for ele in res_list:
#			if ele["product_name"]=="Red Hat Enterprise Linux 7":
#				advisory=ele["advisory"]
#				adivisory=os.path.join(ERRATA_BASE_URL,advisory)
#				break
#		
#	elif "package_state" in res.keys():
#		res_list=res["package_state"]
#		for ele in res_list:
#			if ele["product_name"]=="Red Hat Enterprise Linux 7":
#				advisory=ele["fix_state"]
#				break
	#else:
#		raise Exception("new key emrege!")

	cve_url=os.path.join(CVE_BASE_URL,response_ele["CVE"])
	output={"score":score,"name":response_ele["CVE"],"cve_url":cve_url}#,"adivisory":advisory}

	return output



def check_file(fname_list:List):
	for fname in fname_list:
		get_name_from_log(fname)

if __name__=="__main__":
	exe(["awx_web@prdcmg01_full.txt"],"tmp.tsv")
	#get_name_from_log("awx_web@prdcmg01_full.txt")
	#url="https://access.redhat.com/hydra/rest/securitydata/cve.json?ids=CVE-2019-11043"
	##name=["CVE-2015-6525"]
	#get_info_from_api(name)
	#tmp=["CVE-2016-3616"] 
	#get_info_from_api(tmp)
	#CVE-2015-6525  
	#https://access.redhat.com/hydra/rest/securitydata/cve.json?ids=CVE-2019-11139
#CVE-2015-6525