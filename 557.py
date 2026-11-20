numbers = input().split()
x = {}
for num in numbers:
    if num in x:
        print("Yes")
    else:
        print("No")
        x[num] = True