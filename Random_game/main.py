import random


moves = 16


while True:
    position = int(input("Insert your move: "))  
    bot_move = random.randint(1, moves)

    print(f"The bot move: {bot_move}")
    
    if position == bot_move:
        print("The bot has win")
        break
    else:
        moves -= 1
