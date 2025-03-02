# Import pandas
import pandas as pd
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

def get_data_for_provider(data, INN):
    data_for_provider = data[data["Участники КС - поставщики"].str.contains(str(INN))]
    return data_for_provider

def get_count_of_participations(data, INN, period=0):
    data_for_provider = get_data_for_provider(data, INN)
    if (period == 0):
        return data_for_provider["Id КС"].nunique()
    elif(period == 1):
        count = 0
        current_date = datetime.now()
        year = timedelta(365)
        date_year_ago = current_date - year
        data_for_provider_unique = data_for_provider.drop_duplicates(subset=["Id КС"])
        for i in range(len(data_for_provider_unique)):
            list_data = data_for_provider_unique["Начало КС"].to_list()
            if(list_data[i] >= pd.to_datetime(date_year_ago)): #datetime.strptime(date, "%Y-%m-%d")
                count += 1
        return count
    elif (period == 2):
        count = 0
        current_date = datetime.now()
        month = timedelta(31)
        date_month_ago = current_date - month
        data_for_provider_unique = data_for_provider.drop_duplicates(subset=["Id КС"])
        for i in range(len(data_for_provider_unique)):
            list_data = data_for_provider_unique["Начало КС"].to_list()
            if(list_data[i] >= pd.to_datetime(date_month_ago)):
                count += 1
        return count
    else:
        count = 0
        current_date = datetime.now()
        week = timedelta(7)
        date_week_ago = current_date - week
        data_for_provider_unique = data_for_provider.drop_duplicates(subset=["Id КС"])
        for i in range(len(data_for_provider_unique)):
            list_data = data_for_provider_unique["Начало КС"].to_list()
            if(list_data[i] >= pd.to_datetime(date_week_ago)):
                count += 1
        return count

def get_count_of_wins(data, INN, period=0):
    data_of_wins = data[data["ИНН победителя КС"] == INN]
    if(period == 0):
        return data_of_wins["Id КС"].nunique()
    elif(period == 1):
        count = 0
        current_date = datetime.now()
        year = timedelta(365)
        date_year_ago = current_date - year
        data_of_wins_unique = data_of_wins.drop_duplicates(subset=["Id КС"])
        for i in range(len(data_of_wins_unique)):
            list_data = data_of_wins_unique["Начало КС"].to_list()
            if(list_data[i] >= pd.to_datetime(date_year_ago)):
                count += 1
        return count
    elif(period == 2):
        count = 0
        current_date = datetime.now()
        month = timedelta(31)
        date_month_ago = current_date - month
        data_of_wins_unique = data_of_wins.drop_duplicates(subset=["Id КС"])
        for i in range(len(data_of_wins_unique)):
            list_data = data_of_wins_unique["Начало КС"].to_list()
            if(list_data[i] >= pd.to_datetime(date_month_ago)):
                count += 1
        return count
    else:
        count = 0
        current_date = datetime.now()
        week = timedelta(7)
        date_week_ago = current_date - week
        data_of_wins_unique = data_of_wins.drop_duplicates(subset=["Id КС"])
        for i in range(len(data_of_wins_unique)):
            list_data = data_of_wins_unique["Начало КС"].to_list()
            if(list_data[i] >= pd.to_datetime(date_week_ago)):
                count += 1
        return count

