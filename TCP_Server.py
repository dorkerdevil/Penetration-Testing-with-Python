import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

#this is our client-handeling thread

def handle_client(client_socket):
    #print out what client sends
    request = client_socket.recv(4098)
    print"[*] Recieved: %s" % request

    #send back a packet
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client,addr = server.accept()
    print "[*] Accept connection from: %s:%d" % (addr[0],addr[1])

    #spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,arg=(client,))
    client_handle.start()
