from question import *
from random import *

q01 = question("돌이 길면?","[1: 돌김 2: 돌길 3: 롱스톤 4: 빼빼롱]", "3","D", 5)
q02 = question("설탕이 깜짝 놀라면?","[1: 이럴슈가 2: 방탄슈가 3: 슈가슈가룬 4: 깜놀설탕]","1","D", 5)
q03 = question("매가 독수리를 패면?","[1:매독 2: 매가패쓰 3: 패매 4: 매이글]", "2","D", 5)
q04 = question("흡혈귀가 식탁에서 웃음이 끊이질 않는 이유는?", "[1: 흡킥흡킥해서 2: 웃음이 많아서 3: 피식해서 4: 개그맨이라서]", "3","D", 5)
q05 = question("수박 1통엔 5천원, 그럼 두통엔?", "[1: 1만원 2: 수두 3: 5천원 4: 게보린]", "4", "D", 5)

qList = [q01, q02, q03, q04, q05]


q01 = question("몽골의 수도는?","[1: 흡스골 2: 하라허름 3: 올랑 4: 울란바토르]", "4","A", 10)
q02 = question("네덜란드의 수도는?","[1: 헤이그 2: 암스테르담 3: 브레다 4: 로테르담]","2","A", 10)
q03 = question("스페인의 수도는?","[1:세비야 2: 발렌시아 3: 마드리드 4: 바르셀로나]", "3","A", 10)
q04 = question("태국의 수도는?", "[1: 방콕 2: 파타야 3: 푸켓 4: 코사무이]", "1","A", 10)
q05 = question("한국의 수도는?", "[1: 부산 2: 서울 3: 인천 4: 대구]", "2", "A", 10)

qList_level2 = [q01, q02, q03, q04, q05]

a = randint(1, 10)
b = randint(1, 10)
q01 = question(f"{a}x{b}의 값은?",f"[1: 25 2: 35 3: {a*b} 4: 7]","3","T",10)
q02 = question(f"{a}+{b}의 값은?",f"[1: 25 2: 35 3: {a+b} 4: 7]","3","T",10)
q03 = question(f"{a}-{b}의 값은?",f"[1: 25 2: 35 3: {a-b} 4: 7]","3","T",10)
q04 = question(f"{a}/{b}의 몫은?",f"[1: 25 2: 35 3: {a//b} 4: 7]","3","T",10)

qList_level3 = [q01, q02, q03, q04]


q01 = question("다음 중 빈칸에 들어갈 단어로 알맞은 것은? antidis__stablishmentarianism : 국교 폐지 조례 반대론","[1: i 2: a 3: e 4: o]","3","A", 20)
q02 = question("다음 중 빈칸에 들어갈 단어로 알맞은 것은? floccinaucinihili__ilification : 익살","[1: c 2: p 3: b  4: d]","2","A", 20)
q03 = question("다음 중 빈칸에 들어갈 단어로 알맞은 것은? supercalifragilisticexpiali__ocious : 환상적인","[1:p 2: t 3: d 4: z]", "3","A", 20)
q04 = question("다음 중 빈칸에 들어갈 단어로 알맞은 것은? otorhinolar__ngological: 이빈후과적인", "[1: o 2: y 3: l 4: a]","2","A", 20)
q05 = question("다음 중 빈칸에 들어갈 단어로 알맞은 것은? sesq__ipedalian : 긴 단어의", "[1: u 2: l 3: i 4: e]","1","A", 20)

qList_level4 = [q01, q02, q03, q04, q05]