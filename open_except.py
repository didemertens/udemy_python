try:
  f = open('testfile', 'r')
  f.write("Write a test line")
# except: > all errors
except TypeError:
  print("There was a type error")
except OSError:
  print("You have an OS Error")
finally:
  print("I always run")