def get_customer_variability(data, INN, period = 0):
    data_for_provider = get_data_for_provider(data, INN)
    if (period == 0):
        customer_variability = (get_data_for_provider(data, INN))["ИНН заказчика"].nunique()
        return customer_variability
    elif (period == 1):
        count = 0
        current_date = datetime.now()
        year = timedelta(365)
        date_year_ago = current_date - year
        data_for_provider_unique = data_for_provider.drop_duplicates(subset=["ИНН заказчика"])
        for i in range(len(data_for_provider_unique)):
            list_data = data_for_provider_unique["Начало КС"].to_list()
            if(list_data[i] >= pd.to_datetime(date_year_ago)):
                count += 1
        return count
    elif(period == 2):
        count = 0
        current_date = datetime.now()
        month = timedelta(31)
        date_month_ago = current_date - month
        data_for_provider_unique = data_for_provider.drop_duplicates(subset=["ИНН заказчика"])
        for i in range(len(data_for_provider_unique)):
            list_data = data_for_provider_unique["Начало КС"].to_list()
            if(list_data[i] >= pd.to_datetime(date_month_ago)):
                count += 1
        return count
    else:
        count = 0
        current_date = datetime.now()
        week = timedelta(7)
        date_week_ago = current_date - week
        data_for_provider_unique = data_for_provider.drop_duplicates(subset=["ИНН заказчика"])
        for i in range(len(data_for_provider_unique)):
            list_data = data_for_provider_unique["Начало КС"].to_list()
            if(list_data[i] >= pd.to_datetime(date_week_ago)):
                count += 1
        return count

def get_region_variability(data, INN, period=0):
    data_for_provider = get_data_for_provider(data, INN)
    if (period == 0):
        region_variability = data_for_provider["Регион победителя КС"].nunique()
        print(data_for_provider["Регион победителя КС"].to_list())
        return region_variability

def get_share_of_victories(data, INN, period=0):
    if (get_count_of_participations(data, INN, period) != 0):
        return round(get_count_of_wins(data, INN, period)/get_count_of_participations(data, INN, period) * 100, 1)
    return 0

file = 'data.xlsx'
data = pd.read_excel('data.xlsx')
INN_provider = int("501306807502")
period = 0

print("Количество участий = " + str(get_count_of_participations(data, INN_provider, period)))
print("Количество побед = " + str(get_count_of_wins(data, INN_provider, period)))
print("Доля побед = " + str(get_share_of_victories(data, INN_provider, period)))
print("Вариативность заказчиков = " + str(get_customer_variability(data, INN_provider, period)))
print("Вариативность регионов = " + str(get_region_variability(data, INN_provider, period)))

# PANEAPPLE

from abc import ABC, abstractmethod

# Базовый класс фильтра
class Filter(ABC):
    @abstractmethod
    def apply(self, data):
        pass

# Конкретные фильтры
class KpgzFilter(Filter):
    def __init__(self, kpgz):
        self.kpgz = kpgz

    def apply(self, data):
        return data[data["Код КПГЗ"].str.startswith(self.kpgz)]

class RegionFilter(Filter):
    def __init__(self, region):
        self.region = region

    def apply(self, data):
        return data[data["Регион победителя КС"] == self.region]

class InnFilter(Filter):
    def __init__(self, inn):
        self.inn = inn

    def apply(self, data):
        return data[data["ИНН победителя КС"] == self.inn]

class DateFilter(Filter):
    def __init__(self, dateStart=year_ago, dateEnd=today):
        self.dateStart = dateStart
        self.dateEnd = dateEnd

    def apply(self, data):
        data = data[data["Начало КС"] > self.dateStart]
        return data[data["Окончание КС"] < self.dateEnd]
    
class InnSupplierFilter(Filter):
    def __init__(self, inn_s):
        self.inn_s = inn_s

    def apply(self, data):
        return data[data["ИНН победителя КС"] == self.inn_s]

class InnCustomerFilter(Filter):
    def __init__(self, inn_c):
        self.inn_c = inn_c

    def apply(self, data):
        return data[data["ИНН заказчика"] == self.inn_c]

data['Начало КС'] = pd.to_datetime(data['Начало КС'])
data['Окончание КС'] = pd.to_datetime(data['Окончание КС'])

for i in range (len(data['ИНН победителя КС'])): 
  
    data['ИНН победителя КС'][i] = str(data['ИНН победителя КС'][i])
    data['ИНН заказчика'][i] = str(data['ИНН заказчика'][i])

    if (len(data['ИНН победителя КС'][i])==11 or len(data['ИНН победителя КС'][i])==9):
        data['ИНН победителя КС'][i] = "0"+data['ИНН победителя КС'][i]
        #print(df['ИНН победителя КС'][i])

    if(len(data['ИНН заказчика'][i])==9):
        data['ИНН заказчика'][i] = "0"+data['ИНН заказчика'][i]
    
