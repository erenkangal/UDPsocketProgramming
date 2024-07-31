import socket
import re  # Import the regular expression module

def udp_server():
    # List to store permitted numbers
    permitted_numbers = []

    client_addresses = set()

    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 5000))  # Binding to localhost and port 5000

    try:
        while True:
            # Receive data from client
            message, addr = server_socket.recvfrom(1024)
            message = message.decode('utf-8')
            print("Message:", message)
            print(f"Client Address: {addr}")

            client_addresses.add(addr)

            client_port = addr[1]
            response = "Port is not allowed to communicate"


                

            if client_port == 1234:
                # Match messages strictly starting with "Permission" followed by digits
                if re.fullmatch(r'Permission\d+', message, re.IGNORECASE):
                    number = ''.join(filter(str.isdigit, message))
                    if number in permitted_numbers:
                        response = "Already Permitted"
                    else:
                        permitted_numbers.append(number)
                        response = "Permission Accepted"
                else:
                    response = "Invalid Message"
            
            elif client_port == 3333:
                # Match messages strictly starting with "Request" followed by digits
                if re.fullmatch(r'Request\d+', message, re.IGNORECASE):
                    number = ''.join(filter(str.isdigit, message))
                    if number in permitted_numbers:
                        response = "Request Accepted"
                    else:
                        response = "Request Rejected"
                else:
                    response = "Invalid Message"

            # Send response to the client
            server_socket.sendto(response.encode('utf-8'), addr)

            if len(client_addresses) >= 4:
                print("The number of connected clients is: 4")
                break



    except KeyboardInterrupt:
        # Close the server socket gracefully when interrupted manually
        server_socket.close()

if __name__ == '__main__':
    udp_server()
