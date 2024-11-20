import pygame
import random

# 초기화
pygame.init()

# 화면 설정
가로 = 600
세로 = 700
화면 = pygame.display.set_mode((가로, 세로))
pygame.display.set_caption('테트리스')

# 색상
하얀색 = (255, 255, 255)
검은색 = (0, 0, 0)
빨간색 = (255, 0, 0)
초록색 = (0, 255, 0)
파란색 = (0, 0, 255)

# 게임 설정
블록크기 = 30
게임판_가로 = 10
게임판_세로 = 20
게임판_x = (가로 - 블록크기 * 게임판_가로) // 2
게임판_y = 세로 - (블록크기 * 게임판_세로) - 10

# 블록 모양
블록모양 = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], 
     [1, 1]],        # O
    [[1, 1, 1], 
     [0, 1, 0]],     # T
    [[1, 1, 1], 
     [1, 0, 0]],     # L
]

class 테트리스:
    def __init__(self):
        self.게임판 = [[0] * 게임판_가로 for _ in range(게임판_세로)]
        self.점수 = 0
        self.현재블록 = self.새블록()
        self.x = 게임판_가로 // 2 - 1
        self.y = 0
        
    def 새블록(self):
        return random.choice(블록모양)
    
    def 이동가능(self, x, y):
        for i in range(len(self.현재블록)):
            for j in range(len(self.현재블록[0])):
                if self.현재블록[i][j] == 0:
                    continue
                새x = x + j
                새y = y + i
                if 새x < 0 or 새x >= 게임판_가로 or 새y >= 게임판_세로:
                    return False
                if 새y >= 0 and self.게임판[새y][새x] != 0:
                    return False
        return True
    
    def 블록고정(self):
        for i in range(len(self.현재블록)):
            for j in range(len(self.현재블록[0])):
                if self.현재블록[i][j] == 0:
                    continue
                if self.y + i < 0:
                    return True
                self.게임판[self.y + i][self.x + j] = 1
        self.줄체크()
        self.현재블록 = self.새블록()
        self.x = 게임판_가로 // 2 - 1
        self.y = 0
        return False
    
    def 줄체크(self):
        줄수 = 0
        for i in range(게임판_세로):
            if all(self.게임판[i]):
                줄수 += 1
                del self.게임판[i]
                self.게임판.insert(0, [0] * 게임판_가로)
        self.점수 += 줄수 * 100

def 게임시작():
    게임 = 테트리스()
    시계 = pygame.time.Clock()
    낙하시간 = 0
    게임종료 = False

    while not 게임종료:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                게임종료 = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if 게임.이동가능(게임.x - 1, 게임.y):
                        게임.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if 게임.이동가능(게임.x + 1, 게임.y):
                        게임.x += 1
                elif event.key == pygame.K_DOWN:
                    if 게임.이동가능(게임.x, 게임.y + 1):
                        게임.y += 1

        # 블록 자동 낙하
        if pygame.time.get_ticks() - 낙하시간 > 500:
            if 게임.이동가능(게임.x, 게임.y + 1):
                게임.y += 1
            else:
                게임종료 = 게임.블록고정()
            낙하시간 = pygame.time.get_ticks()

        # 화면 그리기
        화면.fill(검은색)
        
        # 게임판 그리기
        pygame.draw.rect(화면, 하얀색, 
                        [게임판_x-1, 게임판_y-1, 
                         블록크기*게임판_가로+2, 블록크기*게임판_세로+2], 1)

        # 고정된 블록 그리기
        for i in range(게임판_세로):
            for j in range(게임판_가로):
                if 게임.게임판[i][j]:
                    pygame.draw.rect(화면, 파란색,
                                   [게임판_x + j*블록크기, 게임판_y + i*블록크기,
                                    블록크기-1, 블록크기-1])

        # 현재 블록 그리기
        for i in range(len(게임.현재블록)):
            for j in range(len(게임.현재블록[0])):
                if 게임.현재블록[i][j]:
                    pygame.draw.rect(화면, 빨간색,
                                   [게임판_x + (게임.x+j)*블록크기,
                                    게임판_y + (게임.y+i)*블록크기,
                                    블록크기-1, 블록크기-1])

        # 점수 표시
        폰트 = pygame.font.SysFont('맑은고딕', 30)
        점수표시 = 폰트.render(f'점수: {게임.점수}', True, 하얀색)
        화면.blit(점수표시, (10, 10))

        pygame.display.update()
        시계.tick(30)

    pygame.quit()

if __name__ == '__main__':
    게임시작()