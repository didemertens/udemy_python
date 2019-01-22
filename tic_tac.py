import os
import random

def display_board(board):
  os.system('clear')
  print('-------')
  print('|' +board[1] + '|' + board[2] + '|' + board[3] + '|')
  print('|' +'-' + '|' + '-' + '|' + '-' + '|')
  print('|' +board[4] + '|' + board[5] + '|' + board[6] + '|')
  print('|' +'-' + '|' + '-' + '|' + '-' + '|')
  print('|' +board[7] + '|' + board[8] + '|' + board[9] + '|')
  print('-------')

test_board = ['#','X',' ','X','O','X','O','X','O','X']
#display_board(test_board)

def player_input():
  marker = ''
  while marker != 'X' and marker != 'O':
    marker = input('Player 1, do you want to be X or O? ')
  if marker == 'X':
    return ('X', 'O')
  else:
    return ('O', 'X')

#print(player_input())

def place_marker(board, marker, position):
  board[position] = marker

#place_marker(test_board,'$',8)
#display_board(test_board)

def win_check(board, mark):
  return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

#print(win_check(test_board,'X'))

def choose_first():
  return 'Player ' + str(random.randint(1,2))

def space_check(board, position):
  return board[position] == ' '

def full_board_check(board):
  for position in range(1,10):
    if space_check(board, position):
      return False
  return True

#print(full_board_check(test_board))

def player_choice(board):
  position = int(input('Choose a number for your next move: '))
  if space_check(board, position):
    return position

#print(player_choice(test_board))

def replay():
  replay_tic = input('Do you want to play again? Yes/No ')
  return replay_tic[0].lower() == 'y'

#print(replay())

print('Welcome to Tic Tac Toe!')

while True:
  board_game = [' '] * 10
  player1_marker, player2_marker = player_input()
  player_turn = choose_first()
  print(player_turn + ' goes first.')

  play_game = input('Are you ready to play? Yes/No ')
  if play_game[0].lower() == 'y':
    playing = True
  else:
    playing = False

  while playing:
    if '1' in player_turn:
      display_board(board_game)
      position = player_choice(board_game)
      place_marker(board_game, player1_marker, position)

      if win_check(board_game, player1_marker):
        display_board(board_game)
        print('Player 1 won!')
        playing = False

      else:
        if full_board_check(board_game):
          display_board(board_game)
          print("It's a draw.")
          break
        else:
          player_turn = 'Player 2'

    else:
      display_board(board_game)
      position = player_choice(board_game)
      place_marker(board_game, player2_marker, position)

      if win_check(board_game, player2_marker):
        display_board(board_game)
        print('Player 2 won!')
        playing = False

      else:
        if full_board_check(board_game):
          display_board(board_game)
          print("It's a draw.")
          break
        else:
          player_turn = 'Player 1'

  if not replay():
    break

