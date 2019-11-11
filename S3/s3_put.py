import boto3

def put_s3(bucket_name:str,fname:str):

	s3 = boto3.resource('s3')

	data = open(fname, 'rb')
	result=s3.Bucket(bucket_name).put_object(Key=fname, 
	Body=data)
	print(result)

if __name__=="__main__":
	put_s3('bucket_name',"hogehoge.jpg")