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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('socket', 5000)
server.connect(server_address)
server.send(b'00022sinitcours')

def fill(data):
    data = str(data)
    aux = str(len(data))
    while len(aux) < 5:
        aux = '0' + aux
    return aux

def getCourse(course):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM informatica_2022_2 WHERE nombre_asig = '" + course + "';")
    datos = cursor.fetchall()
    res = ""
    # LISTO
    print("DATOS")
    print(datos)
    for course in datos:
        print("COURSE")
        print(course)
        res += str(course) + ","

    aux = fill(len(res+ 'clien'))
    print("RES")
    print(res)
    msg = aux + 'clien' + res
    server.sendall(bytes(msg,'utf-8'))
    pass

def getAll(course):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM informatica_2022_2 ")
    datos = cursor.fetchall()
    # res = ""
    # for i in datos:
    #     res+=res.join(str(x) for x in i)
    aux = fill(len(datos+ 'clien'))
    msg = aux + 'clien' + datos
    server.sendall(bytes(msg,'utf-8'))
    pass


print("Iniciado Courses")
recibido=server.recv(4096)
print("Courses: "+recibido.decode('utf-8'))

while True:
    datos=server.recv(4096)
    print(datos)
    query = datos.decode()[11:].split("-")
    transaction_type = query[0]
    payload = query[1]
    if transaction_type == "getcourse":
        getCourse(payload.replace("\n",""))
    elif transaction_type == "getoferta":
        getAll(query[1])
    else:
        print("XD")