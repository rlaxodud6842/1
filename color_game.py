from time import sleep
import random

GAME_ROUND = 4
COUNT_DOWN_TIME = 2

# 색 클래스
class Basic_Color:
    def __init__(self, code, name, similar_name=None):
        self.code = code
        self.name = name
        self.similar_name = similar_name

# 색 클래스 선언
color = [
    Basic_Color("\033[31m", "빨강색"),
    Basic_Color("\033[32m", "초록색"),
    Basic_Color("\033[33m", "노랑색"),
    Basic_Color("\033[34m", "파랑색"),
    Basic_Color("\033[30m", "검은색"),
    Basic_Color("\033[37m", "하양색", "흰색")
      ]

# 카운트 다운
def count_down(wait_time):

    for i in range(wait_time):
        print(wait_time - i)
        sleep(1)

# 유저 클래스
class User:
    def __init__(self, score, name):
        self.score = score
        self.name = name

#랭크 클래스
class Rank:
    def __init__(self):
        self.user_list = [] #유저 리스트

    def add_user(self,user):
        self.user_list.append(user) #유저 추가

    def list_sort(self): #랭크 리스트 정렬
        self.user_list.sort(key=lambda object: object.score, reverse=True)

    def show_all_rank(self): #전체 랭크 보여주기 메소드
        self.list_sort()
        list_length = len(self.user_list)

        for i in range(list_length):
            rank_name = self.user_list[i].name
            rank_score = self.user_list[i].score
            print(i+1, ".", rank_name, "점수:", rank_score)

    def show_user_ranking(self,user): #사용자 랭킹 보여주기
        self.list_sort()
        ranking = self.user_list.index(user) + 1
        if ranking <=10:
            print("축하합니다! 랭킹 10위 안에 들었습니다!")
        print("당신의 랭킹:", ranking, "위")

rank = Rank()

# 본 게임 함수
def game():
    print(GAME_ROUND, "라운드 까지 있습니다")
    input("아무키나 누르면 게임이 시작됩니다.")

    user_score = 0
    for i in range(GAME_ROUND):
        count_down(COUNT_DOWN_TIME)
        previous_color_code = None

        #문제 생성 및 출제
        random_color = random.choice(color)

        #중복 확인 부분
        while True:
            if random_color.code != previous_color_code:
                previous_color_code = random_color.code
                break
            else:
                random_color = random.choice(color)

        problem = random.choice(color).name
        print(random_color.code + problem + "\033[0m", i + 1, "번째 문제입니다")

        # 정답 확인 부분
        player_response = input("정답을 입력해주세요.:")
        if random_color.name == player_response or random_color.similar_name == player_response :
            print("정답입니다.")
            user_score += 1
        else:
            print("오답입니다.")

    # 점수 처리 부분
    print("점수:", user_score, "/", GAME_ROUND)
    user_name = input("이름을 입력하세요:")

    #유저 객체 생성 부분
    user = User(user_score, user_name)
    rank.add_user(user)
    rank.show_user_ranking(user)


# 메인 메뉴 함수
def main_menu():
    print("1.게임 시작")
    print("2.랭킹 보기")
    print("3.종료")

    while True: #예외 처리
        try:
            user_select = int(input("번호를 입력 해주세요:"))
            break
        except:
            print("숫자로 번호를 다시 입력 해주세요\n")

    if user_select == 1:
        game()

    elif user_select == 2:
        rank.show_all_rank()

    elif user_select == 3:
        print("게임을 종료합니다")
        exit()

while True:
    main_menu()


#(20221022) 완성