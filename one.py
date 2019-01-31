#one.py (name and main)

# build in variable called __name__ which gets assigned a string, if you run
# the script in terminal, can test if the py file is run directly, can organise
# beneath the if statement, what you actually want to execute

def func():
  print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
  print("ONE.PY is being run directly")
else:
  print("ONE.PY has been imported")
