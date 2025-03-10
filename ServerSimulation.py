import socket
import random

def roll_dice(num_dice):
    """Simulate rolling num_dice six-sided dice."""
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print("Received:", data)
                if data == "roll 6 dice":
                    # Call the roll_dice function and send the result back
                    dice_results = roll_dice(6)
                    response = f"摇出的骰子点数为: {dice_results}"
                else:
                    response = "未知指令"
                conn.sendall(response.encode())

if __name__ == '__main__':
    start_server()