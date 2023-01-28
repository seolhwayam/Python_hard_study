class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 생성 :', end=' ')

    def info(self):
        print(f'{self.owner}의 포켓몬이 사용 가능한 스킬')
        n = 1
        for skill in self.skills:
            print(str(n) + " : " + skill)
            n =n+1
        print("공격 번호 선택 : ")

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전!')




class Pikachu(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f'{self.name}')

    def attack(self, idx):
        print(f'[삐까삐까] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')


class Ggoboogi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f'{self.name}')

    def attack(self, idx):
        print(f'[꼬북꼬북] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')

class Pairi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "파이리"
        print(f'{self.name}')

    def attack(self, idx):
        print(f'[파읠파읠] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')




while True:
    print("1) 포켓몬 생성  2) 프로그램 종료 : ")
    choice = int(input())
    if choice == 1:
         print("1) 피카츄  2)꼬부기 3)파이리")
         pick = int(input())
         print("플레이어 이름 입력 :")
         name = input()
         print("사용 가능한 기술 입력(/로 구분하여 입력)")
         skilll = input()
         if pick == 1:
            pika1 = Pikachu(name,skilll)
            pika1.info()
            attackpick = int(input())-1
            pika1.attack(attackpick)
         elif pick == 2:
            Ggoboo1 = Ggoboogi(name,skilll)
            Ggoboo1.info()
            attackpick = int(input())-1
            Ggoboo1.attack(attackpick)
         elif pick == 3:
            Pairi1 = Pairi(name,skilll)
            Pairi1.info()
            attackpick = int(input())-1
            Pairi1.attack(attackpick)
    elif choice == 2:
        print("프로그램을 종료합니다")
        break
    else :
        print("잘못 입력되었습니다. 다시 선택해주세요.")



