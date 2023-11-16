import socket
import pickle

class Network:
    def __init__(self):
        # Crea un socket del cliente
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Define el host y el puerto al que el cliente se conectará
        server_ip = "192.168.56.1"
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
        
    def send(self, data):
        """
        Intenta enviar datos al servidor y luego espera una respuesta.
        Los datos recibidos del servidor se deserializan antes de ser devueltos.
        """
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(f"Error al enviar/recibir datos: {e}")
            return None
