from argparse import ArgumentParser, Namespace
import socket
import os
import platform


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('--address',
                        dest='address',
                        type=str,
                        required=True,
                        help='The IP address to listen on')
    parser.add_argument('--port',
                        dest='port',
                        type=int,
                        required=True,
                        help='The port to listen on')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((args.address, args.port))
    s.listen(1)

    print("Server started! Waiting for connections...")

    conn, addr = s.accept()
    print(f"Client connected with address: {addr}")

    while 1:
        try:
            data = conn.recv(1024)
        except Exception:
            continue

        if data.decode('utf-8') == '1':
            tosend = f"{platform.platform()} {platform.machine()}"
            conn.sendall(tosend.encode())
        elif data.decode('utf-8') == '2':
            data = conn.recv(1024)
            try:
                directory_list = os.listdir(data.decode('utf-8'))
                tosend = ""
                for item in directory_list:
                    tosend += "," + item
            except Exception:
                tosend = "Invalid path!"
            conn.sendall(tosend.encode())
        elif data.decode('utf-8') == '0':
            conn.close()
            conn, addr = s.accept()
            break
