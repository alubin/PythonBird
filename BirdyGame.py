__author__ = 'AL'
import pygame

black = (0,0,0)
white = (255,255,255)

pygame.init()
surface = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()

img = pygame.image.load('Assets/Helicopter_sprite.png');
x = 150
y = 200

def helicopter(x, y, image):
    surface.blit(img, (x, y))

def gameOver():
    pygame.quit()
    quit()

y_move = 1

#Begin Game Loop
game_over = False

while not game_over:
    #Checks for event changes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        #Move Helicopter up
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_move = -5

        #Defaults the helicopter into a falling position.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_move = 5
    #Moves the helicopter down unless action is taken.
    y += y_move

    #Fills the surface with a black screen continuously to erase previous frame.
    surface.fill(black)
    #Calls function that places helicopter on the screen.
    helicopter(x,y,img)

    if y > 360 or y < 0:
        gameOver()

    pygame.display.update()
    #Refresh rate for the game updates.
    clock.tick(60)

#End Game Loop
pygame.quit()
quit()