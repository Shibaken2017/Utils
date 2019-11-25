import boto3
from boto3.session import Session 
import os


def upload(site_id:int,target:str):
	if target=="stage":
		bucket_name=''
	elif target=="develop":
		bucket_name='t'
	else:
		raise Exception("targetはstage or developのみ")
	profile=target
	session=Session(profile_name=profile)
	s3 = session.resource('s3') #S3オブジェクトを取得
	target_dir=str(site_id)
	fnames=os.listdir(target_dir)
	bucket = s3.Bucket(bucket_name)
	for fname in  fnames:
		print(fname)
		bucket.upload_file(os.path.join(target_dir,fname), 'scraper/scraping/{}/{}'.format(site_id,fname))

if __name__=="__main__":
	target_site_id=[7]
	for site_id in target_site_id:
		print(site_id)
		upload(site_id,"stage")
