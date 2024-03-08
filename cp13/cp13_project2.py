import random

class Game:
    def __init__(self):
        self.bot = random.randint(0, 9)

    def start(self):
        print("컴이 낸 숫자를 찾아라")
        print("======================================")
        while True:
            human = int(input("0부터 9 사이를 입력하세요. "))

            if self.bot == human:
                print("맞추었습니다.")
                break
            elif self.bot > human:
                print("더 높은 수를 입력하세요.")
            else:
                print("더 낮은 수를 입력하세요.")


game = Game()
game.start()
