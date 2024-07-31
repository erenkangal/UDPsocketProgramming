import socket

def udp_client():
    # Ask user for the client port number
    client_port = int(input("Enter port no: "))

    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(('localhost', client_port))  # Bind to localhost and the user-defined port

    while True:
        while True:
            # Get message from user
            message = input("Enter a message: ")
            # Send the message to the server
            client_socket.sendto(message.encode('utf-8'), ('localhost', 5000))

            # Receive response from server
            response, _ = client_socket.recvfrom(1024)
            response = response.decode('utf-8')
            print(response)

            # If certain response is received, close the socket
            if response == "Port is not allowed to communicate":
                client_socket.close()
                return

            # If response indicates an invalid message, ask for message again
            if response != "Invalid Message":
                break

if __name__ == '__main__':
    udp_client()