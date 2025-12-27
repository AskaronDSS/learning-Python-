import mysql.connector
from mysql.connector import errorcode

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='askaron250525',
    database='dz6'
)
if connection.is_connected():
    print("Успешное подключение к базе данных MySQL")

    # Здесь вы можете выполнять SQL-запросы с использованием курсора
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM your_table")
    # records = cursor.fetchall()
cursor = connection.cursor()

    # cursor.execute("""CREATE DATABASE users(
    #                id INT AUTO_INCREMENT PRIMERY KEY,
    #                username VARCHAR(255) UNIQUE NOT NULL,
    #                password VARCHAR(255) NOT NULL,
    #                email VARCHAR(255) UNIQUE NOT NULL)
    #                """)


