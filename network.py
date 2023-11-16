import socket
import pickle

class Network:
    # Crea un socket del cliente
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define el host y el puerto al que el cliente se conectará
    server_ip = "192.168.1.15"
    server_port = 5555

    # Conecta el cliente al servidor
    client.connect((server_ip, server_port))

    player_id = pickle.loads(client.recv(2048))  # Recibe el ID del jugador desde el servidor
    print("Connected to the server as Player", player_id)

    # Lógica para manejar la entrada del usuario, por ejemplo, en un bucle de juego
    while True:
        # Implementa aquí la lógica del cliente según tus necesidades
        pass

    client.close()