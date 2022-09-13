class user:
    hp = 100
    name = "none"

    def __init__(self, name):
        self.name = name

    def changeHp(self,hp):
        self.hp += hp
        print(f"{self.name}님의 HP가 {hp}만큼 변동되었습니다..")
        print(f"현재 {self.name}님의 HP는 {self.hp}입니다.")
#유저의 이름과 hp 설정