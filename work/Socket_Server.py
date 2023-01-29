import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(15)
print(f'Server {HOST}:{PORT} start.')

def listen_user(user):
    while True:
        client_message = user.recv(1024).decode('utf-8')
        if client_message == 'file':
            break
        print(f'{client_message}')
        user.send('get message'.encode('utf-8'))

    user.send('start send file'.encode('utf-8'))
    with open('data.txt','r') as file_object:
        count = 0
        for line in file_object:
            count += 1
            user.send(line.rstrip().encode('utf-8'))
            if 'next' == user.recv(1024).decode('utf-8'):
                continue
        user.send('finish'.encode('utf-8'))

def start_socket():
    while True:
        user_socket, addr = server.accept()
        potok_info = threading.Thread(target=listen_user, args=(user_socket, ))
        potok_info.start()

if __name__ == '__main__':
    start_socket()