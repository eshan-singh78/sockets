import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("127.0.0.1", 4444))
print("Connection established")

try:
    while True:
        mess = connection.recv(1024).decode()
        print("Server:", mess)
        
        if mess.strip().lower() == "exit":
            print("Server has terminated the connection.")
            break
        else:
            command1 = input(">>> ")
            connection.send(command1.encode())
finally:
    connection.close()
