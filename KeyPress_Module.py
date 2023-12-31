import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = False
    for event in pygame.event.get() :
        pass

    KeyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))

    print('K_{}'.format(keyName))

    if KeyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("f"):
        print("f key pressed ")
    if getKey("RIGHT"):
        print("Right key pressed")

if __name__ == "__main__":
    init()
    while True:
        main()