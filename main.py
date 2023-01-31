import sys, pygame

pygame.init()

#Game running bool
gameRunning = True

#Screen size
size = width, height = 500,500

screen = pygame.display.set_mode(size)

black = 0,0,0

#store the snek
snakeRec = pygame.Rect(0, 0, 10, 10)



while gameRunning == True:
    pygame.event.get()

    if pygame.key.get_pressed()[pygame.K_w]:
        #print("UP")
        snakeRec = snakeRec.move(0,-1)

    if pygame.key.get_pressed()[pygame.K_a] == True:
        #print("LEFT")
        snakeRec = snakeRec.move(-1,0)
    if pygame.key.get_pressed()[pygame.K_s] == True:
        #print("DOWN")
        snakeRec = snakeRec.move(0,1)
    if pygame.key.get_pressed()[pygame.K_d] == True:
        #print("RIGHT")
        snakeRec = snakeRec.move(1,0)

    if snakeRec.x < 0:
        snakeRec.x = 0
    if snakeRec.x + snakeRec.height > screen.get_height():
        snakeRec.x = screen.get_height() - snakeRec.height
    if snakeRec.y < 0:
        snakeRec.y = 0
    if snakeRec.y + snakeRec.width > screen.get_width():
        snakeRec.y = screen.get_width() - snakeRec.width

    print("X: " + (str)(snakeRec.x))
    print("Y: " + (str)(snakeRec.y))
    # Draw the snek
    screen.fill(black)
    pygame.draw.rect(screen, (255, 255, 255), snakeRec)
    pygame.display.flip()