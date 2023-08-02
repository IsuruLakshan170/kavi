import socket
import threading
import time

isNewMessage = False
message1 = "hello"


# test message test
def testMessages():
    global isNewMessage, message1
    for i in range(20):
        isNewMessage = True
        message1 = f"hello{i}"
        time.sleep(2)


# mannually disconnect
def closedSocket():
    print("")


class SocketConnection:
    is_client_connected = False

    def _init_(self, client_socket, client_address):
        self.client_socket = client_socket
        self.client_address = client_address

    def handle_connection(self):
        # Mark as connected
        SocketConnection.is_client_connected = True
        print(f"\033[34mServer: Connection established with {self.client_address}\033[0m")

        # Start the thread to handle incoming messages from the client
        read_thread = threading.Thread(target=self.receive_messages)
        read_thread.start()

        # Start the thread to send messages to the client
        send_thread = threading.Thread(target=self.send_message)
        send_thread.start()

        # testing ---send  message--------------------------
        send_thread = threading.Thread(target=testMessages)
        send_thread.start()

    def close_connection(self):
        # Reset the connected status when the client disconnects
        SocketConnection.is_client_connected = False
        self.client_socket.close()
        print(f"Server: Connection closed with {self.client_address}")

    def send_message(self):
        global isNewMessage, message1
        try:
            while self.client_socket.fileno() != -1:  # Check if the socket is still valid
                if isNewMessage:
                    self.client_socket.sendall((message1 + '\n').encode())
                    isNewMessage = False
                time.sleep(0.1)  # Add a small delay to avoid tight loop when no messages to send

        except ConnectionResetError:
            # This exception will be raised when the client closes the connection
            pass

        # finally:
        #     self.close_connection("Send")

    def receive_messages(self):
        try:
            while True:
                data = self.client_socket.recv(1024).decode()
                if not data:
                    break  # Client has disconnected

                print(f"`Server`: Received message from {self.client_address}: {data}")

        except ConnectionResetError:
            # This exception will be raised when the client closes the connection
            pass
        finally:
            self.close_connection()


def main():
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 9999  # Choose any available port number

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Server: Listening for incoming connections...")

        while True:
            client_socket, client_address = server_socket.accept()

            if not SocketConnection.is_client_connected:  # Check if another client is already connected
                # Create a SocketConnection object for this client
                socket_connection = SocketConnection(client_socket, client_address)
                socket_connection.handle_connection()

            else:
                # Reject the connection if another client is already connected
                rejection_message = "FAILD"
                client_socket.sendall(rejection_message.encode())
                client_socket.close()
                print(f"\033[31mServer: Connection request from {client_address} rejected. Another client is already connected.\033[0m")

    except KeyboardInterrupt:
        print("Server: Server terminated by user.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()