from core.player import Player
from core.ai import AIPlayer

def play_game():
    human = Player("You")
    ai = AIPlayer()

    human.place_ships()
    ai.place_ships()

    turn = 0
    while True:
        print("\nYour board:")
        human.board.display(reveal=True)
        print("\nEnemy board:")
        ai.board.display()

        if turn % 2 == 0:
            x, y = map(int, input("Enter attack coordinates (x y): ").split())
            if ai.board.attack(x, y):
                print("Hit!")
            else:
                print("Miss!")
        else:
            x, y = ai.choose_move()
            print(f"AI attacks ({x}, {y})")
            if human.board.attack(x, y):
                print("AI hit your ship!")
            else:
                print("AI missed.")
            ai.remove_move(x, y)

        if human.board.all_ships_sunk():
            print("You lost. AI wins!")
            break
        elif ai.board.all_ships_sunk():
            print("You win!")
            break

        turn += 1

if __name__ == "__main__":
    play_game()
