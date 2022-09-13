from user import *
class stage:
    Stage_LEVEL = 1
    chk = False
    def start(self):
        print("게임이 시작되었습니다.")
        print(" 진행 하시겠습니까? ")
        print("YES or NO")
        StartState = True
        while StartState:
            answer = input()
            if answer == "YES":
                print("게임을 시작하겠습니다.")
                StartState = False
                stage.chk = True
            elif answer == "NO":
                print("종료합니다.")
                break
            else:
                print("잘못된 명령입니다.")
#게임이 시작될때 텍스트 출력

    def StageUp(self):
        stage.Stage_LEVEL +=1