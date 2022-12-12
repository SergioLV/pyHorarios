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
server.send(b'00021sinitfeedb')

def fill(data):
    data = str(data)
    aux = str(len(data))
    while len(aux) < 5:
        aux = '0' + aux
    return aux
    
def addFeedback(feedback):
    cursor = conn.cursor()
    ft = feedback[0]
    fn = feedback[1]
    fln = feedback[2]
    fc = feedback[3]
    fe = feedback[4]
    fcomm = feedback[5].replace("\n","")
    current_GMT = time.gmtime()
    ftimestamp = str(calendar.timegm(current_GMT))
    cursor.execute("INSERT INTO feedback (feedback_type, feedbacker_name, feedbacker_last_name, feedbacker_career, feedbacker_email, feedback_comment, feedback_timestamp) VALUES ('" + ft + "', '" + fn + "', '" + fln + "', '" + fc + "', '" + fe + "', '" + fcomm + "', '" + ftimestamp + "')")
    conn.commit()
    datos = "FEEDBACK RECIBIDO"
    aux = fill(len(datos+ 'clien'))
    msg = aux + 'clien' + datos
    server.sendall(bytes(msg,'utf-8'))
    pass


print("Iniciado Feedback")
recibido=server.recv(4096)
print("Feedback: "+recibido.decode('utf-8'))



while True:
    datos=server.recv(4096)
    print(datos)
    query = datos.decode()[11:].split("-")
    transaction_type = query[0]
    payload = query[1:]
    if transaction_type == "comment":
        addFeedback(payload)
    else:
        print("XD")