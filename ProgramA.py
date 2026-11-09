# Program Name: ProgramA.py
# Course: IT3883/Section W01
# Student Name: Maryam Adigun Hammed
# Assignment Number: 4
# Due Date: Nov 6,2026
# Purpose: Send a message to Program B and display
# the uppercase response.
# Resources: Python socket documentation and ChatGPT assistance.

import socket

# Set the server address and port
server_ip = "127.0.0.1"
server_port = 45000

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to Program B
client.connect((server_ip, server_port))

# Ask the user to enter a message
message = input("Enter a message: ")

# Send the message to Program B
client.sendall(message.encode("utf-8"))

# Receive the uppercase response
response = client.recv(1024).decode("utf-8")

# Display the response
print("Response from server:", response)

# Close the socket
client.close()