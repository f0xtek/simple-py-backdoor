# Simple Python Backdoor

A simple client-server backdoor utility to run commands on target machines for enumerating system information.

This will continually evolve to accept more commands/functionality.

## Usage

Server:

```
usage: server.py [-h] --address ADDRESS --port PORT

optional arguments:
  -h, --help         show this help message and exit
  --address ADDRESS  The IP address to listen on
  --port PORT        The port to listen on
```

```
$ python3 server.py --address 127.0.0.1 --port 44444
Server started! Waiting for connections...
Client connected with address: ('127.0.0.1', 56589)
```

Client:

```
usage: client.py [-h] --address ADDRESS --port PORT

optional arguments:
  -h, --help         show this help message and exit
  --address ADDRESS  The IP address to connect to
  --port PORT        The port to connect on
```

```
$ python3 client.py --address 127.0.0.1 --port 44444
Connection established!


0) Close the connection
1) Get system info
2) List directory contents

Please select an option: 1
macOS-11.1-x86_64-i386-64bit x86_64


0) Close the connection
1) Get system info
2) List directory contents

Please select an option: 2
Please enter a directory path: /tmp
****************************************

fseventsd-uuid
com.google.Keystone
powerlog
com.apple.launchd.N111bv8NuP
.BBE72B41371180178E084EEAF106AED4F350939DB95D3516864A1CC62E7AE82F
vmware-luke
aws-toolkit-vscode
tmux-501
****************************************
```