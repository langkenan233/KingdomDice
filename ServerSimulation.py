import socket
# 模拟服务器
def start_server(host='127.0.0.1', port=65432):
    # 创建一个socket对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 绑定socket到指定的IP和端口
        s.bind((host, port))
        # 开始监听传入连接
        s.listen()
        print(f"Server listening on {host}:{port}")
        # 接受一个新的连接
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                # 接收数据
                data = conn.recv(1024)
                if not data:
                    break
                print("Received:", data.decode())
                # 发送数据
                conn.sendall(data)

if __name__ == '__main__':
    start_server()