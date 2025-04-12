import socket 
import threading

desoll=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
desoll.bind(("localhost",1337))
desoll.setblocking(False)
desoll.listen(5)
print("work")

clients = []

def sans():
    global clients
    while True:

        for a in clients:
            try:
                print("o_o", a.recv(1024).decode())
            except:
                pass

threading.Thread(target=sans).start()


def papirus():
    global clients
    while True:
        s = input()
        for a in clients:
            try:
                a.send(s.encode())
            except:
                pass


threading.Thread(target=papirus).start()


while 1:
    try:
        connect,  addres= desoll.accept()

        print("принял клиента :" ,addres )
        connect.setblocking(False)
        # print(addres)
        
        clients.append(connect)
    except:
        pass 

    
            

#command=connection.recv(1024).decode()
#print(command)
#if command == "HELP":
#connection.send(f"Привет {command}".encode())

#connection.close()
#desoll.close