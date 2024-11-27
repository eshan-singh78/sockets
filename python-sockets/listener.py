import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 4444))
print("Listening on port 4444")
s.listen(1)

target, ip = s.accept()
print("Connection received from: ", ip)


while True:
    mes = input(f">>> {ip}: ")
    if mes.strip().lower() == "exit":
        target.send(mes.encode())
        print("Exiting...")
        break
    else:
        target.send(mes.encode())
        res = target.recv(1024)
        print("Client:", res.decode())

