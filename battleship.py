from random import randint
board = []
ships = []
sunked = 0
first_user_ships = 0
second_user_ships = 0
for x in range(10):
    board.append(["O"] * 10)
def print_board(board):
    for row in board:
        print (" ".join(row))
def make_ship():
    ship_back = []
    ship_all = []
    ship_front_row = randint(1, 8)
    ship_front_col = randint(1, 8)
    ship_front = [ship_front_row, ship_front_col]
    veletl = randint(0, 1)
    ship_back_row = ship_front_row + veletl
    if veletl == 0:
        ship_back_col = ship_front_col + 1
    else:
        ship_back_col = ship_front_col
    ship_back = [ship_back_row, ship_back_col]
    ship_all = [ship_front, ship_back]
    return ship_all
def number_of_ships(): 
    num_of_ships = int(input("How many ships you want? maximum 3   "))
    if num_of_ships > 3:
        num_of_ships = int(input("It is too much! maximum 3   "))
    return num_of_ships
def ship_exam(ship_one_, ship_two_):
    egyezes = False
    for k in range(2):
        for j in range(2):
            if ship_one_[k][j] == ship_two_[k][j]:
                egyezes = True
    return egyezes
def matches():
    for test in range(0, hajoszam):
        if (ships[test][0][0] == guess_row and ships[test][0][1] == guess_col \
        or ships[test][1][0] == guess_row and ships[test][1][1] == guess_col) \
        and board[guess_row][guess_col] != "+":
            for sunk in range(0, 2):
                sunked_row = ships[test][sunk][0]
                sunked_col = ships[test][sunk][1]
                board[sunked_row][sunked_col] = "+"
            return True
def results():
    if first_user_ships > second_user_ships:
        print ("First user won!")
    elif first_user_ships < second_user_ships:
        print ("Second user won!")
    else:
        print ("Result is egal.")
  
print ("Let's play Battleship!")
print ("One ship consists of two parts.")
hajoszam = number_of_ships()
for y in range(0, hajoszam):
    if y == 0:
        ship_to_add = make_ship()
        ships.append(ship_to_add)
    elif y == 1:
        ship_to_add = make_ship()
        ships.append(ship_to_add)
        while ship_exam(ships[0], ships[1]): #ennél az összehasonlításnál kell folytatni, mert ez még nem jó
            ships[1] = make_ship()
    elif y == 2:
        ship_to_add = make_ship()
        ships.append(ship_to_add)
        while ship_exam(ships[0], ships[2]) or ship_exam(ships[1], ships[2]):
            ships[2] = make_ship()
print ("Let's play Battleship!")
print ("One ship consists of two parts.")
print_board(board)
print(" ")
print (ships[0]) #for debugging
if hajoszam > 1:
    print (ships[1])
if hajoszam > 2:
    print (ships[2])
for turn in range(8):
    print ("Turn")
    print (turn + 1)
    if turn % 2 == 0:
        print("Guess, first user!")
    else:
        print("Guess, second user!")
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    print (" ")
    if matches():
        print ("Congratulations! You sunk one of my battleship!")
        sunked +=  1
        if turn % 2 == 0:
            first_user_ships += 1
        else:
            second_user_ships += 1
    else:
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        elif(board[guess_row][guess_col] == "+"):
            print ("This ship is sunked already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    print_board(board)
    if sunked == hajoszam:
        print ("You sunked all ships")
        results()
        break
    else:
        results()


