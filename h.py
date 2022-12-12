import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import psycopg2

conn = psycopg2.connect(database="horariosfic",
                        host="192.168.1.158",
                        user="postgres",
                        password="hola123",
                        port="5433")



def get(email):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM newsletter")
    cursor.fetchall()
    print(cursor)
    pass