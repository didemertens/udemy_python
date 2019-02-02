def ask_for_int():
  while True:
    try:
      result = int(input('Enter a number: '))
    except:
      print('That is not  a number!')
      continue
    else:
      print('Thanks!')
      break
    finally:
      print('End of try/except/finally')

ask_for_int()
