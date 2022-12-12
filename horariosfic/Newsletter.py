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
server.send(b'00020sinitnewsl')

def fill(data):
    data = str(data)
    aux = str(len(data))
    while len(aux) < 5:
        aux = '0' + aux
    return aux

# TODO conexion a la db

def getSubscribers():
    subs = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM newsletter")
    emails = cursor.fetchall()
    for email in emails:
        if email[1] == 1:
            subs.append(email[0])
    return subs

def sendMail(mail_content):
    sender_address = 'horariosfic@gmail.com'
    sender_pass = 'mfatbcxzhwkvluox'
    # Obtener suscritos desde la base de datos
    subs = getSubscribers()

    for email in subs:
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = email
        message['Subject'] = 'HorariosFic Newsletter!'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, email, text)
        session.quit()
    datos = "CORREOS ENVIADO"
    aux = fill(len(datos+ 'clien'))
    msg = aux + 'clien' + datos
    server.sendall(bytes(msg,'utf-8'))
    
    

def addSubscriber(email):
    cursor = conn.cursor()
    var = "true"
    cursor.execute("INSERT INTO newsletter (email, subscribed) VALUES ('" + email + "', '" + var + "')")
    conn.commit()
    datos = "USUARIO SUSCRITO"
    aux = fill(len(datos+ 'clien'))
    msg = aux + 'clien' + datos
    server.sendall(bytes(msg,'utf-8'))
    pass


print("Iniciado Newsletter")
recibido=server.recv(4096)
print("Newsletter: "+recibido.decode('utf-8'))



while True:
    datos=server.recv(4096)
    print(datos)
    query = datos.decode()[11:].split("-")
    transaction_type = query[0]
    payload = query[1]
    if transaction_type == "add":
        addSubscriber(payload.replace("\n",""))
    elif transaction_type == "send":
        sendMail(query[1])
    else:
        print("XD")