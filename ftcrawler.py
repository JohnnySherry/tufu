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
response1  = requests.get("https://finance.futunn.com/api/finance-v2/company-info?code=XLNX&label=us&_=1578969470940",headers=headers1)
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



headers2={
    'Host':'finance.futunn.com',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0) Chrome/71.0.3578.80 FutuNN_PC/9.19.7508 CliLang/zh-cn ClientSkinType/3',
    'Accept':'*/*',
    'Referer':'https://finance.futunn.com/?code=XLNX&market=us&skin=1&clienttype=10&direction=0',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
    'Cookie':'uid=156590; web_sig=yQJN2nldUiEMHI9tbrC8b9TGudSjezSUkZ9fcMa6Rt8DZD9TxHq3338c56aNheCoY3nVuE1Jm1NgwTU%2BpEO09t2Wd%2Fvd5kHXHLHJIi82ouw%3D; FUTU_TOOL_STAT_UNIQUE_ID=15782800059176578; cipher_device_id=1578280006825290; tgw_l7_route=8d34ab350eb9a9772a5a0c377f34d47d; PHPSESSID=t3gp4lj276s7538iao1emdblp7'
}

response2  = requests.get("https://finance.futunn.com/api/finance-v2/income-statement?market=us&code=XLNX&quarter=8&time=&size=4&flag=0&_=1578969473681",headers=headers1)
result=response2.json()
print(response2.json())
# pprint(response2.json())
pprint(type(response2.json()))

engine=create_engine("mysql+pymysql://root:1234@192.168.99.100:3306/tufu", max_overflow=5)
DBsession=sessionmaker(bind=engine)
session=DBsession()

# new_income=incomeReport(PeriodEndingDate='hello',Company='XLNX')
#
# session.add(new_income)
# session.commit()
# session.close

pprint(result['data']['list']['values'][0])
pprint(result['data']['list']['title'][3])
str=result['data']['list']['title'][3]
pprint(str[4:14])
values=result['data']['list']['values']
for index in values:
    new_income=incomeReport()
    new_income.PeriodEndingDate=index[0]['value']
    new_income.TotalRevenue=index[1]['value']
    new_income.GrossProfit=index[2]['value']
    new_income.NetNonOperatingInterestIncomeExpense=index[3]['value']
    new_income.TotalExpenses=index[4]['value']
    new_income.CostOfRevenue = index[5]['value']
    new_income.SellingGeneralAndAdministration=index[6]['value']
    new_income.ResearchAndDevelopment = index[7]['value']
    new_income.DepreciationAmortizationDepletion=index[8]['value']
    new_income.OperatingIncome=index[9]['value']
    new_income.OtherIncomeExpense=index[10]['value']
    new_income.PretaxIncome=index[11]['value']
    new_income.TaxProvision=index[12]['value']
    new_income.NetIncome = index[13]['value']
    new_income.NetIncomeCommonStockholders=index[14]['value']
    new_income.NetIncomeIncludingNoncontrollingInterests = index[15]['value']
    new_income.NetIncomeContinuousOperations = index[16]['value']
    new_income.BasicEPS=index[17]['value']
    new_income.DilutedEPS=index[18]['value']
    new_income.DividendPerShare=index[19]['value']
    new_income.InterestIncome=index[20]['value']
    new_income.DepreciationAndAmortization=index[21]['value']
    new_income.InterestExpense = index[22]['value']
    new_income.OperatingRevenue=index[23]['value']
    new_income.OperatingExpense = index[24]['value']
    new_income.InterestIncomeNonOperating=index[25]['value']
    new_income.InterestExpenseNonOperating=index[26]['value']
    new_income.TotalOtherFinanceCost=index[27]['value']
    new_income.OtherNonOperatingIncomeExpenses=index[28]['value']
    new_income.NetInterestIncome=index[29]['value']
    new_income.Amortization = index[30]['value']
    new_income.CurrencyUnit=index[31]['value']
    new_income.AccountingStandards= index[32]['value']
    new_income.AuditorReport= index[33]['value']
    new_income.Company = 'XLNX'
    session.add(new_income)
    session.commit()
    session.close


engine=create_engine("mysql+pymysql://root:1234@192.168.99.100:3306/tufu", max_overflow=5)

# conn=pymysql.connect(host='192.168.99.100',port=3306,user='root',passwd='1234',db='tufu')
# cursor=conn.cursor()
#
# cursor.execute("insert into income(PeriodEndingDate, TotalRevenue, GrossProfit, NetNonOperatingInterestIncomeExpense, TotalExpenses, CostOfRevenue, SellingGeneralAndAdministration, ResearchAndDevelopment, DepreciationAmortizationDepletion, OperatingIncome, OtherIncomeExpense, PretaxIncome, TaxProvision, NetIncome, NetIncomeCommonStockholders, NetIncomeIncludingNoncontrollingInterests, NetIncomeContinuousOperations, BasicEPS, DilutedEPS, DividendPerShare, InterestIncome, DepreciationAndAmortization, InterestExpense, OperatingRevenue, OperatingExpense, InterestIncomeNonOperating, InterestExpenseNonOperating, TotalOtherFinanceCost, OtherNonOperatingIncomeExpenses, NetInterestIncome, Amortization, CurrencyUnit, AccountingStandards, AuditorReport,Company)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", ("hi","I","am","johnny","hi","I","am","johnny","hi","I","am","johnny","hi","I","am","johnny","hi","I","am","johnny","hi","I","am","johnny","hi","I","am","johnny","hi","I","am","johnny","hello","everyone","XLNX"))
#
# conn.commit()
#
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()

# DBsession=sessionmaker(bind=engine)
# session=DBsession()
#
# new_income=incomeReport(PeriodEndingDate='hello',Company='XLNX')
#
# session.add(new_income)
# session.commit()
# session.close

def test():
    pprint("hello")

test()


