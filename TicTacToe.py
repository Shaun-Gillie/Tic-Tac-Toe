def sum(a, b, c):      #defining a function to override inbuilt sum() function will be used later to check wins
    return a + b + c
#creating the board 
def print_board(y, z):
    A1 = 'X ' if y[0] else ('O ' if z[0] else 'A1')
    B1 = 'X ' if y[1] else ('O ' if z[1] else 'B1')
    C1 = 'X ' if y[2] else ('O ' if z[2] else 'C1')
    A2 = 'X ' if y[3] else ('O ' if z[3] else 'A2')
    B2 = 'X ' if y[4] else ('O ' if z[4] else 'B2')
    C2 = 'X ' if y[5] else ('O ' if z[5] else 'C2')
    A3 = 'X ' if y[6] else ('O ' if z[6] else 'A3')
    B3 = 'X ' if y[7] else ('O ' if z[7] else 'B3')
    C3 = 'X ' if y[8] else ('O ' if z[8] else 'C3')
    print(f"{A1} | {B1} | {C1} ")
    print(f"---|----|---")
    print(f"{A2} | {B2} | {C2} ")
    print(f"---|----|---")
    print(f"{A3} | {B3} | {C3} ") 

def sum_list(states):   #function to calculate the sum of values in a list will be used to check for full board
    summ = 0 
    for n in states:
        summ += n
    return summ


def check_for_win(y, z):

    # All winning patters
    winnings = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    

    for win in winnings:
        if(sum(y[win[0]], y[win[1]], y[win[2]]) == 3):
            print_board(y, z)
            print("X Won the match")
            return 1
        if(sum(z[win[0]], z[win[1]], z[win[2]]) == 3):
            print_board(y, z)
            print("O Won the match")
            return 0
#if I remove this, then it shows that there is a winner if the board is full and there is a winning pattern, but if the board is filled, it does not account for at t
        # if all places are filled and no one is the winner
if(sum_list(y) == 5):
    print_board(y, z)
    return -2
return -1


if __name__ == "__main__":
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    z = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    lookup = {"A1":0,
              "A2":3,
              "A3":6,
              "B1":1,
              "B2":4,
              "B3":7,
              "C1":2,
              "C2":5,
              "C3":8
    }

    turn = 1 

    print("Welcome to Tic Tac Toe")
    while(True):
        print_board(y, z)
        if(turn == 1):
            print("X to Play:")
            try:
                position = input("Choose a position: ")
                if (y[lookup[position]] or z[lookup[position]]):
                    print("The position is already taken. Please enter a correct position: ")
                    continue
                else:
                    y[lookup[position]] = 1
                    #print("Inside X -")
                    #print(turn)
                    turn = 1 - turn

            except (ValueError, KeyError) as e:
                print("The position is invalid. Please enter a correct position: ")
                continue

        else:
            print("O to Play:")
            try:
                position = input("Choose a position: ")
                if (y[lookup[position]] or z[lookup[position]]):
                    print("The position is already taken. Please enter a correct position: ")
                    continue
                else:
                    z[lookup[position]] = 1
                    #print("Inside O -")
                    #print(turn)
                    turn = 1 - turn

            except (ValueError, KeyError) as e:
                print("The position is invalid. Please enter a correct position: ")
                continue

        win_flag = check_for_win(y, z)
        if(win_flag == 1 or win_flag == 0):
            print("Match over")
            break

        if(win_flag == -2):
            print("It's a tie! Match over")
            break


               