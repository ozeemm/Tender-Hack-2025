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
            date, time = list_data[i].split(" ")
            if(datetime.strptime(date, "%Y-%m-%d") >= date_year_ago):
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
            date, time = list_data[i].split(" ")
            if(datetime.strptime(date, "%Y-%m-%d") >= date_month_ago):
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
            date, time = list_data[i].split(" ")
            if(datetime.strptime(date, "%Y-%m-%d") >= date_week_ago):
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
            date, time = list_data[i].split(" ")
            if(datetime.strptime(date, "%Y-%m-%d") >= date_year_ago):
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
            date, time = list_data[i].split(" ")
            if(datetime.strptime(date, "%Y-%m-%d") >= date_month_ago):
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
            date, time = list_data[i].split(" ")
            if(datetime.strptime(date, "%Y-%m-%d") >= date_week_ago):
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
            date, time = list_data[i].split(" ")
            if(datetime.strptime(date, "%Y-%m-%d") >= date_year_ago):
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
            date, time = list_data[i].split(" ")
            if(datetime.strptime(date, "%Y-%m-%d") >= date_month_ago):
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
            date, time = list_data[i].split(" ")
            if(datetime.strptime(date, "%Y-%m-%d") >= date_week_ago):
                count += 1
        return count

def get_share_of_victories(data, INN, period=0):
    if (get_count_of_participations(data, INN, period) != 0):
        return round(get_count_of_wins(data, INN, period)/get_count_of_participations(data, INN, period) * 100, 1)
    return 0

file = 'data.xlsx'
df_orders = pd.read_excel('data.xlsx')
INN_provider = int("027502460871")
period = 0

print("Количество участий = " + str(get_count_of_participations(df_orders, INN_provider, period)))
print("Количество побед = " + str(get_count_of_wins(df_orders, INN_provider, period)))
print("Доля побед = " + str(get_share_of_victories(df_orders, INN_provider, period)))
print("Вариативность заказчиков = " + str(get_customer_variability(df_orders, INN_provider, period)))

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/api/count_of_participation', methods=['GET', 'POST'])
def count_of_participation():
    response_object = {'status': 'not success'}
    if request.method == 'POST':
        response_object["status"] = ["succcess"]
        post_data = request.get_json()
        response_object["count_of_participation"] = get_count_of_participations(df_orders, post_data["INN"], int(post_data["period"]))
    return jsonify(response_object)

@app.route('/api/count_of_wins', methods=['GET', 'POST'])
def count_of_wins():
    response_object = {'status': 'not success'}
    if request.method == 'POST':
        response_object["status"] = ["succcess"]
        post_data = request.get_json()
        response_object["count_of_wins"] = get_count_of_wins(df_orders, post_data["INN"], int(post_data["period"]))
    return jsonify(response_object)

@app.route('/api/share_of_victories', methods=['GET', 'POST'])
def share_of_victories():
    response_object = {'status': 'not success'}
    if request.method == 'POST':
        response_object["status"] = ["succcess"]
        post_data = request.get_json()
        response_object["share_of_victories"] = get_share_of_victories(df_orders, post_data["INN"], int(post_data["period"]))
    return jsonify(response_object)

@app.route('/api/customer_variability', methods=['GET', 'POST'])
def customer_variability():
    response_object = {'status': 'not success'}
    if request.method == 'POST':
        response_object["status"] = ["succcess"]
        post_data = request.get_json()
        response_object["customer_vsriability"] = get_customer_variability(df_orders, post_data["INN"], int(post_data["period"]))
    return jsonify(response_object)



if __name__ == '__main__':
    app.run()