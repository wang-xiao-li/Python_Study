#get请求的接口自动化
import requests
url='http://39.97.98.53:8080/api/v1/test/xiaoliget002'
params=dict(id=123,name='hello王玉超')
a=requests.get(url,params=params)
print(a,a.json())
