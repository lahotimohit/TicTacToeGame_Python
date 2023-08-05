b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
chance = 1
Game = 'running'


def design():
    print(" %c | %c | %c " % (b[0], b[1], b[2]))
    print("___|___|___")
    print(" %c | %c | %c " % (b[3], b[4], b[5]))
    print("___|___|___")
    print(" %c | %c | %c " % (b[6], b[7], b[8]))
    print("   |   |   ")


def score():
    global Game
    if b[0] == b[1] and b[1] == b[2] and b[0] != ' ':
        Game = 'win'
    elif b[0] == b[3] and b[3] == b[6] and b[0] != ' ':
        Game = 'win'
    elif b[0] == b[4] and b[4] == b[8] and b[0] != ' ':
        Game = 'win'
    elif b[1] == b[4] and b[4] == b[7] and b[1] != ' ':
        Game = 'win'
    elif b[3] == b[4] and b[4] == b[5] and b[3] != ' ':
        Game = 'win'
    elif b[6] == b[7] and b[7] == b[8] and b[6] != ' ':
        Game = 'win'
    elif b[2] == b[4] and b[4] == b[6] and b[2] != ' ':
        Game = 'win'
    elif b[2] == b[5] and b[5] == b[8] and b[2] != ' ':
        Game = 'win'
    elif b[0] != ' ' and b[1] != ' ' and b[2] != ' ' \
            and b[3] != ' ' and b[4] != ' ' and b[5] != ' ' \
            and b[6] != ' ' and b[7] != ' ' and b[8] != ' ':
        Game = 'draw'
    else:
        Game = 'running'


def check_space(pos):
    if b[pos] == ' ':
        return True
    else:
        return False


def game(pl_a, pl_b):
    while Game == 'running':
        global chance
        if chance % 2 != 0:
            print(f"{pl_a}'s Chance...")
            x = int(input("Please enter the position between 0 to 9 where you want to placed 'X: "))
            if x <= 0:
                print("Please enter correct value....")
            elif check_space(x-1):
                b[x-1] = 'X'
                chance += 1
                score()
                design()
            else:
                print("Value is already stored in given position...")
        else:
            print(f"{pl_b}'s Chance...")
            x = int(input("Please enter the position between 0 to 9 where you want to placed 'O': "))
            if x <= 0:
                print("Please enter correct value....")
            elif check_space(x-1):
                b[x-1] = 'O'
                chance += 1
                score()
                design()


def result(pl_1, pl_2):
    if Game == 'draw':
        print(f"Game is draws between {pl_1} & {pl_2}")
    elif chance % 2 == 0 and Game == 'win':
        print(f"Congratulations {pl_1}, you wins the game...")
    else:
        print(f"Congratulations {pl_2}, you wins the game...")


print("Welcome to the Tic Tac Toe Game.....")
player_a = input("Enter name of Player1: ")
player_b = input("Enter name of Player2: ")
print(f'So, {player_a} is "X" and {player_b} is "O"')
design()
game(player_a, player_b)
result(player_a, player_b)
