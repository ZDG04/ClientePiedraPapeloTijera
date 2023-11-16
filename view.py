import pygame

# Inicializa Pygame

# Define el ancho y la altura de la ventana del juego
WIDTH =  400
HEIGHT = 400

# Crea la ventana del juego
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Establece el título de la ventana del juego
pygame.display.set_caption("Client")


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 100
        self.height = 50

    def draw(self, win):
        # Dibuja el botón en la ventana del juego
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        
        # Dibuja el texto en el botón
        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x+round(self.width/2)-round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))
    
    def click(self, pos):
        # Comprueba si el botón ha sido clicado
        x1 = pos[0] 
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <=self.y + self.height:
            return True
        else:
            return False
        
def scoreUpdate(game, p, scores):
    # Actualiza las puntuaciones
    if game.findWinner() == -1: 
        scores[2] += 1
    else:
        if game.findWinner() == p: 
            scores[0] += 1
        else:
            scores[1] += 1

def redrawWindow(win, game, p, scores):  
    # Redibuja la ventana del juego
    win.fill((255, 255, 255))

    if not(game.isConnected()): 
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render("Waiting for opponent...", 1, (0, 0, 0))
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render("Your Move", 1, (0, 255, 255))
        win.blit(text, (30, 50))

        text = font.render("Opponent's", 1, (0, 255, 255))
        win.blit(text, (200, 50))

        move1 = game.getPlayerMove(0)
        move2 = game.getPlayerMove(1)

        if game.bothGone():
            text1 = font.render(move1, 1, (0, 0, 0))
            text2 = font.render(move2, 1, (0, 0, 0))

        else:
            if game.p1Gone and p == 0:
                text1 = font.render(move1, 1, (0, 0, 0))
            elif game.p1Gone:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))


            if game.p2Gone and p == 1:
                text2 = font.render(move2, 1, (0, 0, 0))
            elif game.p2Gone:
                text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))
        if p == 1: 
            win.blit(text2, (30, 120))
            win.blit(text1, (200, 120))
        else:
            win.blit(text1, (30, 120))
            win.blit(text2, (200, 120))

        f = pygame.font.SysFont("comicsans", 30)
        w1 = f.render("Wins: " + str(scores[0]), 1, (0, 255, 0))
        l1 = f.render("Loses: " + str(scores[1]), 1, (255, 0, 0))
        t1 = f.render("Ties: " + str(scores[2]), 1, (0, 0, 0))

        w2 = f.render("Wins: " + str(scores[0]), 1, (0, 255, 0))
        l2 = f.render("Loses: " + str(scores[1]), 1, (255, 0, 0))
        t2 = f.render("Ties: " + str(scores[2]), 1, (0, 0, 0))

        if p == 0:
            win.blit(w1, (20, 350))
            win.blit(t1, (150, 350))
            win.blit(l1, (270, 350))
        else:
            win.blit(w2, (20, 350))
            win.blit(t2, (150, 350))
            win.blit(l2, (270, 350))
        for btn in btns:
            btn.draw(win)
    pygame.display.update()

# Crea los botones del juego
btns = [Button("Rock", 25, 300, (0, 0, 0)), Button("Paper", 150, 300, (255, 0, 0)), Button("Scissors", 275, 300, (0, 255, 0))]
