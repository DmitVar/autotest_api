import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("Server started on ws://localhost:12345")

    while True:
        #Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"Client connected from {client_address}")
        #Получаем данные от клиента
        data = client_socket.recv(1024).decode()
        print(f"Received {data}")
        #Отправляем ответ клиенту
        response = f"Сервер получил, {data}!"
        client_socket.send(response.encode())
        client_socket.close()
if __name__ == "__main__":
    server()
