#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

n = float(input("a number: "))
n1 = round(n)
if n1 == n:
    print("the number is an integer")
else:
    print("the number is not an integer")



