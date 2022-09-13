from stage import *
from qlist import *
from chckHp import *
from random import *
from veiwPass import *

for i in range(4):
    myPass.append("*")


stage.start(self='')
#시작문구 생성
stageLevel = stage.Stage_LEVEL
password = "DATA"
cnt =0
#스테이지 변수설정

if stage.chk :
    print("이름을 입력해주세요:", end='')
    print()
    n = input()
    user01 = user(n)
    print(f"당신의 이름은 {user01.name} 입니다.")
#이름입력

gameover = False
while stage.chk:
    if gameover == True:
        print("사망하였습니다.")
        break
#게임이 끝났는지 체크
    if stageLevel == 1:
        print(f"LEVEL0{stageLevel}")
        r = randint(0, (len(qList)) - 1)
        print(qList[r].qTitle)
        print(qList[r].sel)
        aa = input()
#question 파일에서 리스트를 가져와 aa입력
        if aa == qList[r].ans:
            print(f"첫번째 암호의 힌트는 {qList[r].hint}입니다.")
            viewPass(qList[r].hint,stageLevel)
            stageLevel +=1
        else:
            user01.changeHp(qList[r].hp * -1)
            gameover = checkHp(user01.hp)
#입력한 답과 비교
    elif stageLevel == 2:
        print(f"LEVEL0{stageLevel}")
        r = randint(0, (len(qList_level2)) - 1)
        print(qList_level2[r].qTitle)
        print(qList_level2[r].sel)
        aa = input()
        if aa == qList_level2[r].ans:
            print(f"두번째 암호의 힌트는 {qList_level2[r].hint}입니다.")
            viewPass(qList_level2[r].hint,stageLevel)
            stageLevel +=1
        else:
            user01.changeHp(qList_level2[r].hp * -1)
            gameover = checkHp(user01.hp)
#레벨2
    elif stageLevel == 3:
        print(f"LEVEL0{stageLevel}")
        r = randint(0, (len(qList_level3)) - 1)
        print(qList_level3[r].qTitle)
        print(qList_level3[r].sel)
        aa = input()
        if aa == qList_level3[r].ans:
            print(f"세번째 암호의 힌트는 {qList_level3[r].hint}입니다.")
            viewPass(qList_level3[r].hint,stageLevel)
            stageLevel +=1
        else:
            user01.changeHp(qList_level3[r].hp * -1)
            gameover = checkHp(user01.hp)
#레벨3
    elif stageLevel == 4:
        print(f"LEVEL0{stageLevel}")
        r = randint(0, (len(qList_level4)) - 1)
        print(qList_level4[r].qTitle)
        print(qList_level4[r].sel)
        aa = input()
        if aa == qList_level4[r].ans:
            print(f"네번째 암호의 힌트는 {qList_level4[r].hint}입니다.")
            viewPass(qList_level4[r].hint,stageLevel)
            stageLevel +=1
        else:
            user01.changeHp(qList_level4[r].hp * -1)
            gameover = checkHp(user01.hp)
#레벨4
    elif stageLevel == 5:
        if cnt==0:
            print("게임을 모두 클리어 하셨습니다.\n비밀번호 입력을 해주세요")
            cnt+=1
        x= input()
        if x== password:
            print("비밀번호가 맞았습니다.\n 축하합니다 게임을 클리어 하셨습니다!!!")
        elif x != password:
            print("비밀번호가 맞지않습니다.")
            user01.changeHp(-25)
            if user01.hp <=0:
                print("사망")
                break
        else:
            break
#비밀번호 입력후 정답인지 아닌지 확인


