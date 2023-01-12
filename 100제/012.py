class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')


x = Wizard(545, 210, 10)
print(x.health, x.mana, x.armor)
x.attack()


# 답지는 실행안됨, 아마 파이썬 버전 차이인듯
# class Wizard:
#     def stats(self, health, mana, armor):
#         self.health = health
#         self.mana = mana
#         self.armor = armor

#     def attack(self):
#         print('파이어볼')


# x = Wizard(health=545, mana=210, armor=10)
# print(x.health, x.mana, x.armor)
# x.attack()
