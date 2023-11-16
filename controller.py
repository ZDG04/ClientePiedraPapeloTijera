import pygame
from network import Network
from view import scoreUpdate, redrawWindow,win, WIDTH, HEIGHT, btns

# Se mantiene el mismo código para la clase Button, scoreUpdate, y redrawWindow

# Crea una instancia de la clase Network para manejar la conexión con el servidor
n = Network()

# La función main ahora maneja la lógica del cliente
def main():
    run = True
    clock = pygame.time.Clock()

    player = int(n.getPlayer())  # Obtiene el jugador del servidor (0 o 1)
    print("You are Player ", player)

    scores = [0, 0, 0]

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get Game")
            break

        if game.bothGone():
            scoreUpdate(game, player, scores)
            redrawWindow(win, game, player, scores)
            pygame.time.delay(500)

            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 60)
            if (game.findWinner() == 1 and player == 1) or (game.findWinner() == 0 and player == 0):
                text = font.render("You Won!!!", 1, (0, 255, 0))
            elif game.findWinner() == -1:
                text = font.render("Game Tied", 1, (0, 0, 0))
            else:
                text = font.render("You Lost...", 1, (255, 0, 0))
            
            win.blit(text, (WIDTH/2 -text.get_width()/2, HEIGHT/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.isConnected():
                        if player == 0:
                            if not game.p1Gone:
                                n.send(btn.text)
                        else:
                            if not game.p2Gone:
                                n.send(btn.text)

        redrawWindow(win, game, player, scores)

# Función para el menú (landing page)
def menu():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font1 = pygame.font.SysFont("comicsans", 40)
        text1 = font1.render("Rock Paper Scissors", 1, (0, 0, 0))
        text2 = font1.render("Game", 1, (0, 0, 0))
        win.blit(text1, (WIDTH/2 -text1.get_width()/2, HEIGHT/2 - text1.get_height()/2 - 100))
        win.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT/2 - text2.get_height()/2 - 50))

        font = pygame.font.SysFont("comicsans", 50)
        text = font.render("Click to Play!!!", 1, (255, 0, 0))
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 + 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu()