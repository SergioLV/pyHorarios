import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('socket', 5000)
server.connect(server_address)
server.send(b'00019sinitclien')
recibido=server.recv(4096)

def track(service, req):
    ip = socket.gethostbyname(socket.gethostname())
    datos = " track-"+ ip +"-"+service
    aux = fill(len(datos+ 'track'))
    msg = aux + 'track' + datos
    print("Request to " + service)
    print("Request: " + req)
    server.sendall(bytes(msg,'utf-8'))

def printMenu(service, options):
    print("=========="+service+"==========")
    for idx, value in enumerate(options):
        print(str(idx+1)+". " + value)
    print("===============================")

def parseMessage(serviceAction, payload):
    res = " " + serviceAction
    for msg in payload:
        res+="-"+msg
    return res

def fill(data):
    data = str(data)
    aux = str(len(data))
    while len(aux) < 5:
        aux = '0' + aux
    return aux

def sendMessage(service, serviceAction, payload):
    datos = parseMessage(serviceAction, payload)
    aux = fill(len(datos+ service))
    msg = aux + service + datos
    server.sendall(bytes(msg,'utf-8'))
    recibido = server.recv(4096)

    track(service, msg)

    if recibido.decode('utf-8').find('clien')!=-1:
        print(recibido)
    pass

def newsletterSubscription():
    email = input("Ingrese su correo: ")
    sendMessage("newsl", "add", [email])

def sendNewsletter():
    news = input("News: ")
    sendMessage("newsl", "send", [news])

def feedback():
    type = input("Tipo de feedback: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    carrera = input("Carrera: ")
    email = input("Email: ")
    comentario = input("Comentario: ")
    sendMessage("feedb", "comment", [type, nombre, apellido, carrera, email, comentario])

def getHorario():
    curso = input("Curso: ")
    sendMessage("cours", "getcourse", [curso])

def getOferta():
    # VERIFICAR SI ES QUE ESTA BIEN
    datos = " getoferta"
    sendMessage("", "getcourse", [])

def evaluations():
    mensaje = input("Ingrese la carrera: ")
    sendMessage("evalu", "geturl", [mensaje])

def mailing():
    correo = input("Ingrese correo: ")
    mensaje = input("Ingrese el contenido: ")
    sendMessage("maili", "send", [correo, mensaje])

while True:
    main_menu = False
    printMenu("HORARIOSFIC", ["Newsletter", "Feedback", "Cursos", "Evaluations", "Mailing"])
    opcion = input("OPCION: ")
    if opcion == '1':
        printMenu("NEWSLETTER", ["Suscribirse", "Enviar Newsletter"])
        opt = input("OPCION: ")
        if opt == '1':
            newsletterSubscription()
        elif opt == '2':
            sendNewsletter()
    elif opcion == '2':
        feedback()
    elif opcion == '3':
        printMenu("COURSES", ["Obtener Horario", "Oferta"])
        opt = input("OPCION: ")
        if opt == '1':
            getHorario()
        elif opt == '2':
            getOferta()
    elif opcion == '4':
        evaluations()
    elif opcion == '5':
        mailing()



