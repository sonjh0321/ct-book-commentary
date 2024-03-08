import random

class Game:
    def __init__(self):
        self.human_count = 0
        self.bot_count = 0

    def start(self):
        print("컴퓨터와의 가위-바위-보 게임을 시작하겠습니다.")
        print("======================================")
        while True:
            human = input("가위, 바위, 보 중에 하나를 입력하세요! ")
            bot = random.choice(["가위", "바위", "보"])
            print(f"봇이 [ {bot} ]을 냈습니다.")

            winner = self.rock_paper_scissors(human, bot)
            if winner == "human":
                print("당신이 이겼습니다.")
            elif winner == "bot":
                print("봇이 이겼습니다.")
            else:
                print("비겼습니다.")


            if self.human_count >= 3:
                print("축하드립니다!! 봇을 이기셨습니다!!")
                break
            if self.bot_count >= 3:
                print("봇이 먼저 세 판을 이겼군요.")
                break

    def rock_paper_scissors(self, player1_choice, player2_choice):
        rules = {
            '가위': '보',
            '바위': '가위',
            '보': '바위'
        }

        if rules.get(player1_choice) is None:
            return "오류"
        elif rules.get(player2_choice) is None:
            return "오류"

        if player1_choice == player2_choice:
            return '무승부'
        elif rules.get(player1_choice) == player2_choice:
            self.human_count += 1
            return 'human'
        else:
            self.bot_count += 1
            return 'bot'

game = Game()
game.start()
