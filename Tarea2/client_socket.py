import socket

HEADER = 64
PORT = 80
SERVER = '158.251.91.68'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT!'
#------------asociacion al socket--------------------------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)
#--------------Envio de mensajes---------------------
def send(msg):
    message=msg.encode(FORMAT) # se codidifica el mensaje en utf-8 y se guarda en message

    msg_length = len(message) #len devuelve el largo de la variable, por lo que el largo queda guardado en msg_length
    send_length = str(msg_length).encode(FORMAT) #se envia el largo, como devuelve entero se convierte a string, y se codifica en el formato utf-8
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length) #primero se manda el largo
    client.send(message)  # y aca se manda el mensaje
    print(client.recv(2048).decode(FORMAT)) #como el servidor tambien me va a estar mandando informacion, se imprime a funcion recibir


send('hello')
#input()
send('funciona?')
#input()
send('adios')
#input()
send(DISCONNECT_MESSAGE)
