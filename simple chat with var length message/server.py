from socket import *

s = socket(AF_INET, SOCK_STREAM)
print("[*] socket created")

ip = '127.0.0.1' #loop back
port = 1025

s.bind((ip, port))
print(f"[*] socket is binded to {port}")
s.listen(5)
print("[*] Server is listening")

c, addr = s.accept()
print(f"[*] connection received from {addr}")

while True:
    # Receive the length of the message (fixed size: 10 bytes)
    length_data = c.recv(10)
    length = int(length_data.decode('utf-8'))

    # Receive the message with variable length
    received_message = c.recv(length).decode('utf-8')
    print("Client : " + received_message)

    # close the cession if q is pressed otherwise collect length from data
    x = input('Server : ')
    if x == 'q':
        print('[*] Bye, server disconnect')
        c.close()
        break

    # Send the length of the message (fixed size: 10 bytes)
    message_data = x.encode('utf-8')
    message_length = str(len(message_data)).zfill(10).encode('utf-8')
    c.send(message_length)

    # Send the actual message
    c.send(message_data)
c.close()