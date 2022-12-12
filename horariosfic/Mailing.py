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
server.send(b'00024sinitmaili')

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

def sendMail(email, mail_content):
    track("mailing")
    sender_address = 'horariosfic@gmail.com'
    sender_pass = 'mfatbcxzhwkvluox'
    # Obtener suscritos desde la base de datos
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
    datos = "HORARIO ENVIADO"
    aux = fill(len(datos+ 'clien'))
    msg = aux + 'clien' + datos
    server.sendall(bytes(msg,'utf-8'))


print("Iniciado Mailing")
recibido=server.recv(4096)
print("Mailing: "+recibido.decode('utf-8'))


while True:
    datos=server.recv(4096)
    print(datos)
    query = datos.decode()[11:].split("-")
    transaction_type = query[0]
    payload = query[1:]
    if transaction_type == "sendMail":
        sendMail(payload[0], payload[1])
    else:
        print("XD")