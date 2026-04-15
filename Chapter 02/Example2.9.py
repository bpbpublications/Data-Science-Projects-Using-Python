n = 3
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")#Print spaces
    for y in range(2*i-1):
        print("*", end="")# Print stars
    print()# Move to the next line
