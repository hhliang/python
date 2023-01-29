import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def connect_server():
    while True:
        message = input('請輸入訊息:')
        client.send(message.encode('utf-8'))
        sever_message = client.recv(1024).decode('utf-8')
        if sever_message == 'start send file':
            break;
        print(f'{sever_message}')
    
    log1 = []
    log2 = []

    while True:       
        file_data = client.recv(1024).decode('utf-8')
        if file_data == 'finish':
            break;  
        client.send('next'.encode('utf-8'))
        arr = file_data.split(',')
        #print(file_data)
        if arr[0] == 'qwer':
             log1.append(file_data)
        if arr[0] == 'asdf':
            log2.append(file_data)
    
    a1 = threading.Thread(target=job, args=(log1, ))
    a2 = threading.Thread(target=job, args=(log2, ))
    a1.start()
    a2.start()
    
def job(arr):
    with open('log.txt', 'a') as file_object:
       for str in arr:
            file_object.write(f'{str},{threading.get_ident()}\n')
     #print(f'{arr},{threading.get_ident()}')   

#def connect_server():
    #listen_server = threading.Thread(target='get_file')
    #listen_server.start()

if __name__ == '__main__':
    print('***Welcome***')
    connect_server()
