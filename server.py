import socket
from os.path import exists, getsize

port = 7000 # port number > 3000 // 
host = "192.168.210.243" # ip // my phone


def server():
    soc =  socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) # server socket open 
    soc.bind((host, port)) 
    soc.listen() # request 대기 

    while True:
        consoc,addr = soc.accept() # client로부터 연결
        message = consoc.recv(1024).decode() #client에게 요청된 메시지 수신
        request_data = message.split() # client로부터 request message를 받아와 split을 사용하여 쪼갬
        request_method = request_data[0] # method 내용이 포함된 0번째 index를 받아옴

        filename = './' + message.split('\r\n')[0].split(' ')[1]  # 요청한 파일의 이름을 request message에서 추출
        content_type = message.split('\r\n')[0].split(' ')[1].split('.')[1] # content-Type html,txt 등.. split을 통해 파일명에서 type 추출

        if request_method == "GET": # GET method 일때 
            if not exists(filename):  # 파일이 없는 경우
                msg = request_method + "\r\nHTTP/1.0 404 NOT FOUND\r\nHost:192.168.210.243"
                consoc.sendall(msg.encode())  # client에게 response message, 404에러 메시지 전송
                consoc.close()  # 연결 종료
                raise SystemError(":No File.") # Error 발생후 종료 
            else:  # 파일이 있는 경우
                size = getsize(filename)
                msg = request_method + "\r\nContent-Type:"+content_type+"; charset=UTF-8\r\nHTTP/1.0 200 OK\r\nHost:192.168.210.243\r\nContent-Length: %d" % size 
                f = open(filename, 'r',encoding="UTF-8")  #요청한 파일의 내용을 담기 
                data = ''
                for line in f:
                    data += line  # data에 내용 쓰기
                f.close() # 파일 닫기

                consoc.send(msg.encode())  # client에게 200 OK response message 전송
                consoc.send(data.encode()) # client에게 요청한 파일의 내용 전송
                consoc.close()  # 연결 종료

        if request_method=="HEAD":
            if not exists(filename):  # 파일이 없는 경우
                msg = request_method + "\r\nContent-Type:"+content_type+"; charset=UTF-8\r\nHTTP/1.0 404 NOT FOUND\r\nHost:192.168.210.243" # 본래 HTTP request문에서는 Request 출력이 없으나, 원활한 구분을 위해 사용
                consoc.sendall(msg.encode())  # client에게  404 response message 전송
                consoc.close()  # 연결 종료
                raise SystemError(":No File.") # Error 발생후 종료
            else:
                size = getsize(filename)
                msg = request_method + "\r\nContent-Type:"+content_type+"; charset=UTF-8\r\nHTTP/1.0 200 OK\r\nHost:192.168.210.243\r\nContent-Length: %d" % size  
                consoc.send(msg.encode())  # client에게 HEAD문 처리 성공 200 성공 response message 전송
                consoc.close()  # 연결 종료


        if request_method =="POST":
            nontype_filename = message.split('\r\n')[0].split(' ')[1].split('.')[0].split('/')[1] # file의 type을 제외한 이름만 저장
            f = open(nontype_filename+'.'+content_type, 'w') #실제 요청에 맞추어 파일 생성
            f.close()

            size=getsize(nontype_filename+'.'+content_type)
            msg = request_method + "\r\nContent-Type:"+content_type+"; charset=UTF-8\r\nHTTP/1.0 201 OK\r\nHost:192.168.210.243\r\nContent-Length: %d"% size

            consoc.send(msg.encode())  # client에게 POST문 처리 성공 201 성공 response message 전송
            consoc.close()  # 연결 종료


# server 시작 
if __name__ == '__main__':
    server()