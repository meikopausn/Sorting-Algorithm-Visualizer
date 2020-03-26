import pygame
import random as rnd
import time

def insertionsort(screen, numbers):
    for i in range(1, len(numbers)):
        x = numbers[i]
        tmpindex = i
        check = True
        while check:
            for block in range(0, len(numbers)):
                if block == tmpindex:
                    pygame.draw.rect(screen, (0, 255, 0), (block * 40 + 5, 0, 30, numbers[block]))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (block * 40 + 5, 0, 30, numbers[block]))
            pygame.display.flip()
            if tmpindex == 0 or x > numbers[tmpindex-1]:
                check = False
            else:
                tmp = numbers[tmpindex-1]
                numbers[tmpindex-1] = x
                numbers[tmpindex] = tmp
                tmpindex = tmpindex-1
            time.sleep(0.3)
            screen.fill((0,0,0))

def main():
    numbers = [rnd.randint(15, 580) for i in range(100)]
    print(numbers)
    pygame.init()
    pygame.display.set_caption("Sortingalgorithm")
    sc_b = 800 * 5
    sc_h = 600
    screen = pygame.display.set_mode([sc_b, sc_h])
    clock = pygame.time.Clock()
    FPS = 60

    unsorted = True
    running = True
    while running:
        pygame.event.get()
        screen.fill((0,0,0))

        if unsorted:
            for block in range(0, len(numbers)):
                pygame.draw.rect(screen, (255, 255, 255), (block * 40 + 5, 0, 30, numbers[block]))
            pygame.display.flip()
            time.sleep(3)
            insertionsort(screen, numbers)
            time.sleep(2)
            unsorted = False
        else:
            for block in range(0, len(numbers)):
                pygame.draw.rect(screen, (255, 0, 0), (block * 40 + 5, 0, 30, numbers[block]))
            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()