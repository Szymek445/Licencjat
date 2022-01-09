import pandas as pd 
import numpy as np 
from urllib.request import urlopen
from urllib.error import HTTPError
import json
API_KEY = 'd2aaf7b071cdcc2e04fb7188b7e0ffe4'


def available_companies(api_key):
    
    response = urlopen(f"https://financialmodelingprep.com/api/v3/stock/list?apikey={api_key}")
    data = json.loads(response.read().decode("utf-8"))
    
    if 'Error Message' in data:
        raise ValueError(data['Error Message'])

    df = pd.DataFrame(data)
    df.loc[df["name"].isna(), "name"] = df["symbol"]
    df = df[df['type']=='stock']
    df = df[df['exchangeShortName'] == 'NYSE']
#     Uncoment for nasdaq
#     df = df[df['exchangeShortName'] == 'NASDAQ']
    list_of_companies = df['symbol'].values.tolist()

    
    return list_of_companies


list_of_stock = available_companies(API_KEY)





class Data:


    def cash_flow_statement(ticker, api_key, period="annual", limit=0):

        URL = (f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}"
                f"?period={period}&limit={limit}&apikey={api_key}")

        response = urlopen(URL)
        data = json.loads(response.read().decode("utf-8"))

        if 'Error Message' in data:
            raise ValueError(data['Error Message'])

        data_formatted = {}
        for value in data:

            date = value['date'][:4]

            data_formatted[date] = value


        data_formatted1 = pd.DataFrame(data_formatted)
        data_formatted1 = data_formatted1.transpose()
        return data_formatted1


    def key_metrics(ticker, api_key, period="annual", limit=0):
              
        URL = f"https://financialmodelingprep.com/api/v3/key-metrics/{ticker}?period={period}&limit={limit}&apikey={api_key}"
       
        response = urlopen(URL)
        data = json.loads(response.read().decode("utf-8"))

        if 'Error Message' in data:
            raise ValueError(data['Error Message'])
       
        data_formatted = {}
        for value in data:            
            date = value['date'][:4]
            del value['date']

            data_formatted[date] = value
        
        data_formatted = pd.DataFrame(data_formatted)

        data_formatted = data_formatted.transpose()
        return data_formatted


    def financial_ratios(ticker, api_key, period="annual", limit=0):
        

        URL = f"https://financialmodelingprep.com/api/v3/ratios/{ticker}?period={period}&limit={limit}&apikey={api_key}"
        
        response = urlopen(URL)
        data = json.loads(response.read().decode("utf-8"))

        if 'Error Message' in data:
            raise ValueError(data['Error Message'])

        data_formatted = {}
        for value in data:

            date = value['date'][:4]
            del value['date']

            data_formatted[date] = value
        
        data_formatted = pd.DataFrame(data_formatted)
        
        data_formatted = data_formatted.transpose()

        return data_formatted


    def financial_statement_growth(ticker, api_key, period="annual", limit=0):
                
        response = urlopen(f"https://financialmodelingprep.com/api/v3/financial-growth/{ticker}"
                            f"?period={period}&limit={limit}&apikey={api_key}")
        data = json.loads(response.read().decode("utf-8"))


        if 'Error Message' in data:
            raise ValueError(data['Error Message'])

        data_formatted = {}
        for value in data:
            date = value['date'][:4]
            del value['date']

            data_formatted[date] = value
        data_formatted = pd.DataFrame(data_formatted)
        data_formatted = data_formatted.transpose()
        return data_formatted                                                             

    def discounted_cash_flow(ticker, api_key, period="annual", limit=0):
        
        response = urlopen(f"https://financialmodelingprep.com/api/v3/discounted-cash-flow/{ticker}"
                            f"?period={period}&limit={limit}&apikey={api_key}")
        data = json.loads(response.read().decode("utf-8"))


        if 'Error Message' in data:
            raise ValueError(data['Error Message'])

        data_json_current = data[0]

        try:
            del data_json_current['symbol']
            data_json_current['DCF'] = data_json_current.pop('dcf')
        except KeyError:
            pass

        
        response = urlopen(f"https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow/{ticker}"
                            f"?period={period}&apikey={api_key}")
        data = json.loads(response.read().decode("utf-8"))


        if 'Error Message' in data:
            raise ValueError(data['Error Message'])

        data_json = data[0]['historicalDCF']

        data_formatted = {}


        
        current_year = data_json_current['date'][:4]
        data_formatted[current_year] = data_json_current

        for data in data_json:    
            date = data['date'][:4]
            data_formatted[date] = data
        df = pd.DataFrame(data_formatted)
        df1 = df.transpose()
        return df1


    def end_data(ticker):
        pass


    def income_statement(ticker, api_key, period="annual", limit=0):

        URL = (f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}"
                f"?period={period}&limit={limit}&apikey={api_key}")

        
        response = urlopen(URL)
        data = json.loads(response.read().decode("utf-8"))


        if 'Error Message' in data:
            raise ValueError(data['Error Message'])

        data_formatted = {}
        for value in data:
            date = value['date'][:4]
            del value['date']
            del value['symbol']
            del value['fillingDate']        
            del value['acceptedDate']
            del value['period']
            del value['link']
            del value['finalLink']

            data_formatted[date] = value
        
        df = pd.DataFrame(data_formatted)
        df1 = df.transpose()
        
        return pd.DataFrame(df1)


    def balance_sheet_statement(ticker, api_key, period="annual", limit=0):
        
        URL = (f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}"
                f"?period={period}&limit={limit}&apikey={api_key}")
        
        response = urlopen(URL)
        data = json.loads(response.read().decode("utf-8"))

        if 'Error Message' in data:
            raise ValueError(data['Error Message'])

        data_formatted = {}
        for value in data:

            date = value['date'][:4]
            del value['date']
            del value['symbol']
            del value['fillingDate']        
            del value['acceptedDate']
            del value['period']
            del value['link']
            del value['finalLink']

            data_formatted[date] = value
        
        df = pd.DataFrame(data_formatted)
        df1 = df.transpose()

        return pd.DataFrame(df1)


    def cash_flow_statement(ticker, api_key, period="annual", limit=0):
        

        URL = (f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}"
                f"?period={period}&limit={limit}&apikey={api_key}")

        
        response = urlopen(URL)
        data = json.loads(response.read().decode("utf-8"))


        if 'Error Message' in data:
            raise ValueError(data['Error Message'])

        data_formatted = {}
        for value in data:

            date = value['date'][:4]
            del value['date']
            del value['symbol']
            del value['fillingDate']        
            del value['acceptedDate']
            del value['period']
            del value['link']
            del value['finalLink']

            data_formatted[date] = value

        df = pd.DataFrame(data_formatted)
        df1 = df.transpose()

        return pd.DataFrame(df1)





i = 0
while i < 40000:
    name = list_of_stock[i]
    name = str(name)
    try:
        df = Data.income_statement(name, API_KEY)
        df1 = Data.balance_sheet_statement(name, API_KEY)
        df2 = Data.cash_flow_statement(name, API_KEY)
        df3 = Data.discounted_cash_flow(name, API_KEY)
        df4 = Data.key_metrics(name, API_KEY)
        df5 = Data.financial_ratios(name, API_KEY)
        df6 = Data.financial_statement_growth(name, API_KEY)
        frame = pd.concat([df,df1,df2, df3, df4, df5], axis=1, join='inner')
        frame.to_csv(f"/home/sb/Python_Programing/Licencjat/NYSE/{name}")
    except:        

        pass
    i += 1
    print(i, " Company ticker:", name)



# print(Data.key_metrics('AAPL', API_KEY))
# print(Data.financial_ratios('AAPL', API_KEY))
