from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread
import threading
import socket

"""
def main():
    
    # 自定义线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'apple.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建套接字对象并指定使用哪种传输服务
    server1 = socket()
    server2 = socket()
    # 2.绑定IP地址和端口(区分不同的服务)
    server1.bind(('127.0.0.1', 9999))
    server2.bind(('127.0.0.1', 1234))
    # 3.开启监听 - 监听客户端连接到服务器
    server1.listen(512)
    server2.listen(512)
    print('服务器启动开始监听...')
    with open('apple.jpg', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server1.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()
"""
HOST = '127.0.0.1'
PORT = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(15)
print(f'Server {HOST}:{PORT} start.')

users = [] # To store their name
sort = [] # To store their socket

def listen_user(user):
    print('Listening user')
    #sort.append(user)  # Store their socket in sort[]
    #user.send('Name'.encode('utf-8')) # send 'Name' to clients
    name = user.recv(1024).decode('utf-8') # Receive their name
    users.append(name) # Store their name in user[]

    while True:
        data = user.recv(1024).decode('utf-8')
        print(f'{name} sent {data} {threading.get_ident()}{threading.current_thread().ident}')
        user.send('abc'.encode('utf-8'))
        #for i in sort: # Send received messages to clients
           #if(i != server and i != user): # Filter server and message sender. Send message except them.
               #i.sendall(f'{name} > {data}'.encode('utf-8'))
   
    user.close() # To close client socket connection.

def start_server():
    while True:
       user_socket, addr = server.accept()
       potok_info = threading.Thread(target=listen_user, args=(user_socket, ))
       potok_info.start()


if __name__ == '__main__':
    start_server()