#!/usr/local/bin/python3.7
import sys,pygame,pyautogui
from pygame.locals import KEYUP,KEYDOWN,K_ESCAPE,K_SPACE,QUIT
import random,time
pygame.init()

#$B=i4|JQ?t$N@_Dj(B
x,y=pyautogui.size()
font = pygame.font.Font(None, 300)

def keybutton(sur,nums,key):#$B%\%?%sA`:n(B
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key==K_SPACE:
                key=False
        elif event.type==KEYUP:
            key=True
        return key
    
def drawing():
    sur=pygame.display.set_mode((x,y))
    sur.fill((0,0,0))
    return sur

def getnum():
    x=[]
    for i in range(1,73):
        x.append(i)
    return x

def change_number(sur,nums):#nums[1-72]
    random.seed()
    num=random.sample(nums,1)
    text=font.render(str(num),True,(255,255,255))
    sur.blit(text,[x/2-150,y/2-50])
    time.sleep(0.05)
    pygame.display.update()

def callchange_number(sur,nums,call):
    if(call==True):
        change_number(sur,nums)
    else:
        num=random.sample(nums,1)
        text=font.render(str(num),True,(255,255,255))
        sur.blit(text,[x/2-150,y/2-50])

def main():
    nums=getnum()
    key=None
    while True:
        sur=drawing()
        call=keybutton(sur,nums,key)
        callchange_number(sur,nums,call)
main()
