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
server.send(b'00023sinitevalu')

def fill(data):
    data = str(data)
    aux = str(len(data))
    while len(aux) < 5:
        aux = '0' + aux
    return aux

def track(service):
    ip = socket.gethostbyname(socket.gethostname())
    datos = " track-"+ ip +"-"+service
    aux = fill(len(datos+ 'track'))
    msg = aux + 'track' + datos
    server.sendall(bytes(msg,'utf-8'))

def getEvaluations(carreer):
    track("evaluations")
    # DEBERIA DEVOLVER LA URL Y NO LA ESTA DEVOLVIENDO
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM evaluations WHERE carreer = '" + carreer + "';")
    datos = cursor.fetchone()
    aux = fill(len(datos[0]+ 'clien'))
    msg = aux + 'clien' + datos[0]
    server.sendall(bytes(msg,'utf-8'))
    pass


print("Iniciado Evaluations")
recibido=server.recv(4096)
print("Evaluations: "+recibido.decode('utf-8'))

while True:
    datos=server.recv(4096)
    print(datos)
    query = datos.decode()[11:].split("-")
    transaction_type = query[0]
    payload = query[1]
    print("tr type: " + payload)
    if transaction_type == "geturl":
        getEvaluations(payload.replace("\n",""))
    else:
        print("XD")