import csv
import pymysql
import os

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
port = int(os.getenv('DB_PORT'))
password = os.getenv('MYSQL_ROOT_PASSWORD')
db_name = os.getenv('DB_NAME')
table_name = os.getenv('TABLE_NAME')


def set_connection(host, port, user, password, database_name, table_name):
    try:
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
        )

        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        cursor.execute(f"USE {database_name}")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (name VARCHAR(228),age INTEGER)")
        cursor.execute("FLUSH TABLES")


        cursor.execute('SHOW DATABASES')
        dbs = cursor.fetchall()
        print('\nEXISTING DataBases \n')
        for idx, db in enumerate(dbs):
            print(f"Database {idx}: {db[0]}")

        cursor.execute('SHOW TABLES')
        tbls = cursor.fetchall()
        print('\nEXISTING Tables \n')
        for idx, tbl in enumerate(tbls):
            print(f"Table {idx}:{tbl[0]}")

    except Exception as e:
        raise e

    return connection, cursor


def fill_database(table_name):
    try:
        connection, cursor = set_connection(host, port, user, password, db_name, table_name)

        with open("data.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                name = row["name"]
                age = int(row["age"])
                cursor.execute(f"INSERT INTO {table_name} (name,age) VALUES (%s,%s)", (name,age))


        print(f"\nTHE ENTIRE CONTENTS OF THE TABLE {table_name} \n")
        cursor.execute(f"SELECT * FROM {table_name}")
        results = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        for row in results:
            print(dict(zip(column_names,row)))

        connection.commit()
        cursor.close()
        connection.close()

    except Exception as e:
        raise e


if __name__ == "__main__":
    fill_database(table_name)
