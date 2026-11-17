# Cliente Piedra, Papel o Tijera

Cliente en Python (Pygame) para jugar Piedra, Papel o Tijera en red entre dos jugadores. Se conecta por sockets TCP a un servidor que gestiona las partidas.

## Estructura

- `controller.py`: punto de entrada, bucle del juego y menú.
- `view.py`: ventana, botones y marcador.
- `network.py`: conexión con el servidor (sockets + `pickle`).

## Requisitos

- Python 3.10+
- Pygame: `pip install pygame`

## Uso

1. Ajusta `server_ip` y `server_port` en `network.py`.
2. Inicia el servidor (no incluido en este repositorio).
3. Ejecuta el cliente en cada jugador:

```bash
python controller.py
```

## Cómo se juega

Haz clic para empezar, espera al oponente y elige Rock, Paper o Scissors. Al elegir ambos se muestra el resultado y el marcador (victorias, empates y derrotas) se actualiza.

## CI

Cada push a `main` ejecuta un análisis con SonarQube (requiere los secretos `SONAR_TOKEN` y `SONAR_HOST_URL`).
