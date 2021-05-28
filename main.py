from Mymodule import gamefucs 

print('Welcome to Tic Tac Toe!')


while True:
    gamebrd = [' ']*10
    pl1, pl2 = gamefucs.player_input()
    turn = gamefucs.choose_first()
    print(turn + " moves first!")
    game = True
    while game:
        if turn == "player1":
            position = gamefucs.player_choice(gamebrd)
            gamefucs.place_marker(gamebrd, pl1, position)
            gamefucs.display_board(gamebrd)
            turn = "player2"
            if gamefucs.win_check(gamebrd, pl1):
                print("X wins the game!")
                gamefucs.replay(game)
                if game == False:
                    break
            else:
                if gamefucs.full_board_check(gamebrd):
                    print("It's a draw!")
                    gamefucs.replay(game)
                    if game == False:
                        break
        else:
            position = gamefucs.player_choice(gamebrd)
            gamefucs.place_marker(gamebrd, pl2, position)
            gamefucs.display_board(gamebrd)
            turn = "player1"
            if gamefucs.win_check(gamebrd, pl2):
                print("O wins the game!")
                gamefucs.replay(game)
                if game == False:
                    break
            else:
                if gamefucs.full_board_check(gamebrd):
                    print("It's a draw!")
                    gamefucs.replay(game)
                    if game == False:
                        break