def getCustomers(data, kpgz, isMoney, isKC_count):
    cust = KpgzFilter(kpgz).apply(DateFilter().apply(data))
    cust_inn = cust["ИНН заказчика"].unique()

    if (isMoney):
        sum = []
        for i in range (len(cust_inn)):
            s=0
            d_money = InnCustomerFilter(cust_inn[i]).apply(cust)
            for index, row in d_money.iterrows():
                s+= row["Количество СТЕ"]*row["Цена оферты за единицу"]
            sum.append(s)  

    jsn = []
    titles = []
    for i in range (len(cust_inn)):
        name = data.loc[data['ИНН заказчика'] == cust_inn[i], 'Наименование заказчика'].iloc[0]
        region = data.loc[data['ИНН заказчика'] == cust_inn[i], 'Регион заказчика'].iloc[0]
        if (isMoney):
            if (isKC_count):
                kc_count = cust['Id КС'].nunique()
                jsn.append([[kpgz],[cust_inn[i]],[name],[region],[sum[i]],[kc_count]])
                titles = ['Код КПГЗ','ИНН заказчика', 'Наименование заказчика', 'Регион заказчика', 'Денежный оборот за период','Количество проведенных КС']
        
            else:
                jsn.append([[kpgz],[cust_inn[i]],[name],[region],[sum[i]]])
                titles = ['Код КПГЗ','ИНН заказчика', 'Наименование заказчика', 'Регион заказчика', 'Денежный оборот за период']
        
        
        elif(isKC_count):
            kc_count = cust['Id КС'].nunique()
            jsn.append([[kpgz],[cust_inn[i]],[name],[region], [kc_count]])
            titles = ['Код КПГЗ','ИНН заказчика', 'Наименование заказчика', 'Регион заказчика','Количество проведенных КС']
        
        else:
            jsn.append([[kpgz],[cust_inn[i]],[name],[region]])
            titles = ['Код КПГЗ','ИНН заказчика', 'Наименование заказчика', 'Регион заказчика']     

    return titles, jsn
# END

# ROUTER
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/api/count_of_participation', methods=['GET', 'POST'])
def count_of_participation():
    response_object = {'status': 'not success'}
    if request.method == 'POST':
        response_object["status"] = ["succcess"]
        post_data = request.get_json()
        response_object["count_of_participation"] = get_count_of_participations(data, post_data["INN"], int(post_data["period"]))
    return jsonify(response_object)

@app.route('/api/count_of_wins', methods=['GET', 'POST'])
def count_of_wins():
    response_object = {'status': 'not success'}
    if request.method == 'POST':
        response_object["status"] = ["succcess"]
        post_data = request.get_json()
        response_object["count_of_wins"] = get_count_of_wins(data, post_data["INN"], int(post_data["period"]))
    return jsonify(response_object)

@app.route('/api/share_of_victories', methods=['GET', 'POST'])
def share_of_victories():
    response_object = {'status': 'not success'}
    if request.method == 'POST':
        response_object["status"] = ["succcess"]
        post_data = request.get_json()
        response_object["share_of_victories"] = get_share_of_victories(data, post_data["INN"], int(post_data["period"]))
    return jsonify(response_object)

@app.route('/api/customer_variability', methods=['GET', 'POST'])
def customer_variability():
    response_object = {'status': 'not success'}
    if request.method == 'POST':
        response_object["status"] = ["succcess"]
        post_data = request.get_json()
        response_object["customer_variability"] = get_customer_variability(data, post_data["INN"], int(post_data["period"]))
    return jsonify(response_object)

@app.route('/api/get_customers', methods=['GET', 'POST'])
def get_customers():
    response_object = {'status': 'not success'}
    if request.method == 'POST':
        response_object["status"] = ["succcess"]
        post_data = request.get_json()
        response_object["title"], response_object["customers"] = getCustomers(data, post_data["kpgz"], post_data["isMoney"], post_data["isKC_count"])
    return jsonify(response_object)



if __name__ == '__main__':
    app.run()