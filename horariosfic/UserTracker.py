import socket
import psycopg2
import calendar
import time

conn = psycopg2.connect(database="horariosfic",
                        host="192.168.1.158",
                        user="postgres",
                        password="hola123",
                        port="5433")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('socket', 5000)
server.connect(server_address)
server.send(b'00025sinittrack')

def fill(data):
    data = str(data)
    aux = str(len(data))
    while len(aux) < 5:
        aux = '0' + aux
    return aux

def track(user_info):
    ip = user_info[0]
    service = user_info[1]
    current_GMT = time.gmtime()
    timestamp = str(calendar.timegm(current_GMT))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_tracker (ip, service_requested, request_timestamp) VALUES ('" + ip + "', '" + service + "','" + timestamp + "')")
    conn.commit()
    datos = "EVENTO TRACKEADO"
    aux = fill(len(datos+ 'clien'))
    msg = aux + 'clien' + datos
    server.sendall(bytes(msg,'utf-8'))
    pass


print("Iniciado TRACKING SERVICE")
recibido=server.recv(4096)
print("TRACKING SERVICE: "+recibido.decode('utf-8'))

while True:
    datos=server.recv(4096)
    print(datos)
    query = datos.decode()[11:].split("-")
    transaction_type = query[0]
    payload = query[1:]
    print("guatefac")
    print(payload)
    if transaction_type == "track":
        track(payload)
    else:
        print("XD")