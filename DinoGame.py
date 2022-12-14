#공룡 게임
import pygame
import sys
# step1 : set screen, fps
# step2 : show dino, jump dino
# step3 : show tree, move tree 

MAX_WIDTH=800 #스크린 가로크기
MAX_HEIGHT=400 #세로 크기
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)
white=(255,255,255)

def startGame():
    global screen,clock,imgDino1,imgDino2,imgTree,fps
    pygame.init() #파이게임 모듈 초기화
    pygame.display.set_caption('Dino Game')#게임 프로그램 이름 설정
    # set screen, fps    
    screen=pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))
    #게임이 실행될 창 생성(가로*세로)
    fps=pygame.time.Clock()
    #프레임 조정하기 위한 변수 생성
    #화면을 초당 몇 번 출력하는가
    # dino    
    imgDino1=pygame.image.load('dino1.png')
    imgDino2=pygame.image.load('dino2.png')
    #공룡 사진 불러오기
    imgTree=pygame.image.load('tree.png')
    #나무사진 불러오기
    
def restartGame():
    pygame.display.update()
    runGame()
    
def drawOver():
    global screen
    font=pygame.font.SysFont("arial",30,True,True)
    #screen.fill((0,0,0))
    text_over=font.render("GAME OVER",True,red)
    #render(Text,antialias,color,background=None)
    screen.blit(text_over,(300,100))
    #게임 오버 텍스트 출력
    text_restart=font.render("PRESS 'R' TO RESTART",True,green)
    text_exit=font.render("PRESS 'E' TO GAME EXIT",True,black)
    screen.blit(text_restart,(300,130))
    screen.blit(text_exit,(300,160))
    
    pygame.display.update()
    
def runGame():
    
    
    dino_height=imgDino1.get_size()[1]#공룡 세로 길이
    dino_bottom=MAX_HEIGHT-dino_height#공룡 이미지 y축 중심 설정
    
    dino_x=50
    dino_y=dino_bottom
    jump_top=120
    leg_swap=True
    is_bottom=True
    is_go_up=False
   
    tree_height=imgTree.get_size()[1]
    tree_x=MAX_WIDTH
    tree_y=MAX_HEIGHT-tree_height
    
    
    score=0
    
    Running=True
    
    while Running:
        font=pygame.font.SysFont("arial",30,True,True)
        #(font name, size, bold, italic)

        screen.fill((255,255,255))
        
        text_score=font.render("SCORE :"+f'{score}',True,black)
        screen.blit(text_score,(20,10))
        #점수 텍스트 출력

                        
        # dino move        
        if is_go_up:
            dino_y -= 10.0
        elif not is_go_up and not is_bottom:
            dino_y += 10.0
        # dino top and bottom check        
        if is_go_up and dino_y <= jump_top:
            is_go_up = False
        
        if not is_bottom and dino_y >= dino_bottom:
            is_bottom=True
            dino_y=dino_bottom
        # tree move        
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x=MAX_WIDTH
        # draw tree        
        screen.blit(imgTree,(tree_x,tree_y))    
        # draw dino        
        if leg_swap:
            screen.blit(imgDino1,(dino_x,dino_y))
            leg_swap=False
        else:
            screen.blit(imgDino2,(dino_x,dino_y))
            leg_swap=True
            
        #나무 사각형 
        rect_tree=imgTree.get_rect()
        rect_tree.left=tree_x
        rect_tree.top=tree_y
        
        #공룡 사각형
        rect_dino=imgDino1.get_rect()
        rect_dino.x=dino_x
        rect_dino.y=dino_y
        
        #공룡과 나무 충돌시 게임 종료
        if  rect_tree.colliderect(rect_dino):
            
            drawOver()
            pressKey=True
            while pressKey:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_r:
                            restartGame()
                        if event.key==pygame.K_e:
                            pygame.quit()
                            sys.exit()
               
        else:
            score+=10
            #점수 증가
        
        #이벤트 점프랑, 게임종료
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if is_bottom:
                        is_go_up=True
                        is_bottom=False
                    #스페이스바 눌러서 공룡 점프
            else:
                pass
        
            
            
        # update        
        pygame.display.update()
        fps.tick(30)
        



startGame()
runGame()
