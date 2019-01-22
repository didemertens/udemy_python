import os
import random

def display_board(board):
  os.system('clear')
  print(board[1] + '|' + board[2] + '|' + board[3])
  print('-|-|-')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('-|-|-')
  print(board[7] + '|' + board[8] + '|' + board[9])


#display_board(test_board)

def player_input():
  marker = ''
  while marker != 'X' and marker != 'O':
    marker = input('Player 1, do you want to be X or O? ')
  player1_marker = marker
  if player1_marker == 'X':
    player2_marker = 'O'
  elif player1_marker == 'O':
    player2_marker = 'X'
  return (player1_marker, player2_marker)

#print(player_input())

def place_marker(board, marker, position):
  board[position] = marker

#print(place_marker(test_board,'$',8))
#display_board(test_board)

def win_check(board, mark):
  return  ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

#win_check(test_board,'X')

def choose_first():
  if random.randint(1, 2) == 1:
      return 'Player 1'
  else:
      return 'Player 2'

#print(choose_first())

def space_check(board, position):
  return board[position] == ' '

def full_board_check(board):
  for x in range(1,10):
    if space_check(board, x):
      return False
  return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
      position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
  playing = input('Do you want to play again? Yes/No: ')
  return playing.lower() == 'yes'

print("Welcome to Tic Tac Toe! Let's begin.")

while True:
  the_board = [' '] * 10
  player1_marker, player2_marker = player_input()
  player_turn = choose_first()
  print(player_turn + ' goes first.')


  play_game = input('Are you ready to play? Yes/No: ')
  if play_game.lower() == 'yes':
    playing = True
  else:
    playing = False

  while playing == True:
    if player_turn == 'Player 1':
      display_board(the_board)
      position = player_choice(the_board)
      place_marker(the_board, player1_marker, position)

      if win_check(the_board, player1_marker):
        display_board(the_board)
        print("Player 1 won!")
        playing = False

      else:
        if full_board_check(the_board):
          display_board(the_board)
          print('The game is a draw!')
          break
        else:
          player_turn = 'Player 2'

    else:
      display_board(the_board)
      position = player_choice(the_board)
      place_marker(the_board, player2_marker, position)

      if win_check(the_board, player2_marker):
        display_board(the_board)
        print("Player 2 won!")
        playing = False
      else:
        if full_board_check(the_board):
          display_board(the_board)
          print('The game is a draw!')
          break
        else:
          player_turn = 'Player 1'

  if not replay():
    break






