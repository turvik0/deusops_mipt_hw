from flask import Flask
import pymysql
import json
import os

app = Flask(__name__)

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
port = int(os.getenv('DB_PORT'))
password = os.getenv('MYSQL_ROOT_PASSWORD')
db_name = os.getenv('DB_NAME')
table_name = os.getenv('TABLE_NAME')



def beautify(results, column_names):
    data_list = []
    for row in results:
        data_dict = dict(zip(column_names, row))
        data_list.append(data_dict)
    return json.dumps(data_list)


def get_data_from_db(host, port, user, password, db_name, table_name):
    try:
        print('Try to connect')
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
        )
        cursor = connection.cursor()
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"SELECT * FROM {table_name}")

        results = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        connection.commit()
        cursor.close()
        connection.close()

        return beautify(results, column_names)

    except Exception as e:
        raise e


@app.route("/", methods=['GET'])
def get_data():
    return get_data_from_db(host, port, user, password, db_name, table_name)


@app.route("/health", methods=['GET'])
def health_check():
    return {"status": "OK"}

