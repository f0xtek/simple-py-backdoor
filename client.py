import socket
from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('--address',
                        dest='address',
                        type=str,
                        required=True,
                        help='The IP address to connect to')
    parser.add_argument('--port',
                        dest='port',
                        type=int,
                        required=True,
                        help='The port to connect on')
    return parser.parse_args()


def print_menu():
    print("""\n\n0) Close the connection
1) Get system info
2) List directory contents""")


if __name__ == '__main__':
    args = parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.address, args.port))

    print("Connection established!")
    print_menu()

    while 1:
        message = input("\nPlease select an option: ")

        if message == '0':
            s.sendall(message.encode())
            data = s.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
        elif message == '1':
            s.sendall(message.encode())
            data = s.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
        elif message == '2':
            path = input("Please enter a directory path: ")
            s.sendall(message.encode())
            s.sendall(path.encode())
            data = s.recv(1024)
            data = data.decode('utf-8').split(",")
            print('*'*40)
            for d in data:
                print(d)
            print('*'*40)

        print_menu()
