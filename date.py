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
}
# response1  = requests.get("https://finance.futunn.com/api/finance-v2/company-info?code=XLNX&label=us&_=1578969470940",headers=headers1)
code="XLNX"
timestamp=time.time()
print(timestamp)
str="https://finance.futunn.com/api/finance-v2/income-statement?market=us&code=XLNX&quarter=6&time=&size=4&flag=0&date=&_={time}".format(companyname=code,time=timestamp)
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
pprint(response1.json())

engine=create_engine("mysql+pymysql://root:1234@192.168.99.100:3306/tufu", max_overflow=5)
DBsession=sessionmaker(bind=engine)
session=DBsession()

dict=response1.json()
pprint(dict['data']['list']['title'][-1])
pprint(dict['data']['list']['title'][3])

initUrl="https://finance.futunn.com/api/finance-v2/income-statement?market=us&code=XLNX&quarter=6&time=&size=4&flag=0&date=&_=1579181629649"
startDict=requests.get(initUrl,headers=headers1).json()
test=startDict['data']['hasMore']

def repeat(test,startDict):
    if test == True:
        str = startDict['data']['list']['title'][-1]
        print(str[4:14])
        print("hello%s,%s,%s" % (str[4:8], str[9:11], str[12:14]))
        url = "https://finance.futunn.com/api/finance-v2/income-statement?market=us&code=XLNX&quarter=6&time=&size=4&flag=0&date={year}%2F{month}%2F{date}&_={time}".format(
            companyname=code, time=timestamp, year=str[4:8], month=str[9:11], date=str[12:14])
        try:
            values = startDict['data']['list']['values']
            for index in values:
                new_income = incomeReport()
                new_income.PeriodEndingDate = index[0]['value']
                new_income.TotalRevenue = index[1]['value']
                new_income.GrossProfit = index[2]['value']
                new_income.NetNonOperatingInterestIncomeExpense = index[3]['value']
                new_income.TotalExpenses = index[4]['value']
                new_income.CostOfRevenue = index[5]['value']
                new_income.SellingGeneralAndAdministration = index[6]['value']
                new_income.ResearchAndDevelopment = index[7]['value']
                new_income.DepreciationAmortizationDepletion = index[8]['value']
                new_income.OperatingIncome = index[9]['value']
                new_income.OtherIncomeExpense = index[10]['value']
                new_income.PretaxIncome = index[11]['value']
                new_income.TaxProvision = index[12]['value']
                new_income.NetIncome = index[13]['value']
                new_income.NetIncomeCommonStockholders = index[14]['value']
                new_income.NetIncomeIncludingNoncontrollingInterests = index[15]['value']
                new_income.NetIncomeContinuousOperations = index[16]['value']
                new_income.BasicEPS = index[17]['value']
                new_income.DilutedEPS = index[18]['value']
                new_income.DividendPerShare = index[19]['value']
                new_income.InterestIncome = index[20]['value']
                new_income.DepreciationAndAmortization = index[21]['value']
                new_income.InterestExpense = index[22]['value']
                new_income.OperatingRevenue = index[23]['value']
                new_income.OperatingExpense = index[24]['value']
                new_income.InterestIncomeNonOperating = index[25]['value']
                new_income.InterestExpenseNonOperating = index[26]['value']
                new_income.TotalOtherFinanceCost = index[27]['value']
                new_income.OtherNonOperatingIncomeExpenses = index[28]['value']
                new_income.NetInterestIncome = index[29]['value']
                new_income.Amortization = index[30]['value']
                new_income.CurrencyUnit = index[31]['value']
                new_income.AccountingStandards = index[32]['value']
                new_income.AuditorReport = index[33]['value']
                new_income.Company = 'XLNX'
                session.add(new_income)
                session.commit()
        except(Exception):
            pprint(Exception)
        finally:
            session.close()
        result = requests.get(url=url, headers=headers1).json()
        test = result['data']['hasMore']
        startDict = result
        pprint(result)
        repeat(test,startDict)
    else:
        startDict=None
        quit()

repeat(test,startDict)
# while test==True:
#     str=startDict['data']['list']['title'][-1]
#     print(str[4:14])
#     print("hello%s,%s,%s"%(str[4:8],str[9:11],str[12:14]))
#     url="https://finance.futunn.com/api/finance-v2/income-statement?market=us&code=XLNX&quarter=6&time=&size=4&flag=0&date={year}%2F{month}%2F{date}&_={time}".format(companyname=code,time=timestamp,year=str[4:8],month=str[9:11],date=str[12:14])
#     result=requests.get(url=url,headers=headers1)
#     test=result['data'['hasMore']]
#     startDict=result
#     pprint(result.json())