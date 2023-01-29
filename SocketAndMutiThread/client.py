from socket import socket
from json import loads
from base64 import b64decode
import socket
import time
import threading
import os
"""
def main():

    client = socket()
    
    client.connect(('127.0.0.1', 9999))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('D:/python/SocketAndMutiThread/pic/' + filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存.')

if __name__ == '__main__':
    main()
""" 
HOST = '127.0.0.1'
PORT = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
in_data = bytes()

def send_message():

   #if('Name' in client.recv(1024).decode('utf-8')): # If 'Name' received. It allows you to send the name.
   name  = input('Enter Name : ') # Type name
   client.send(name.encode('utf-8'))

   while True:
       data = input('Enter : ') # Enter message
       client.send(data.encode('utf-8'))
    
       receive = client.recv(1024).decode('utf-8')# Receive messages from other clients.
       print(receive)

def send_server():

   listen_thread = threading.Thread(target=send_message)
   listen_thread.start()      

if __name__ == '__main__':
   os.system('clear')
   print('***** Welcome in Security Chat. *****')
   send_server()