start = ["A","B","C","D"]
end = ["P","Q","R"]

for i in range(4):

    x = 0
    for j in range(i+1):
        print(start[x], end=" ")
        x+=1

    y = 0
    for j in range(3-i):
        print(end[y], end=" ")
        y+=1

    print()
