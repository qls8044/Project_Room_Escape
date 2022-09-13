
class question:
    qTitle = ""
    sel = ""
    ans = ""
    hint = ""
    hp = 0

    def __init__(self, qTitle, sel, ans, hint, hp):
        self.qTitle = qTitle
        self.sel = sel
        self.ans = ans
        self.hint = hint
        self.hp = hp
#질문저장요소 생성