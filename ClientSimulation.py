import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        # 发送摇骰子的指令
        s.sendall(b"roll 6 dice")
        # 接收响应
        data = s.recv(1024)
        print('Received:', data.decode())

if __name__ == '__main__':
    start_client()