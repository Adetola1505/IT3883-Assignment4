# Program Name: ProgramB.py
# Course: IT3883/Section W01
# Student Name: Maryam Adigun Hammed
# Assignment Number: 4
# Due Date: Nov 6,2026
# Purpose: Receive a message, convert it to uppercase,
# and send it back to the client.
# Resources: Python socket documentation and ChatGPT assistance.

import socket

# Set up the server address and port
server_ip = "127.0.0.1"
server_port = 45000

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket and start listening
server.bind((server_ip, server_port))
server.listen(1)

print("Server is waiting for a connection...")

# Accept a connection from Program A
connection, address = server.accept()
print("Connected to:", address)

# Receive the message and convert it to text
message = connection.recv(1024).decode("utf-8")

# Convert the message to uppercase
uppercase_message = message.upper()

# Send the uppercase message back
connection.sendall(uppercase_message.encode("utf-8"))

# Close the connection and server
connection.close()
server.close()