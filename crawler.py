import requests
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from entity import incomeReport
from pprint import pprint
import datetime,time


headers1={
    'Host':'finance.futunn.com',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0) Chrome/71.0.3578.80 FutuNN_PC/9.19.7508 CliLang/zh-cn ClientSkinType/3',
    'Accept':'*/*',
    'Referer':'https://finance.futunn.com/?code=XLNX&market=us&skin=1&clienttype=10&direction=0',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
    'Cookie':'uid=156590; web_sig=yQJN2nldUiEMHI9tbrC8b9TGudSjezSUkZ9fcMa6Rt8DZD9TxHq3338c56aNheCoY3nVuE1Jm1NgwTU%2BpEO09t2Wd%2Fvd5kHXHLHJIi82ouw%3D; FUTU_TOOL_STAT_UNIQUE_ID=15782800059176578; cipher_device_id=1578280006825290; tgw_l7_route=8d34ab350eb9a9772a5a0c377f34d47d; PHPSESSID=t3gp4lj276s7538iao1emdblp7'
}
# response1  = requests.get("https://finance.futunn.com/api/finance-v2/company-info?code=XLNX&label=us&_=1578969470940",headers=headers1)
code="XLNX"
timestamp=time.time()
print(timestamp)
str="https://finance.futunn.com/api/finance-v2/company-info?code={companyname}&label=us&_={time}".format(companyname=code,time=timestamp)
response1 = requests.get(str,headers=headers1)
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)
# print(response.content)
# print(type(response.content))
print(response1.content.decode("utf-8"))
print(type(response1.content.decode("utf-8")))
print(response1.json())
