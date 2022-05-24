import socket

host = "192.168.210.243" # ip // my phone
port = 7000

def client():
    clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) # server socket open 
    clientSocket.connect((host, port))

    # GET method 
    # clientSocket.sendall(b"GET /test.txt HTTP/1.1\r\nHost: 192.168.210.243\r\n\r\n")
    # recieve_message=clientSocket.recv(1024)
    # print(recieve_message.decode()) 

    # clientSocket.sendall(b"GET /tst.txt HTTP/1.1\r\nHost: 192.168.210.243\r\n\r\n")
    # recieve_message=clientSocket.recv(1024)
    # print(recieve_message.decode()) 

    # # HEAD method 
    # clientSocket.sendall(b"HEAD /test.txt HTTP/1.1\r\nHost: 192.168.210.243\r\n\r\n")
    # recieve_message=clientSocket.recv(1024)
    # print(recieve_message.decode())
    
    # clientSocket.sendall(b"HEAD /tst.txt HTTP/1.1\r\nHost: 192.168.210.243\r\n\r\n")
    # recieve_message=clientSocket.recv(1024)
    # print(recieve_message.decode())

    # POST
    clientSocket.sendall(b"POST /test.txt HTTP/1.1\r\nHost: 192.168.210.243\r\n\r\n")
    recieve_message=clientSocket.recv(1024)
    print(recieve_message.decode())

    clientSocket.close()

if __name__ == '__main__':
    client()