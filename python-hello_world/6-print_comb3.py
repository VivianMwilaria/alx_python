for i in range (10):
    for j in range (1 + 1, 10 ):
              print("{:02}".format(i * 10 + j), end="," if (i != 8 or j != 9) else "\n")
