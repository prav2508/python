j = 1
i = 1
while i <= 4:
    j = 1
    while j <= i:
        print("#", end=" ")
        j += 1
    print()
    i += 1
print("-------------------------")
for i in range(4,0,-1):
    for j in range(i):
        print("#", end=" ")
    print()