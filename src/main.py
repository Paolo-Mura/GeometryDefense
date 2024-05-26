import pygame

pygame.init()

screen = pygame.display.set_mode([800, 800])

pygame.display.set_caption('GeometryDefense')

running = True

while running:
    
    # Catch exit event and quit application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (0, 0, 255), (400, 400), 30)
    
    pygame.display.flip()
    
pygame.quit()