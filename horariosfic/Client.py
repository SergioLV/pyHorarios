import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('socket', 5000)
server.connect(server_address)
server.send(b'00019sinitclien')
recibido=server.recv(4096)

def track(service):
    # ESTA IP DEBERIA OBTENERSE DESDE EL FRONT
    ip = socket.gethostbyname(socket.gethostname())

    datos = " track-"+ ip +"-"+service
    aux = fill(len(datos+ 'track'))
    msg = aux + 'track' + datos
    server.sendall(bytes(msg,'utf-8'))

def fill(data):
    data = str(data)
    aux = str(len(data))
    while len(aux) < 5:
        aux = '0' + aux
    return aux

while True:
    main_menu = False
    print("""
    ==========HORARIOSFIC==========
    Seleccione un servicio:
        1. Newsletter
        2. Feedback
        3. Cursos
        4. Evaluations
        5. Mailing
    ==============================
    """)
    opcion = input("OPCION: ")
    if opcion == '1':
        print("""
    ==========NEWSLETTER==========
    Seleccione un servicio:
        1. Suscribirse
        2. Envio Masivo
    ==============================
    """)
        opt = input("NEWSLETTER: ")
        if opt == '1':
            email = input("Ingrese su correo: ")


            datos = " add-"+ email
            aux = fill(len(datos+ 'newsl'))
            msg = aux + 'newsl' + datos
            server.sendall(bytes(msg,'utf-8'))
            recibido=server.recv(4096)
            track("newsl")
            if recibido.decode('utf-8').find('clien')!=-1:
                print(recibido)
        elif opt == '2':
            mensaje = input("Ingrese las buenas nuevas: ")
            datos = " send-"+ mensaje
            aux = fill(len(datos+ 'newsl'))
            msg = aux + 'newsl' + datos
            server.sendall(bytes(msg,'utf-8'))
            recibido=server.recv(4096)
            track("newsl")
            if recibido.decode('utf-8').find('clien')!=-1:
                print(recibido)
    elif opcion == '2':
        type = input("Tipo de feedback: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        carrera = input("Carrera: ")
        email = input("Email: ")
        comentario = input("Comentario: ")
        datos = " comment-"+type+"-"+nombre+"-"+apellido+"-"+carrera+"-"+email+"-"+comentario
        aux = fill(len(datos+ 'feedb'))
        msg = aux + 'feedb' + datos
        server.sendall(bytes(msg,'utf-8'))
        recibido=server.recv(4096)
        track("feedb")
        if recibido.decode('utf-8').find('clien')!=-1:
            print(recibido)
    elif opcion == '3':
        print("""
    ==========COURSES==========
    Seleccione un servicio:
        1. Obtener Horario
        2. Oferta
    ===========================
    """)
        opt = input("OPCION: ")
        if opt == '1':
            curso = input("Curso: ")
            datos = " getcourse-"+curso
            aux = fill(len(datos+ 'cours'))
            msg = aux + 'cours' + datos
            server.sendall(bytes(msg,'utf-8'))
            recibido=server.recv(4096)
            track("cours")
            if recibido.decode('utf-8').find('clien')!=-1:
                print(recibido)
        elif opt == '2':
            datos = " getoferta"
            aux = fill(len(datos+ 'cours'))
            msg = aux + 'cours' + datos
            server.sendall(bytes(msg,'utf-8'))
            recibido=server.recv(4096)
            track("cours")
            if recibido.decode('utf-8').find('clien')!=-1:
                print(recibido)
    elif opcion == '4':
            mensaje = input("Ingrese la carrera: ")
            datos = " geturl-"+ mensaje
            aux = fill(len(datos+ 'evalu'))
            msg = aux + 'evalu' + datos
            server.sendall(bytes(msg,'utf-8'))
            recibido=server.recv(4096)
            track("evalu")
            if recibido.decode('utf-8').find('clien')!=-1:
                print(recibido)
    elif opcion == '5':
        correo = input("Ingrese correo: ")
        mensaje = input("Ingrese el contenido: ")
        datos = " send-"+ correo + "-"+ mensaje
        aux = fill(len(datos+ 'maili'))
        msg = aux + 'maili' + datos
        server.sendall(bytes(msg,'utf-8'))
        recibido=server.recv(4096)
        track("maili")
        if recibido.decode('utf-8').find('clien')!=-1:
            print(recibido)


